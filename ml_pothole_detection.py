import cv2
import YoloPothole.yolov5.detect as det
MODEL_PATH = 'YoloPothole\potholeYolo5s.pt'
#MODEL_PATH = "YoloPothole\ivy.pt"
CONF_THRE = 0.35
det.run(weights = MODEL_PATH, source = 2, conf_thres=CONF_THRE, view_img=True, save_txt=True)
