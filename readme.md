# python 直接使用 rabbitmq 的一个示例

## 安装
```shell
pip install -r requirements.txt
```

## 使用

### 配置
修改rabbitmq服务相关配置
```shell
cp .env.example .env
```

### 生产者（经典队列）
```shell
python classic_producer.py
```

### 消费者（经典队列）
```shell
python classic_worker.py
```
可运行多个消费者看公平调度策略，随意关停看是否有消息丢失，stop rabbitmq 队列看是否有消息丢失。

### 生产者（仲裁队列）
```shell
python quorum_producer.py
```

### 消费者（仲裁队列）
```shell
python quorum_worker.py
```


## 参考
- [rabbitmq-tutorials](https://github.com/rabbitmq/rabbitmq-tutorials/tree/main/python)
