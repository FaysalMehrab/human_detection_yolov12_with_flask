import asyncio
import json
import os
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
from av import VideoFrame
from ultralytics import YOLO
import cv2

# Load YOLOv12 model for human detection
model = YOLO('yolo12n.pt')

# Custom VideoStreamTrack for human detection
class HumanDetectionTrack(VideoStreamTrack):
    def __init__(self, track):
        super().__init__()
        self.track = track
        self.frame_count = 0
        self.last_annotated = None

    async def recv(self):
        frame = await self.track.recv()
        img = frame.to_ndarray(format="bgr24")
        self.frame_count += 1

        # Only run YOLO every 5th frame, reuse last result for others
        if self.frame_count % 5 == 0 or self.last_annotated is None:
            img_resized = cv2.resize(img, (160, 160))  # Lower resolution for faster inference
            results = model(img_resized, classes=[0])
            annotated_img = results[0].plot()
            annotated_img = cv2.resize(annotated_img, (frame.width, frame.height))
            self.last_annotated = annotated_img
        else:
            annotated_img = self.last_annotated

        annotated_frame = VideoFrame.from_ndarray(annotated_img, format="bgr24")
        annotated_frame.pts = frame.pts
        annotated_frame.time_base = frame.time_base
        return annotated_frame

# Set up aiohttp application
app = web.Application()

# Serve the index page
async def index(request):
    with open('templates/index.html', 'r') as f:
        content = f.read()
    return web.Response(content_type="text/html", text=content)

# Handle WebRTC offer from client
async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])
    
    pc = RTCPeerConnection()
    
    @pc.on("track")
    def on_track(track):
        if track.kind == "video":
            pc.addTrack(HumanDetectionTrack(track))
    
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    
    return web.Response(
        content_type="application/json",
        text=json.dumps({
            "sdp": pc.localDescription.sdp,
            "type": pc.localDescription.type
        }),
    )

# Define routes
app.router.add_get("/", index)
app.router.add_post("/offer", offer)
app.router.add_static("/static/", path="static/")

# Run the application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    web.run_app(app, host="0.0.0.0", port=port)
