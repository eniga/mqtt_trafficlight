import paho.mqtt.client as mqtt
from time import sleep


def subscribe(broker, topic):
    client = mqtt.Client("Traffic Control 1")
    client.on_message = on_message  # attach function to callback
    print("Connecting to broker")
    client.connect(broker)
    client.loop_start()  # start the loop
    print("Subscribing to topic", topic)
    client.subscribe(topic)
    sleep(4)
    client.loop_stop()  # stop the loop


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
