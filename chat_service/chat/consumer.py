from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .services.message_service import MessageService
from .services.group_service import GroupService
from .models import Message


messageService = MessageService()
groupService = GroupService()

#! APLICAR PATRON REPOSITORIO 
class ChatConsumer(AsyncWebsocketConsumer):
    '''
    Clase que se encarga de la comunicacion entre el cliente y el servidor del Chat

    params:
        - AsyncWebsocketConsumer: Clase que hereda de la clase AsyncWebsocketConsumer
    '''

    async def connect(self):    
        '''
        Metodo que se ejecuta cuando el cliente se conecta al servidor
        '''
        print('WEBSOCKET CONNECTED...')
        print("CHANNEL LAYER...", self.channel_layer)
        print("CHANNEL NAME...", self.channel_name)
        # Traemos el id del grupo para sacar el nombre del grupo
        self.group_id = self.scope['url_route']['kwargs']['groupkid']
        self.group_name = 'chat_%s' % self.group_id
        print('GROUP ID...', self.group_id)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        '''
        Metodo que se ejecuta cuando el cliente se desconecta del servidor

        args:
            close_code: Codigo de cierre de la conexion
        '''
        print('DISCONNECT', close_code)
        print("CHANNEL LAYER...", self.channel_layer)
        print("CHANNEL NAME...", self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None):
        '''
        Metodo que se ejecuta cuando el cliente envia un mensaje al servidor

        args:
            text_data: Mensaje enviado por el cliente
        '''
        print('RECEIVE', text_data)
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        user_id = data['user_id']
        group = await database_sync_to_async(groupService.get_by_id)(self.group_id)

        try: #TODO: Verificar despues con token
            print(message)
            print(username)
            print(user_id)
            print(group)
            if message != '':

                await messageService.add(message, user_id, username, group)

                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type': 'chat.message',
                        'message': message,
                        'username': username
                    }
                )
        except: 
            await self.send(text_data=json.dumps({
                'message': 'You are not authenticated'
            }))


    async def chat_message(self, event):
        '''
        Metodo que se ejecuta cuando el servidor envia un mensaje al cliente

        args:
            event: Mensaje enviado por el servidor
        '''
        print('Event..', event)
        await self.send(text_data = json.dumps({
            'message':event['message'],
            'username':event['username']
        }))