import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt
# import time

import mediapipe as mp

mp_holistic = mp.solutions.holistic  #holistic
mp_drawing = mp.solutions.drawing_utils  #drawing utilites

def mediapipe_detection(image,model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #COLOR CONVERSION BGR TO RGB
    image.flags.writeable = False                   #Image is no loger writable
    results = model.process(image)                  #Make Prediction
    image.flags.writeable = True                    #Image is now writable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  #COLOR CONVERSION RGB TO BGR
    return image, results

def draw_landmark(image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)  #Draw face connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)  #Draw pose connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) #Draw left hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) #Draw right hand connections

# file_path=r"C:\Users\ms526\Downloads\3-indian-sign-language-101-basic-words-1-1080-publer.io.mp4"
# con_path= file_path.replace("\\","/")
cap=cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        #Read feed
        ret, frame= cap.read()

        #Make detection
        image, results = mediapipe_detection(frame, holistic)
        print(results)

        #Draw Lanmarks
        draw_landmark(image, results)

        #Show to screeen
        cv2.imshow('Opencv Feed',image)

        #Break gracefully
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()