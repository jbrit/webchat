import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

class EchoConsumer(JsonWebsocketConsumer):
    def connect(self):
        # accept by default
        self.room = self.scope['url_route']['kwargs']['room']
        self.room_group_name = f"video_{self.room}"

        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

    # receives direct data from websocket and sends back object.data
    def receive_json(self, content):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            # type present to know correct handler
            {
                'type': 'general_message',
                'data': content,
                'sender_channel_name': self.channel_name
            }
        )
    
    def general_message(self, event):
        if self.channel_name != event['sender_channel_name']:
            self.send_json(event)


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    