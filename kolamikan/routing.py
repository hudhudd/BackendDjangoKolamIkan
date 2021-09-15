from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from datakolam.consumers import MqttConsumer

application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "mqtt.pub": MqttConsumer,
        "mqtt.sub": MqttConsumer,
    }),
})
