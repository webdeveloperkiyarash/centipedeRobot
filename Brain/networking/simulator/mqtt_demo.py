import json
import paho.mqtt.client as mqtt
from networking.mqtt.topics import topics


def run_mqtt_demo():
    client = mqtt.Client()

    def on_connect(client, userdata, flags, rc):
        print("Connected to MQTT broker with code", rc)
        client.subscribe(topics["command"].format(id="r1"))

    def on_message(client, userdata, msg):
        print("MQTT message received:", msg.topic, msg.payload.decode())

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)

    # ارسال یک پیام تستی
    cmd_msg = {
        "robotId": "r1",
        "cmd": "forward",
        "value": 0.7,
        "timeStamp": "2025-12-25T08:00:00Z"
    }
    client.publish(topics["command"].format(id="r1"), json.dumps(cmd_msg))
    client.loop_start()
