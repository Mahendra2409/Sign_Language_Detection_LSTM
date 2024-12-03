import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt
# import time
# import mediapipe as mp

cap=cv2.VideoCapture(0)
while cap.isOpened():
    #Read feed
    ret, frame= cap.read()
    #Show to screeen
    cv2.imshow('Opencv Feed',frame)

    #Break gracefully
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()