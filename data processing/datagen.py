import cv2
import os

path = "IMG_2603.mov"
save_dir = r"..\frames\empty"

os.makedirs(save_dir,exist_ok=True)

cap = cv2.VideoCapture(path)
frame_num = 0
print("Opened:", cap.isOpened())



while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imwrite(f"{save_dir}/2frame_{frame_num:05d}.jpg", frame)
    frame_num += 1

cap.release()