from aio_pika import IncomingMessage
from fastapi import APIRouter

from app.utils.rabbitmq import rabbitmq_client

router = APIRouter()

TEST_QUEUE = "test.queue"

@router.post("/")
async def process():
    message = {
        'type': 'test_message',
        'message': 'Test message text'
    }
    await rabbitmq_client.publish(
        queue_name=TEST_QUEUE,
        message_body=message
    )


async def handle_event(message: IncomingMessage):
    async with message.process():
        body = message.body.decode()
        print(f"[IncomingMessage] Received: {body}")


async def start_consumer():
    await rabbitmq_client.setup_consumer(TEST_QUEUE, handle_event)