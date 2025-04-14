from fastapi import APIRouter

from app.utils.rabbitmq import rabbitmq_client

router = APIRouter()

@router.post("/")
async def process():
    message = {
        'type': 'test_message',
        'message': 'Test message text'
    }
    await rabbitmq_client.publish(
        queue_name="test.queue",
        message_body=message
    )