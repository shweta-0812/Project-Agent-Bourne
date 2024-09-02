from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def process_string_task(input_string):
    # Simulate processing
    processed_result = f"Processed: {input_string}"

    # Notify frontend using WebSockets
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "response_group",
        {
            "type": "send_response",
            "message": processed_result,
        },
    )
