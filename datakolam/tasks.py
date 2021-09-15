from __future__ import absolute_import, unicode_literals

from celery.schedules import crontab
from celery import shared_task

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import paho.mqtt.publish as publish


channel_layer = get_channel_layer()

@shared_task(bind=True)
def mqtt_test(self, msg):
    print(f"Celery task say: \"{msg}\"")
    host = "127.0.0.1"
    topic = "some_topic"

    # If broker asks user/password.
    auth = {'username': "", 'password': ""}

    # If broker asks client ID.
    client_id = ""

    publish.single(topic, payload=msg+"123", qos=1, hostname=host)

    async_to_sync(channel_layer.send)('mqtt', {
        'type': 'mqtt.pub',
        'text': {
            'topic': topic, 
            'payload': f"{msg} - {self.request.id}"
        }
    })
