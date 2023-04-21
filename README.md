# PotBot

# YOLOv5 instruction
YOLOv5 github is added to YoloPothole folder. 
Installation & Setup ref: https://docs.ultralytics.com/yolov5/train_custom_data/

or:
navigate to yolov5 folder, and run pip install -r requirements.txt 

## Ivy's personal note:
# Setup:
Please run in yolov5 folder
train command: python3 train.py --img 640 --epochs 3 --data coco128.yaml --weights yolov5s.pt
val command: python3 val.py --weights MODEL_FILE_PATH.pt --data SunglassedWebCam.yaml --img 640
test command: 

python3 detect.py --weights PATH --source --> 0 for webcam
other useful features: 
--conf_thres = 0.25 % confidence threshold
--save-text to save coordinate
--name "NAME" to specify document name
---> the detect code can run on video feed, so simply add the detect function should allow us to run images through the model. 

# how to get box coords
See line 165 - 167 in detect.py

# other
All test results and models are in ~/YoloPothole/yolove5/runs/

.yaml is in the data folder
