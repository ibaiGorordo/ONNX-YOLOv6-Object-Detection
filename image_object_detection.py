import cv2
from imread_from_url import imread_from_url

from YOLOv6 import YOLOv6

# Initialize YOLOv6 object detector
model_path = "models/yolov6l_base_bs1.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.35, iou_thres=0.5)

# Read image
img_url = "https://upload.wikimedia.org/wikipedia/commons/a/af/Motorcyclists_lane_splitting_in_Bangkok%2C_Thailand.jpg"
img = imread_from_url(img_url)

# Detect Objects
boxes, scores, class_ids = yolov6_detector(img)

# Draw detections
combined_img = yolov6_detector.draw_detections(img)
cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Objects", combined_img)
cv2.imwrite("doc/img/detected_objects.jpg", combined_img)
cv2.waitKey(0)
