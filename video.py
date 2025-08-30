import os
import cv2
import torch
from tqdm import tqdm

print("[INFO] Loading YOLOv5 model...")
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

video_path = "ayam4.mp4"  
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

base_name = os.path.splitext(os.path.basename(video_path))[0]
output_name = f"{base_name}_out.mp4"
out = cv2.VideoWriter(output_name, fourcc, fps, (width, height))

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
pbar = tqdm(total=frame_count, desc="Processing", unit="frame")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    output = results.render()[0]
    out.write(output)
    pbar.update(1)

cap.release()
out.release()
pbar.close()
print(f"[DONE] Video selesai diproses -> {output_name}")
