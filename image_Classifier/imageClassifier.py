
# TFLite for image classification model
#FULL PROCESSING
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

def processImage(frame):
    h, w, channels = frame.shape
    half = w//2
    left_part = frame[:, :half]
    right_part = frame[:, half:]
    return right_part,left_part

def imageClassification(frame):
    full_class_scores = []
    generalPath = "C:/Users/polgo/Desktop/VR keyboard project/image_Classifier/"
    model = tf.lite.Interpreter(model_path=generalPath+"model.tflite")
    classes = [  "0" ,  "1" ,  "2" ,  "3" ,  "4" ,  "5" ,  ]


    # Learn about its input and output details
    input_details = model.get_input_details()
    output_details = model.get_output_details()

    model.resize_tensor_input(input_details[0]['index'], (1, 224, 224, 3))
    model.allocate_tensors()


    right,left = processImage(frame)

    img = Image.fromarray(cv2.cvtColor(right, cv2.COLOR_BGR2RGB)).convert("RGB")
    img = img.resize((224, 224))
    img_np = np.array( img )[None].astype('float32')
    model.set_tensor(input_details[0]['index'], img_np)
    model.invoke()
    class_scores = model.get_tensor(output_details[0]['index'])
    
    full_class_scores.append(class_scores)

    img = Image.fromarray(cv2.cvtColor(left, cv2.COLOR_BGR2RGB)).convert("RGB")
    img = img.resize((224, 224))
    img_np = np.array( img )[None].astype('float32')
    model.set_tensor(input_details[0]['index'], img_np)
    model.invoke()
    class_scores = model.get_tensor(output_details[0]['index'])
    
    full_class_scores.append(class_scores)

    return full_class_scores[0],full_class_scores[1]




