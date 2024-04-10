import json
from typing import Union
import pika
import sys
import config

def send_message(message: Union[dict, list, str]):
    msg = json.dumps(message, ensure_ascii=False)
    credentials = pika.PlainCredentials(config.RABBITMQ_USER, config.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=config.RABBITMQ_HOST, 
        port=config.RABBITMQ_PORT, 
        credentials=credentials, 
        virtual_host=config.RABBITMQ_VHOST
    ))
    channel = connection.channel()
    # 声明一个持久化队列
    channel.queue_declare(queue='test_queue', durable=True)
    # 消息标记持久化
    channel.basic_publish(
        exchange='', 
        routing_key='test_queue', 
        body=msg,
        properties=pika.BasicProperties(
            delivery_mode = pika.DeliveryMode.Persistent
        )
    )
    print(" [x] send msg:", msg)
    connection.close()
    

if __name__ == "__main__":
    # msg = ' '.join(sys.argv[1:]) or "Hello, World!"
    # send_message({"data": msg})
    for i in range(20):
        send_message(f"message - {i}")