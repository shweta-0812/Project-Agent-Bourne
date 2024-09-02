from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the connection
        await self.accept()

    async def disconnect(self, close_code):
        # Close the connection
        pass

    async def receive(self, text_data):
        # Receive a message and send it back
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'message': data['message']
        }))
