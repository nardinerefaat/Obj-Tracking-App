# Object Tracking App

A web-based object tracking application built with **Streamlit** and **OpenCV** that detects and tracks moving objects in video files.

## Features

- **Video Upload**: Support for multiple video formats (MP4, MOV, AVI, MKV)
- **Background Subtraction**: Uses MOG2 (Mixture of Gaussians) algorithm for foreground detection
- **Object Detection**: Identifies moving objects using contour detection
- **Real-time Visualization**: Displays bounding boxes around detected objects
- **Interactive Web Interface**: User-friendly Streamlit interface

## Requirements

- Python 3.7+
- streamlit
- opencv-python (cv2)
- numpy

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install streamlit opencv-python numpy
   ```

## Usage

Run the application with:
```bash
streamlit run obj_track.py
```

The app will open in your default browser at `http://localhost:8501`

### Steps:
1. Click "Upload video" to select a video file
2. The app will process the video frame-by-frame
3. Moving objects will be highlighted with green bounding boxes
4. Frames are displayed in real-time as they are processed

## How It Works

1. **Background Subtraction**: The MOG2 algorithm separates foreground (moving objects) from background
2. **Contour Detection**: Identifies the boundaries of moving objects
3. **Filtering**: Objects with area < 300 pixels are filtered out to reduce noise
4. **Bounding Boxes**: Green rectangles are drawn around detected objects
5. **Display**: Processed frames are shown in the web interface

## Notes

- Minimum object size: 300 pixels (adjustable in code)
- Processing includes a 0.01s delay per frame for optimal visualization
- Color space is converted from BGR to RGB for proper web display

## Future Enhancements

- Multi-object tracking across frames
- Adjustable detection parameters in UI
- Performance optimization for large videos
- Export tracking results to file
