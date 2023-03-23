import cv2
import subprocess

subprocess.Popen("python ./assets/yolov5/detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source 0 --classes 0")
