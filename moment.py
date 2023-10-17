import cv2
import mediapipe as mp
import numpy
from time import sleep
import fnd
import csv
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
cap = cv2.VideoCapture("VID-20231017-WA0004.mp4")
shot = ''

def ang(_1:list,_2:list,_3:list):
    _1,_2,_3 = numpy.array(_1), numpy.array(_2), numpy.array(_3) 
    radians = numpy.arctan2(_3[1]-_2[1], _3[0]-_2[0]) - numpy.arctan2(_1[1]-_2[1], _1[0]-_2[0])
    angle = numpy.abs(radians*180.0/numpy.pi)
    if angle >180.0:
        angle = 360-angle
    return angle 
def angtxt(_1,_2,_3):
    angle = int(ang(_1,_2,_3))
    cv2.putText(img, str(angle),tuple(numpy.multiply(_2, [1280, 720]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    return angle
img = cv2.imread("WhatsApp Image 2023-10-17 at 15.13.44.jpeg")
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = pose.process(RGB)

lanmak = results.pose_landmarks.landmark
mp_drawing.draw_landmarks(
    img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
a1 = angtxt((lanmak[11].x,lanmak[11].y),(lanmak[13].x,lanmak[13].y),(lanmak[15].x,lanmak[15].y))            
a2=angtxt((lanmak[12].x,lanmak[12].y),(lanmak[14].x,lanmak[14].y),(lanmak[16].x,lanmak[16].y))            
a3=angtxt((lanmak[13].x,lanmak[13].y),(lanmak[11].x,lanmak[11].y),(lanmak[23].x,lanmak[23].y))            
a4=angtxt((lanmak[14].x,lanmak[14].y),(lanmak[12].x,lanmak[12].y),(lanmak[24].x,lanmak[24].y))
a5 = angtxt((lanmak[23].x,lanmak[23].y),(lanmak[25].x,lanmak[25].y),(lanmak[27].x,lanmak[27].y))
print(fnd.fnd(a4,a3,a2,a1,None))
cv2.imshow("ang",img)
cv2.waitKey(0)                  
# while cap.isOpened():
#     _, frame = cap.read()
#     try:
#         RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = pose.process(RGB)
#         try:
#             lanmak = results.pose_landmarks.landmark
#             mp_drawing.draw_landmarks(
#                 frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#             a1 = angtxt((lanmak[11].x,lanmak[11].y),(lanmak[13].x,lanmak[13].y),(lanmak[15].x,lanmak[15].y))            
#             a2=angtxt((lanmak[12].x,lanmak[12].y),(lanmak[14].x,lanmak[14].y),(lanmak[16].x,lanmak[16].y))            
#             a3=angtxt((lanmak[13].x,lanmak[13].y),(lanmak[11].x,lanmak[11].y),(lanmak[23].x,lanmak[23].y))            
#             a4=angtxt((lanmak[14].x,lanmak[14].y),(lanmak[12].x,lanmak[12].y),(lanmak[24].x,lanmak[24].y))
#             a5 = angtxt((lanmak[23].x,lanmak[23].y),(lanmak[25].x,lanmak[25].y),(lanmak[27].x,lanmak[27].y))
#             print(fnd.fnd(a4,a3,a2,a1,None))
#         except Exception as e:
#             pass
#         cv2.imshow('Output', frame)
#     except:
#         break
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
