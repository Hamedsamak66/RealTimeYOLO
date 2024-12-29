from ultralytics import YOLO
import cv2
'''
import torch
if torch.cuda.is_available():
    print(f"CUDA is available. Device name: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available.")
exit()
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
exit()
'''
# بارگذاری مدل YOLOv8
model = YOLO('yolov8x.pt')  # استفاده از مدل دقیق‌تر (x). می‌توانید مدل دیگری مثل 'yolov8s.pt' را انتخاب کنید.

# دسترسی به دوربین
cap = cv2.VideoCapture(0)

# تنظیم رزولوشن دوربین (اختیاری)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

if not cap.isOpened():
    print("Cannot access the camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # تشخیص اشیاء روی فریم
    results = model(frame)

    # گرفتن تعداد اشیاء شناسایی‌شده
    detected_objects = len(results[0].boxes)  # تعداد اشیاء شناسایی‌شده

    # رسم جعبه‌ها و اطلاعات روی تصویر
    annotated_frame = results[0].plot()  # فریمی با جعبه‌های محاط‌کننده و برچسب‌ها

    # افزودن تعداد اشیاء به تصویر
    cv2.putText(annotated_frame, f'Detected Objects: {detected_objects}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # نمایش تصویر
    cv2.imshow('YOLOv8 Object Detection', annotated_frame)

    # خروج با کلید 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
