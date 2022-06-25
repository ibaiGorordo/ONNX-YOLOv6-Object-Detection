import cv2

from YOLOv6 import YOLOv6

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize YOLOv6 object detector
model_path = "models/yolov6s.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.7, iou_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():

    # Read frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids = yolov6_detector(frame)

    combined_img = yolov6_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)

    # Press key q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
