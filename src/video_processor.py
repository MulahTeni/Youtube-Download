import cv2
import os
from pathlib import Path

def process_video():
    # Create directories if they don't exist
    Path("vids/halved").mkdir(parents=True, exist_ok=True)
    Path("vids/used").mkdir(parents=True, exist_ok=True)
    
    # Get the first video from downloaded folder
    downloaded_dir = "vids/downloaded"
    video_files = [f for f in os.listdir(downloaded_dir) if f.endswith(('.mp4', '.mov', '.avi'))]
    
    if not video_files:
        print("No videos found in vids/downloaded")
        return
    
    video_path = os.path.join(downloaded_dir, video_files[0])
    
    # Open the video
    cap = cv2.VideoCapture(video_path)
    print("Video opened")
    
    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Set exact dimensions for output (960x1080)
    new_width = 960
    new_height = 1080
    

    # Create output video writer
    output_path = f"vids/halved/{video_files[0]}"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))
    
    print("Processing video")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Get dimensions of the frame
        h, w = frame.shape[:2]
        
        # Calculate the size and position of the square crop
        size = min(h, w)
        x = (w - size) // 2
        y = (h - size) // 2
        
        # Crop the frame to a square
        cropped_frame = frame[y:y+size, x:x+size]
        
        # Resize the square to 960x1080
        resized_frame = cv2.resize(cropped_frame, (new_width, new_height))
        
        # Write the frame
        out.write(resized_frame)
    
    # Release everything
    cap.release()
    out.release()
    
    # Move original file to used folder
    os.rename(video_path, f"vids/used/{video_files[0]}")
    print(f"Processed {video_files[0]}")

if __name__ == "__main__":
    process_video()
