# Real-Time Human Detection using YOLOv12

A professional, modern web application for real-time human detection using YOLOv12 and WebRTC.  
Built with Python, Flask, aiohttp, aiortc, and Ultralytics YOLO.  
Supports both live webcam detection and video file uploads.

---

## Features

- **Real-time webcam human detection** (WebRTC, browser-based)
- **Video file upload and batch detection**
- **Modern, responsive UI** (glassmorphism, soft gradients)
- **Fast inference** with YOLOv12 nano model
- **Docker support** for easy deployment

---

## Demo

![UI Screenshot](screenshot.png) <!-- Add your screenshot here -->

---

## Requirements

- Python 3.8+
- [YOLOv8/YOLOv12 nano model](https://github.com/ultralytics/ultralytics) (`yolo12n.pt`)
- See [`requirements.txt`](requirements.txt) for Python dependencies

---

## Installation

### 1. Clone the repository

```sh
gh repo clone FaysalMehrab/human_detection_yolov12_with_flask
cd human_detection_yolov12_with_flask
```

### 2. Download YOLO Model

Place your YOLOv12 nano model file (e.g., `yolo12n.pt`) in the project root.

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the server

```sh
python server.py
```

Open [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## Docker

Build and run with Docker:

```sh
docker build -t human-detection .
docker run -p 8000:8000 human-detection
```

---

## Project Structure

```
Human_detection using yolov8/
│
├── app.py                  # Flask app for video upload & batch detection
├── server.py               # aiohttp + aiortc server for real-time detection
├── requirements.txt
├── Dockfiler               # Dockerfile (rename to Dockerfile if needed)
├── yolo12n.pt              # YOLO model (download separately)
│
├── static/
│   └── main.js             # WebRTC and UI JS
│
├── templates/
│   └── index.html          # Main UI
│
├── uploads/                # Uploaded videos (auto-created)
├── processed/              # Processed videos (auto-created)
```

---

## Usage

- **Live Detection:**  
  Open the web app, allow camera access, and click "Start Detection".
- **Video Upload:**  
  (If enabled in `app.py`) Upload a video file and get a processed video with detected humans.

---

## Credits

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [aiortc](https://github.com/aiortc/aiortc)
- [CSE Project HUB](https://github.com/yourusername)

---

## License

MIT License

---

> **Made with ❤️ by CSE Project
