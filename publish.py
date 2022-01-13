import paho.mqtt.client as mqtt


def publish(broker, topic, message):
    client = mqtt.Client("Traffic Control 1")
    client.connect(broker)
    client.publish(topic, message)  # Publish
