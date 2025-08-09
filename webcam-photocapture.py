import cv2
from datetime import datetime
import os
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot access webcam.")
    exit()
print("📷 Press SPACE to capture photo or ESC to exit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame.")
        break
    cv2.imshow("Webcam - Press SPACE to capture", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == 32:
        folder = "captured_photos"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(folder, f"photo_{timestamp}.jpg")
        cv2.imwrite(file_path, frame)
        print(f"✅ Photo saved as {file_path}")
cap.release()
cv2.destroyAllWindows()
