# Real-Time Human Detection with YOLOv12 & WebRTC

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Framework" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img alt="YOLO" src="https://img.shields.io/badge/YOLOv12-8A2BE2?style=for-the-badge&logo=yolo&logoColor=white"/>
  <img alt="WebRTC" src="https://img.shields.io/badge/WebRTC-D42E16?style=for-the-badge&logo=webrtc&logoColor=white"/>
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

<p align="center">
  A modern, high-performance web application for real-time human detection using the YOLOv12 model. This project leverages WebRTC for live webcam streaming and supports video file uploads for batch processing, all wrapped in a sleek, responsive UI.
</p>

<p align="center">
  <a href="https://human-detection-yolov12-with-flask-br6t.onrender.com" target="_blank">
    <img src="https://img.shields.io/badge/Live_Demo-WebApp-brightgreen?style=for-the-badge&logo=google-chrome" />
  </a>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/f7896047-a139-4114-bdf1-aba8dfa1d0c6" alt="Application Demo Screenshot" width="100%"/>
</p>

---

## ✨ Features

-   **🚀 Real-Time Webcam Detection:** Delivers low-latency human detection directly in the browser using WebRTC.
-   **📹 Video File Processing:** Allows users to upload video files for offline batch detection.
-   **💻 Modern Responsive UI:** A clean, intuitive interface built with glassmorphism and soft gradients that works on all devices.
-   **⚡ Blazing-Fast Inference:** Utilizes the highly efficient YOLOv12 nano model for rapid detection.
-   **🐳 Dockerized for Deployment:** Comes with a `Dockerfile` for easy, reproducible deployment in any environment.

---

## 🛠️ Technology Stack

-   **Backend:** Python, Flask, aiohttp, aiortc
-   **Machine Learning:** Ultralytics YOLOv12
-   **Frontend:** HTML5, CSS3, JavaScript
-   **Containerization:** Docker

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   Git
-   A webcam (for real-time detection)

### Installation Guide

1.  **Clone the Repository**
    ```sh
    git clone https://github.com/FaysalMehrab/human_detection_yolov12_with_flask.git
    cd human_detection_yolov12_with_flask
    ```

2.  **Set Up a Virtual Environment** (Recommended)
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Download the YOLOv12 Model**
    -   Download the `yolo12n.pt` model file from the [Ultralytics YOLOv12 releases](https://github.com/ultralytics/ultralytics) or a trusted source.
    -   Place the `yolo12n.pt` file in the project's root directory.

5.  **Run the Application**
    ```sh
    python server.py
    ```
    The application will be accessible at **[http://localhost:8000](http://localhost:8000/)**.

---

## 🐳 Docker Deployment

You can also build and run the application using Docker for a clean, isolated environment.

1.  **Build the Docker image:**
    ```sh
    docker build -t human-detection-app .
    ```

2.  **Run the Docker container:**
    ```sh
    docker run -p 8000:8000 human-detection-app
    ```
    Access the application at **[http://localhost:8000](http://localhost:8000/)**.

---

## 📁 Project Structure

```
human_detection_yolov12_with_flask/
├── 📄 app.py              # Flask server for video upload & processing
├── 📄 server.py            # aiohttp/aiortc server for real-time WebRTC logic
├── 📄 requirements.txt     # Python dependencies
├── 🐳 Dockerfile           # Instructions for building the Docker image
├── 🧠 yolo12n.pt           # YOLO model file (must be downloaded)
│
├── 📁 static/
│   └── 📜 main.js          # Frontend JavaScript for WebRTC and UI interaction
│
├── 📁 templates/
│   └── 📄 index.html       # The main HTML file for the user interface
│
├── 📁 uploads/             # Default directory for uploaded videos (auto-created)
└── 📁 processed/           # Default directory for processed videos (auto-created)
```

---

## 🙏 Acknowledgements

-   This project relies heavily on the incredible work by the teams behind [Ultralytics YOLO](https://github.com/ultralytics/ultralytics).
-   The real-time streaming is powered by the excellent [aiortc](https://github.com/aiortc/aiortc) library.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
