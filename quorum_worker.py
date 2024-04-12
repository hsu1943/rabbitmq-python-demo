import pika
import os
import sys
import time
import random
import config

def main():
    credentials = pika.PlainCredentials(config.RABBITMQ_USER, config.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config.RABBITMQ_HOST, 
        port=config.RABBITMQ_PORT, 
        credentials=credentials, 
        virtual_host=config.RABBITMQ_VHOST
    ))
    channel = connection.channel()

    # 使用仲裁队列
    channel.queue_declare(queue='test_quorum_queue', arguments={"x-queue-type": 'quorum'}, durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received {}".format(body.decode()))
        second = random.randint(1, 5)
        time.sleep(second)
        print(" [x] Done in {} seconds".format(second))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # 公平调度
    channel.basic_qos(prefetch_count=1)

    # 手动确认消息，auto_ack=True则是自动提交
    channel.basic_consume(queue='test_quorum_queue', on_message_callback=callback)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)