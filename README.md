# VideoDetection
YOLOv5 Video Detection

Project ini menggunakan **YOLOv5** untuk mendeteksi objek di video, menampilkan bounding box, dan menyimpan output video.

---

## 1. Prasyarat
- Python 3.9+
- CUDA (opsional, untuk GPU)

---

## 2. Instalasi Dependencies

Jalankan perintah berikut di terminal:

```bash
# Install PyTorch (GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install OpenCV untuk video processing
pip install opencv-python

# Install tqdm untuk progress bar
pip install tqdm

# Opsional: Matplotlib 
pip install matplotlib


# simpan video di bagian ini didalam Video.py
video_path = "ayam4.mp4"  
cap = cv2.VideoCapture(video_path)
