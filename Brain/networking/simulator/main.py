from networking.simulator import mqtt_demo, hotspot_demo, webrtc_demo
from networking.hotspot.manager import HotspotManager
from networking.webrtc.connection import WebRTCConnection
from networking.mqtt.topics import topics
import json


def run_simulator():
    print("=== Simulator Started ===")

    # 1. MQTT Demo
    print("\n--- MQTT Demo ---")
    mqtt_demo.run_mqtt_demo()

    # 2. Hotspot Demo
    print("\n--- Hotspot Demo ---")
    hotspot_demo.run_hotspot_demo()

    # 3. WebRTC Demo
    print("\n--- WebRTC Demo ---")
    webrtc_demo.run_webrtc_demo()

    print("\n=== Simulator Finished ===")


if __name__ == "__main__":
    run_simulator()
