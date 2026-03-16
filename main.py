import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.video_utils import read_video, save_video
from tracker.tracker import Tracker

def main():
    # Read Video
    video_frames = read_video('input_video/SPLvideo.mp4')

    # initialise tracker
    tracker = Tracker('models/best.pt') 

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=False,
                                       stub_path='stubs/tracks_stub.pkl')
    
    #Draw output
    ##Draw object Tracks 
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save Video 
    save_video(output_video_frames, 'output_videos/output_video.avi')

if __name__ == '__main__':
    main()    