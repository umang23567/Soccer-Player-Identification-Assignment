import cv2

def read_video(video_path):
    cap=cv2.VideoCapture(video_path)
    frames=[]
    while True:
        flag,frame=cap.read()
        if not flag:
            break
        frames.append(frame)
    return frames

def save_video(video_frames, video_path, fps=30):
    if not video_frames:
        return
    height, width, channels = video_frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
    for frame in video_frames:
        out.write(frame)
    out.release()