from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from base.models import Message
from django.contrib.auth import get_user_model

class PersonalChatConsumer(AsyncWebsocketConsumer):
    """chat consumer"""

    async def connect(self):
        """connect to channel"""
        request_user = self.scope['user']
        print(request_user)
        if request_user.is_authenticated:
            chat_with_user = self.scope['url_route']['kwargs']['id']
            user_ids = [int(request_user.id), int(chat_with_user)]
            user_ids = sorted(user_ids)
            self.room_group_name = f"chat_{user_ids[0]}-{user_ids[1]}"
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
    
    async def receive(self, text_data=None, bytes_data=None):
        """receive group message"""

        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        await self.save_message(self.scope['user'].id, self.scope['url_route']['kwargs']['id'], message)

    async def diconnect(self):
        """diconnect from channel"""
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def chat_message(self, event):
        """send chat message"""

        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    @database_sync_to_async
    def save_message(self, sender, receiver, message):
        """save message to database"""
        receiver = get_user_model().object.get(id=receiver)
        sender = get_user_model().object.get(id=sender)
        Message.objects.create(sender=sender, receiver=receiver, message=message)
