import os
import cv2
import uuid
from flask import Flask, render_template, request, send_file, redirect, url_for
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv'}
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB limit

# Create directories if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

# Load the YOLOv12 model once when the app starts
model = YOLO('yolo12n.pt')  # Nano version for faster processing

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def process_video(input_path, output_path):
    """Process video with YOLOv12 human detection"""
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        return False, "Error opening video file"
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Initialize VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    frame_num = 0
    human_count = 0
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
            
        # Run YOLOv12 inference
        results = model(frame, classes=[0])  # Class 0 is 'person'
        
        # Visualize results and count humans
        annotated_frame = results[0].plot()
        current_humans = len(results[0].boxes)
        if current_humans > human_count:
            human_count = current_humans
        
        # Write processed frame
        out.write(annotated_frame)
        
        # Update progress
        frame_num += 1
        progress = int((frame_num / frame_count) * 100)
    
    cap.release()
    out.release()
    return True, human_count

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    """Handle video upload and processing"""
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = secure_filename(file.filename)
        unique_id = uuid.uuid4().hex
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique_id}_{filename}")
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], f"processed_{unique_id}_{filename}")
        
        # Save uploaded file
        file.save(input_path)
        
        # Process video
        start_time = datetime.now()
        success, human_count = process_video(input_path, output_path)
        processing_time = (datetime.now() - start_time).total_seconds()
        
        if success:
            # Generate a preview video URL
            preview_url = url_for('preview_video', filename=f"processed_{unique_id}_{filename}")
            
            return render_template('result.html', 
                                  input_file=filename,
                                  output_file=f"processed_{unique_id}_{filename}",
                                  preview_url=preview_url,
                                  human_count=human_count,
                                  processing_time=f"{processing_time:.2f}")
        else:
            return render_template('error.html', message="Error processing video")
    
    return render_template('error.html', message="Invalid file format")

@app.route('/preview/<filename>')
def preview_video(filename):
    """Serve processed video for preview"""
    return send_file(os.path.join(app.config['PROCESSED_FOLDER'], filename), 
                     mimetype='video/mp4')

@app.route('/download/<filename>')
def download_video(filename):
    """Download processed video"""
    return send_file(os.path.join(app.config['PROCESSED_FOLDER'], filename), 
                     as_attachment=True,
                     download_name=f"detected_{filename}")

if __name__ == '__main__':
    app.run(debug=True)