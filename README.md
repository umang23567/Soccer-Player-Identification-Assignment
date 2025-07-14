# Soccer-Player-Identification-Assignment

This project detects and tracks players, referees, and the ball from a soccer video using YOLOv8 and ByteTrack. The final output is an annotated video showing tracked objects with bounding ellipses and IDs.

Directory Structure
├── main.py                     # Main entry point
├── model.pt                    # YOLO model 
├── 15sec_input_720p.mp4        # Input soccer video
├── output_videos/
│   └── output.mp4              # Annotated output video
├── stubs/
│   └── track_stubs.pkl         # Optional: cached tracking data
├── trackers/
│   ├── __init__.py
│   └── tracker.py              # Tracker class using YOLO + ByteTrack
├── utils/
│   ├── __init__.py
│   └── video_utils.py          # Video reading/writing helpers
├── analysis.ipynb              # (Optional) Notebook for analysis
├── .gitattributes
└── README.md

Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/soccer-tracking.git
cd soccer-tracking
2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
Create and use this requirements.txt:
ultralytics>=8.0.20
supervision>=0.12.0
opencv-python
numpy<2.0  # Ensure compatibility with older binary modules
Install with:
pip install -r requirements.txt
▶️ How to Run
Ensure the following files are present:
15sec_input_720p.mp4 — input video
model.pt — YOLOv8 model file
Then run:
python main.py
This will:
Load the video
Detect and track objects
Annotate frames with ellipses and IDs
Save the output to: output_videos/output.mp4
