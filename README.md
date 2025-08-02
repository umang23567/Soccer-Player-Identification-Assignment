# ⚽ Soccer-Player-Identification-Assignment

This project detects and tracks players, referees, and the ball from a soccer video using **YOLOv11** and **ByteTrack**. The final output is an annotated video showing tracked objects with bounding ellipses and player IDs.

---

## 📁 Directory Structure

```
.
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
```

---

## 🔧 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/umang23567/Soccer-Player-Identification-Assignment.git
cd Soccer-Player-Identification-Assignment
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

Install the packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Ensure the following files are present in the root directory:

- `15sec_input_720p.mp4` — input video
- `model.pt` — YOLOv8 model file

Then run the main script:

```bash
python main.py
```

### This will:

- Load the video
- Detect and track objects (players, referee, ball)
- Annotate frames with bounding ellipses and IDs
- Save the final output to `output_videos/output.mp4`

---

## 📌 Notes

- Uses cached tracking data from `stubs/track_stubs.pkl` if available (for faster reruns).
- Replace the video or model file as needed — just update the path in `main.py`.
- Goalkeepers are relabeled as players during post-processing.

---

## ✏️ Optional

- Use `analysis.ipynb` for further exploration or visualization.
- Modify `draw_annotations()` or `draw_ellipse()` in `tracker.py` for different overlay styles.

---

