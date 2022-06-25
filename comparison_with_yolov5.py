import cv2
import pafy

from YOLOv6 import YOLOv6

# Initialize video
# cap = cv2.VideoCapture("input.avi")

videoUrl = 'https://youtu.be/trNO5Imf1Q8'
videoPafy = pafy.new(videoUrl)
print(videoPafy.streams)
cap = cv2.VideoCapture(videoPafy.streams[-1].url)
start_time = 0  # skip first {start_time} seconds
cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * 60)

# Initialize object localizer
yolov6_path = "models/yolov6s.onnx"
yolov6_detector = YOLOv6(yolov6_path, conf_thres=0.5, iou_thres=0.5)

yolov5_path = "models/yolov5s6.onnx"
yolov5_detector = YOLOv6(yolov5_path, conf_thres=0.5, iou_thres=0.5)

cv2.namedWindow("Model comparison", cv2.WINDOW_NORMAL)
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
        break

    # Update object localizer
    yolov6_detector(frame)

    yolov5_detector(frame)

    yolov6_img = yolov6_detector.draw_detections(frame)
    yolov5_img = yolov5_detector.draw_detections(frame)

    combined_img = cv2.hconcat([yolov5_img, yolov6_img])
    combined_img = cv2.resize(combined_img, (3840, 2160))
    cv2.putText(combined_img, "YOLOv5", (combined_img.shape[1]//4, 60), cv2.FONT_HERSHEY_DUPLEX, 2.4, (55, 55, 55), 4)
    cv2.putText(combined_img, "YOLOv6", (combined_img.shape[1]*3//4, 60), cv2.FONT_HERSHEY_DUPLEX, 2.4, (55, 55, 55), 4)

    cv2.imshow("Model comparison", combined_img)