import datetime
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer
from .models import Datakol
from django.contrib.auth.models import User

class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        x = payload
        # print(x)
        if 'ph' in x:
            # save_model = Datakol(ph=x['ph'],temp=x['temp'],alat=x['alat'],owner=User.objects.get(id=x['owner']))

            save_model = Datakol(ph=x['ph'],temp=x['temp'],alat=bool(x['alat']),owner=User.objects.get(id=2))

            save_model.save()
            print("topic: {0}, payload: {1}".format(topic, x))
        else:
            print('Tidak masuk database')

    def mqtt_pub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        print("topic: {0}, payload: {1}".format(topic, payload))
