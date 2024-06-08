from channels.generic.websocket import AsyncWebsocketConsumer

class PersonalChatConsumer(AsyncWebsocketConsumer):
    """chat consumer"""

    async def connect(self):
        """connect to channel"""
        print("TESTING CONNECTION AND REDIS")
        await self.accept()
