import paho.mqtt.client as mqtt
import time


def on_connect(client, usardata, flags, rc):
    if rc == 0:
        client.connected_flag + True
        print("connected OK")
    else:
        print("Bad connection return code=", rc)


mqtt.Client.connected_flag = False
broker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Traffic Control 1")
client.on_connect = on_connect
client.loop_start()
print("Connecting to broker", broker)
client.connect(broker)
while not client.connected_flag:
    print("In wait loop")
    time.sleep(1)
print("In main loop")
client.loop_stop()
client.disconnect()
