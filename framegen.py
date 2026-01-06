import cv2
import random

video_path = "vid1_A_aerial.mp4"   # change if needed
output_path = "random_frame.png"

cap = cv2.VideoCapture(video_path)

# Check video opened
if not cap.isOpened():
    raise IOError("Cannot open video file")

# Total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total frames:", total_frames)

# Pick a random frame index
random_frame_idx = random.randint(0, total_frames - 1)
print("Selected frame:", random_frame_idx)

# Jump to that frame
cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_idx)

# Read the frame
ret, frame = cap.read()
if not ret:
    raise IOError("Failed to read frame")

# Save frame
cv2.imwrite(output_path, frame)

cap.release()

print(f"Saved random frame to {output_path}")
