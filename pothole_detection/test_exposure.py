from PIL import Image, ImageEnhance
import cv2
import numpy as np



vid = cv2.VideoCapture(3)

while True:
    _, img = vid.read()

    # Reduce the exposure by 50%
    exposure = ImageEnhance.Brightness(img)
    img = exposure.enhance(0.5)

    # Increase the contrast by 30%
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(1.3)

    # Adjust the white balance
    # img = ImgOps.autocontrast(img, cutoff=0)

    # Save the fixed image
    
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()
