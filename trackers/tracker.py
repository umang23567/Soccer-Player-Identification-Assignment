from ultralytics import YOLO
import supervision as sv
import pickle
import os
import sys
import cv2

class Tracker:
    
    def __init__(self,model_path):
        self.model=YOLO(model_path)
        self.tracker=sv.ByteTrack()
        
    def detect_frames(self,frames):
        batch_size=20
        detections=[]
        for i in range(0,len(frames),batch_size):
            detections_batch = self.model.predict(frames[i:i+batch_size], conf=0.3)
            detections.extend(detections_batch)
        return detections
    
    def get_object_tracks(self,frames,read_from_stub=False,stub_path=None):
        
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path,'rb') as f:
                tracks=pickle.load(f)
            return tracks
        
        detections=self.detect_frames(frames)
        
        tracks={
            "players":[],
            "referee":[],
            "ball":[]
        }
        
        for frame_num,detection in enumerate(detections):
            
            cls_names=detection.names
            cls_names_inv={v:k for k,v in cls_names.items()}
            
            detection_supervision=sv.Detections.from_ultralytics(detection)
            
            for obj_ind, cls_id in enumerate(detection_supervision.class_id):
                if (cls_names[cls_id]=="goalkeeper"):
                    detection_supervision.class_id[obj_ind]=cls_names_inv["player"]
            
            detection_with_tracks=self.tracker.update_with_detections(detection_supervision)
            
            tracks["players"].append({})
            tracks["referee"].append({})
            tracks["ball"].append({})
            
            for frame_detection in detection_with_tracks:
                
                bbox=list(frame_detection[0])
                # conf=frame_detection[1]
                cls_id=frame_detection[3]
                track_id=frame_detection[4]
                
                if (cls_id==cls_names_inv["player"]):
                    tracks["players"][frame_num][track_id]={"bbox":bbox}
                if (cls_id==cls_names_inv["referee"]):
                    tracks["referee"][frame_num][track_id]={"bbox":bbox}
                    
            for frame_detection in detection_supervision:
                
                bbox=list(frame_detection[0])
                # conf=frame_detection[1]
                cls_id=frame_detection[3]
                track_id=frame_detection[4]
                
                if (cls_id==cls_names_inv["ball"]):
                    tracks["ball"][frame_num]={"bbox":bbox}
                
        if stub_path is not None:
            with open(stub_path,'wb') as f:
                pickle.dump(tracks,f)
                
        return tracks
        
    def draw_ellipse(self,frame,bbox,colour,track_id=None):
        x1,y1,x2,y2=bbox
        x_centre=int((x1+x2)/2)
        y2=int(y2)
        cv2.ellipse(
            frame,
            (x_centre,y2),
            (int(x2-x1),int(0.35*(x2-x1))),
            0.0,
            -45,
            235,
            colour,
            2,
            cv2.LINE_8,
            )
        
        w=40
        h=20
        x1_rect=x_centre-w//2
        x2_rect=x_centre+w//2
        y1_rect=(y2-h//2) +15
        y2_rect=(y2+h//2) +15
        
        if track_id is not None:
            cv2.rectangle(
                frame,
                (x1_rect,y1_rect),
                (x2_rect,y2_rect),
                colour,
                cv2.FILLED
                )
            x1_text=x1_rect+12
            if track_id>99:
                x1_text-=10
            cv2.putText(
                frame,
                str(track_id),
                (x1_text,y1_rect+15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,0,0),
                2
            )
        
        return frame

    def draw_annotations(self,frames,tracks):
        
        output_frames=[]
        for frame_num,frame in enumerate(frames):
            
            frame=frame.copy()
            player_dict=tracks["players"][frame_num]
            referee_dict=tracks["referee"][frame_num]
            ball_dict=tracks["ball"][frame_num]
            
            for track_id,player in player_dict.items():
                frame=self.draw_ellipse(frame,player["bbox"],(0,0,255),track_id)
            for _,referee in referee_dict.items():
                frame=self.draw_ellipse(frame,referee["bbox"],(0,255,255))
                
            output_frames.append(frame)
                
        return output_frames