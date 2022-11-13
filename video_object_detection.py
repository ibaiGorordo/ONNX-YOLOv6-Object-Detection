import cv2
from cap_from_youtube import cap_from_youtube

from YOLOv6 import YOLOv6

# # Initialize video
# cap = cv2.VideoCapture("input.avi")

videoUrl = 'https://youtu.be/yXEb0fWLJIY'
cap = cap_from_youtube(videoUrl)
start_time = 0  # skip first {start_time} seconds
cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * 30)

# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (1280, 720))

# Initialize object localizer
model_path = "models/yolov6s.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.5, iou_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

    try:
        # Read frame from the video
        ret, frame = cap.read()
        if not ret:
            break
    except Exception as e:
        print(e)
        continue

    # Update object localizer
    boxes, scores, class_ids = yolov6_detector(frame)

    combined_img = yolov6_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)
    # out.write(combined_img)

# out.release()
