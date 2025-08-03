# YOLO docs
- use yolov11
https://docs.ultralytics.com/ the quickstart guide is really helpful just make a venv and install ultralytics
to view a webcam use --source 0
to train look in https://docs.ultralytics.com/modes/train/
to convert to a onix so that it can be converted to a hef

to train read the docs use
- I think that we will use roboflow to generate the training data
then we can export it in the yolov11 format

# convert to hef to run on the rasberry pi ai exelarator
https://github.com/hailo-ai/hailo_model_zoo -- used in the video below
https://github.com/LukeDitria/RasPi_YOLO -- the git that has useful scripts to get the data flow compiler to work
https://www.youtube.com/watch?v=Dm37x7sObIc -- a video guide that explains how to convert a yolov11 model to a hef
https://hailo.ai/developer-zone/documentation/hailo-sw-suite-2025-04/?sp_referrer=suite/suite_install.html -- the official documentation for the Hailo SW Suite

when you download the zip file from https://hailo.ai/developer-zone/software-downloads/
use the docker option
unzip it then then run the *.sh

#also you can run """hailo tutorial""" this will pull up some jupyter notebooks that will give you a better understanding to convert your model to a hef


I am following https://note.mmmsk.myds.me/Projects/Embedded-AI/files/hailo_dataflow_compiler_v3.27.0_user_guide.pdf page 54
1. hailo parser onnx --hw-arch hailo8 yolo11n-tenis-made-by-me.onnx
this is to make it in har format for the next step
2. convert your test imges to .nyp with this scrip chatGPT wrote for me 
"""import os
import cv2
import numpy as np

input_dir = 'test_img-1'
output_dir = 'test_img_npy'
os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(input_dir):
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, file_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (640, 640))  # adjust to your model input size
        img = img.astype(np.uint8)
        out_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.npy')
        np.save(out_path, img)

print("Conversion done.")"""

    
hailo optimize --hw-arch hailo8 --calib-set-path test_img/*  yolo11n-tenis-made-by-me.har

3. hailo compiler --hw-arch hailo8 yolo11n-tenis-made-by-me_optimized.har 



