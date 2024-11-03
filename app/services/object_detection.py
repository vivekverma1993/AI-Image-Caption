import cv2
import torch

def detect_objects(image_path):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    image = cv2.imread(image_path)
    results = model(image)
    detected_objects = results.pandas().xyxy[0].to_dict(orient='records')
    return detected_objects
