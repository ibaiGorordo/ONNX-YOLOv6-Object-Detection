# ONNX YOLOv6 Object Detection
 Python scripts performing object detection using the YOLOv6 model in ONNX.

![! ONNX YOLOv6 Object Detection](https://github.com/ibaiGorordo/ONNX-YOLOv6-Object-Detection/blob/main/doc/img/detected_objects.jpg)
*Original image: https://commons.wikimedia.org/wiki/File:Motorcyclists_lane_splitting_in_Bangkok,_Thailand.jpg*

# Important
- The input images are directly resized to match the input size of the model. I skipped adding the pad to the input image, it might affect the accuracy of the model if the input image has a different aspect ratio compared to the input size of the model. Always try to get an input size with a ratio close to the input images you will use.
- The original YOLOv6 repository is still in development, so things might not work in the future.

# Requirements

 * Check the **requirements.txt** file. 
 * For ONNX, if you have a NVIDIA GPU, then install the **onnxruntime-gpu**, otherwise use the **onnxruntime** library.
 * Additionally, **pafy** and **youtube-dl** are required for youtube video inference.
 
# Installation
```
git clone https://github.com/ibaiGorordo/ONNX-YOLOv6-Object-Detection.git
cd ONNX-YOLOv6-Object-Detection
pip install -r requirements.txt
```
### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`

### For youtube video inference
```
pip install youtube_dl
pip install git+https://github.com/zizo-pro/pafy@b8976f22c19e4ab5515cacbfae0a3970370c102b
```

# ONNX model 
The original model was converted to ONNX using the following Colab notebook from the original repository, run the notebook and save the download model into the [models  folder](https://github.com/ibaiGorordo/ONNX-YOLOv6-Object-Detection/tree/main/models):
- **Convert YOLOv6 ONNX for Inference** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pke1ffMeI2dXkIAbzp6IHWdQ0u8S6I0n?usp=sharing)
- The License of the models is GPL-3.0 license: [License](https://github.com/meituan/YOLOv6/blob/main/LICENSE)

# Pytorch model
The original Pytorch model can be found in this repository: [YOLOv6 Repository](https://github.com/meituan/YOLOv6)
 
# Examples

 * **Image inference**:
 ```
 python image_object_detection.py
 ```
 
 * **Webcam inference**:
 ```
 python webcam_object_detection.py
 ```

 * **Video inference**: https://youtu.be/yYo0XQp97vo
 ```
 python video_object_detection.py
 ```
 ![!YOLOv6 detection video](https://github.com/ibaiGorordo/ONNX-YOLOv6-Object-Detection/blob/main/doc/img/yolov6s_video.gif)
  
 *Original video: https://youtu.be/yXEb0fWLJIY*

# References:
* YOLOv6 model: https://github.com/meituan/YOLOv6
* YOLOv5 model: https://github.com/ultralytics/yolov5
