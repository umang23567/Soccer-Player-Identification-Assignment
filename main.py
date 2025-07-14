from utils.video_utils import read_video,save_video
from trackers import Tracker

def main():
    
    #Read video
    video_frames=read_video('15sec_input_720p.mp4')

    #Initialize tracker
    tracker = Tracker('model.pt')
    tracks=tracker.get_object_tracks(video_frames,
                                     read_from_stub=True,
                                     stub_path='stubs/track_stubs.pkl')
    
    #Draw output
    #Draw object tracks
    output_video_frames=tracker.draw_annotations(video_frames,tracks)
    
    #Save video
    save_video(output_video_frames,'output_videos/output.mp4')
    
if __name__=='__main__':
    main()