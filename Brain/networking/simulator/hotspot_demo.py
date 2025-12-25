from networking.hotspot.manager import HotspotManager


def run_hotspot_demo():
    manager = HotspotManager()
    manager.start_hotspot()
    status = manager.status()
    print("Hotspot status:", status)
    manager.stop_hotspot()
