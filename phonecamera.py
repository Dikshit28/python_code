import cv2
import numpy as np
url = "http://192.168.1.41:8080/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    
    val='A'
    loc=f'./dataset/{val}.png'
    cv2.imwrite(loc,frame)
    if q==ord("q"):
        break
cv2.destroyAllWindows()