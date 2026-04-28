import cv2
import os

video_path = "/home/svdgsinstallationpc3/Videos/Screencasts/B_09.mp4"
output_folder = "input"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video not found")
    exit()

fps = int(cap.get(cv2.CAP_PROP_FPS))
print("CAP:", cap)
if  fps <= 1 or fps >100:
    fps = 10
print("FPS:", fps)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % fps == 0:
        frame_filename = os.path.join(output_folder, f"frame_{saved_count:06d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()

print("Total frames processed:", frame_count)
print("Frames saved (1 per second):", saved_count)