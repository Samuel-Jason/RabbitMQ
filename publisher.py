from typing import Dict
import pika
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self._host = "localhost"
        self._port = 5672
        self._username = "guest"
        self._password = "guest"
        self._channel = self.__create_channel()
        self._exchange = "data_exchange"
        self._routing_key = ""

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self._host,
            port=self._port,
            credentials=pika.PlainCredentials(
                username=self._username,
                password=self._password
            )
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        return channel

    def send_message(self, body: Dict):
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2  # make message persistent
            )
        )

rabbitmq_publisher = RabbitmqPublisher()
rabbitmq_publisher.send_message({"ola": "mundo"})
