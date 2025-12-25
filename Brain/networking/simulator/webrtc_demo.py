import asyncio
from networking.webrtc.connection import WebRTCConnection


def run_webrtc_demo():
    async def demo():
        conn = WebRTCConnection()
        channel = conn.add_data_channel("demo")
        channel.on("open", lambda: channel.send("Hello from WebRTC demo!"))
        offer = await conn.create_offer()
        # فقط بخشی از SDP برای نمایش
        print("WebRTC Offer created:\n", offer.sdp[:100], "...")
        await conn.close()

    asyncio.run(demo())
