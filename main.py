from pyfirmata import ArduinoMega, util
import time
import keyboard
# CV related libraries
import cv2
import argparse
import os
import platform
import sys
from pathlib import Path

import torch

MODEL_PATH = 'YoloPothole\potholeYolo5s.pt'
#MODEL_PATH = "YoloPothole\ivy.pt"
CONF_THRE = 0.35

# YOLOv5 🚀 by Ultralytics, AGPL-3.0 license


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from YoloPothole.yolov5.models.common import DetectMultiBackend
from YoloPothole.yolov5.utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from YoloPothole.yolov5.utils.general import (LOGGER, Profile, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from YoloPothole.yolov5.utils.plots import Annotator, colors, save_one_box
from YoloPothole.yolov5.utils.torch_utils import select_device, smart_inference_mode

# Monkey patch to fix python 3.11 bug
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

board = ArduinoMega('COM5')

# CV Models Initialization
weights=ROOT / 'yolov5s.pt',  # model path or triton URL
source=ROOT / 'data/images',  # file/dir/URL/glob/screen/0(webcam)
data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
imgsz=(640, 640),  # inference size (height, width)
conf_thres=0.25,  # confidence threshold
iou_thres=0.45,  # NMS IOU threshold
max_det=1000,  # maximum detections per image
device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
view_img=False,  # show results
classes=None,  # filter by class: --class 0, or --class 0 2 3
agnostic_nms=False,  # class-agnostic NMS
augment=False,  # augmented inference
visualize=False,  # visualize features
project=ROOT / 'runs/detect',  # save results to project/name
name='exp',  # save results to project/name
exist_ok=False,  # existing project/name ok, do not increment
line_thickness=3,  # bounding box thickness (pixels)
hide_labels=False,  # hide labels
hide_conf=False,  # hide confidences
half=False,  # use FP16 half-precision inference
dnn=False,  # use OpenCV DNN for ONNX inference
vid_stride=1,  # video frame-rate stride

# Wheels
L_LEN = board.get_pin('d:50:o')
L_REN = board.get_pin('d:49:o')
L_RPWM = board.get_pin('d:9:p')
L_LPWM = board.get_pin('d:3:p')
R_RPWM = board.get_pin('d:10:p')
R_LPWM = board.get_pin('d:5:p')

# Auger
A_RENABLE = board.get_pin('d:48:o')
A_LENABLE = board.get_pin('d:47:o')
A_RPWM = board.get_pin('d:11:p')
A_LPWM = board.get_pin('d:6:p')

# Pump
PUMP = board.get_pin('d:46:o')

# Motor Initialization
L_LEN.write(1)
L_REN.write(1)
A_RENABLE.write(1)
A_LENABLE.write(1)
PUMP.write(0)

"""
print('forward')
L_LPWM.write(0.5)
L_RPWM.write(0)
R_LPWM.write(0.5)
R_RPWM.write(0)

print('backward')
L_LPWM.write(0)
L_RPWM.write(0.5)
R_LPWM.write(0)
R_RPWM.write(0.5)

print('left')
L_LPWM.write(0.5)
L_RPWM.write(0)
R_LPWM.write(0)
R_RPWM.write(0.5)

print('right')
L_LPWM.write(0)
L_RPWM.write(0.5)
R_LPWM.write(0.5)
R_RPWM.write(0)

print('auger turning')
A_LPWM.write(0)
A_RPWM.write(0.5)

print("pump")
PUMP.write(1)
"""

sleepTime = 0.1
thresh_low = 0
thresh_high = 0

NavigationFlag = 1
FillingFlag = 0
FlatteningFlag = 0
MoveAwayFlag = 0
OperationFinished = 0

FillingTime = 4
FlatteningTime = 5
MoveAwayTime = 5

source = str(source)

# Directories
save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
# Load model
device = select_device(device)
model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)
stride, names, pt = model.stride, model.names, model.pt
imgsz = check_img_size(imgsz, s=stride)  # check image size

# Dataloader
bs = 1  # batch_size
view_img = check_imshow(warn=True)
dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
bs = len(dataset)

# Run inference
model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
for path, im, im0s, vid_cap, s in dataset:
    with dt[0]:
        im = torch.from_numpy(im).to(model.device)
        im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

        # Inference
    with dt[1]:
        visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
        pred = model(im, augment=augment, visualize=visualize)

        # NMS
    with dt[2]:
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

        # Process predictions
    for i, det in enumerate(pred):  # per image
        seen += 1
        p, im0, frame = path[i], im0s[i].copy(), dataset.count
        s += f'{i}: '

        p = Path(p)  # to Path
        s += '%gx%g ' % im.shape[2:]  # print string
        gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            
        annotator = Annotator(im0, line_width=line_thickness, example=str(names))
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()
            # find pothole box center
            for *xyxy, conf, cls in reversed(det):
                xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                x = (xyxy[2]-xyxy[0])//2
                y = (xyxy[3]-xyxy[1])//2
                print("Found %i Potholes in %i ms"%(len(det), dt[1].dt * 1E3))
                print("x = %f, y = %f, w = %f, h = %f"%(xywh[0],xywh[1],xywh[2],xywh[3]))
                print("xPixel = %i, yPixel = %i"%(x, y))

                c = int(cls)  # integer class
                label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                annotator.box_label(xyxy, label, color=colors(c, True))
            #TODO: Integrate Control Code when Pothole is detected. x, y only appears in this loop
        else: 
            #TODO: Integrate Control Code when Pothole is not detected

        # Stream results
        im0 = annotator.result()

        cv2.imshow(str(p), im0)
        cv2.waitKey(1)  # 1 millisecond

while True:
    L_LPWM.write(0)
    L_RPWM.write(0)
    R_LPWM.write(0)
    R_RPWM.write(0)

    A_RPWM.write(0)
    A_LPWM.write(0)
    
    PUMP.write(0)

    if NavigationFlag == 1:
    # Place holder: CV output x, y
    
        if (x > thresh_low and x < thresh_high):
            # Go forward
            L_LPWM.write(0.5)
            L_RPWM.write(0)
            R_LPWM.write(0.5)
            R_RPWM.write(0)
        
        if (x < thresh_low):
            # Trun left
            L_LPWM.write(0.5)
            L_RPWM.write(0)
            R_LPWM.write(0)
            R_RPWM.write(0.5)
        
        if (x > thresh_low):
            # Turn right
            L_LPWM.write(0)
            L_RPWM.write(0.5)
            R_LPWM.write(0.5)
            R_RPWM.write(0)
            
        if ():
            NavigationFlag = 0
            FillingFlag = 1
        
        continue
    
    if FillingFlag == 1:
        A_LPWM.write(0)
        A_RPWM.write(0.5)
        FillingFlag = 0
        time.sleep(5)
    
    if FlatteningFlag == 1:
        PUMP.write(1)
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        FlatteingFlag = 2
        time.sleep(FlatteningTime)
    
    if FlatteningFlag == 2:
        PUMP.write(1)
        L_LPWM.write(0)
        L_RPWM.write(0.5)
        R_LPWM.write(0)
        R_RPWM.write(0.5)
        FlatteningFlag = 0
        MoveAwayFlag = 1
        time.sleep(FlatteningTime)
    
    if MoveAwayFlag == 1:
        L_LPWM.write(0.5)
        L_RPWM.write(0)
        R_LPWM.write(0.5)
        R_RPWM.write(0)
        OperationFinished = 1
        MoveAwayFlag = 0
        time.sleep(MoveAwayTime)
    
    if OperationFinished == 1:
        break
    
    
