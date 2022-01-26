from subscribe import subscribe
from publish import publish
from time import sleep
import threading
from trafficlight import blink_red, blink_green, blink_amber

broker = "test.mosquitto.org"
topic = "trafficlight/bradford"

try:
    # subscribe to the topic
    thr = threading.Thread(target=subscribe, args=(broker, topic))
    thr.start()
    while thr.is_alive():
        # publish traffic data to the broker on the topic
        publish(broker, topic, "{light: amber, signal: OFF, duration: 0}")
        publish(broker, topic, "{light: red, signal: ON, duration: 5}")
        sleep(1)  # Add a second delay before the traffic light change to ensure the user has gotten the message
        blink_red()  # Change traffic light to Red for 5 seconds
        publish(broker, topic, "{light: red, signal: OFF, duration: 0}")
        publish(broker, topic, "{light: amber, signal: ON, duration: 2}")
        sleep(1)  # Add a second delay before the traffic light change to ensure the user has gotten the message
        blink_amber()  # Change traffic light to Amber for 2 seconds
        publish(broker, topic, "{light: amber, signal: OFF, duration: 0}")
        publish(broker, topic, "{light: green, signal: ON, duration: 10}")
        sleep(1)  # Add a second delay before the traffic light change to ensure the user has gotten the message
        blink_green()  # Change Traffic light to Green for 10 seconds
except KeyboardInterrupt:
    pass
