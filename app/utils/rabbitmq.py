import logging
from typing import Callable

from aio_pika import connect_robust, Message, DeliveryMode, IncomingMessage
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

from app.core.config import settings

RABBITMQ_URL = f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}"

# references : https://github.com/kieled/fastapi-aiopika-boilerplate
class RabbitMQClient:
    connection: AbstractRobustConnection | None = None
    channel: AbstractRobustChannel | None = None

    def __init__(self):
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await connect_robust(RABBITMQ_URL)
        self.channel = await self.connection.channel()
        logging.info("🟢 RabbitMQ에 연결되었습니다: %s", RABBITMQ_URL)

    async def publish(self, queue_name: str, message_body: dict):
        await self.channel.declare_queue(name=queue_name, durable=True)
        message = Message(
            body=str(message_body).encode(),
            delivery_mode=DeliveryMode.PERSISTENT
        )
        await self.channel.default_exchange.publish(message, routing_key=queue_name)

    async def close(self):
        await self.connection.close()


    async def setup_consumer(self, queue_name: str, callback: Callable[[IncomingMessage], None]):
        connection = await self.connect()
        queue = await self.channel.declare_queue(queue_name, durable=True)

        await queue.consume(callback)

rabbitmq_client = RabbitMQClient()
