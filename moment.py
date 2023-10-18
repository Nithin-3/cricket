import cv2
import mediapipe as mp
import numpy
import time
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
def ang(_1:list,_2:list,_3:list):
    _1,_2,_3 = numpy.array(_1), numpy.array(_2), numpy.array(_3) 
    radians = numpy.arctan2(_3[1]-_2[1], _3[0]-_2[0]) - numpy.arctan2(_1[1]-_2[1], _1[0]-_2[0])
    angle = numpy.abs(radians*180.0/numpy.pi)
    if angle >180.0:
        angle = 360-angle
    return angle 
def angtxt(image,_1,_2,_3):
    angle = int(ang(_1,_2,_3))
    cv2.putText(image, str(angle),tuple(numpy.multiply(_2, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    return angle
def i(img):
    try:
        results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        lanmak = results.pose_landmarks.landmark
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        a1 = angtxt(img,(lanmak[11].x,lanmak[11].y),(lanmak[13].x,lanmak[13].y),(lanmak[15].x,lanmak[15].y))            
        a2=angtxt(img,(lanmak[12].x,lanmak[12].y),(lanmak[14].x,lanmak[14].y),(lanmak[16].x,lanmak[16].y))            
        a3=angtxt(img,(lanmak[13].x,lanmak[13].y),(lanmak[11].x,lanmak[11].y),(lanmak[23].x,lanmak[23].y))            
        a4=angtxt(img,(lanmak[14].x,lanmak[14].y),(lanmak[12].x,lanmak[12].y),(lanmak[24].x,lanmak[24].y))
        a5 = angtxt(img,(lanmak[23].x,lanmak[23].y),(lanmak[25].x,lanmak[25].y),(lanmak[27].x,lanmak[27].y))
        return img
    except:
        return img   
previousTime = 0               
while cap.isOpened():
    _, frame = cap.read()
    try:
        currentTime = time.time()
        fps = 1 / (currentTime-previousTime)
        previousTime = currentTime
        frame = cv2.flip(frame,1)
        image = i(frame)
        cv2.putText(image, str(int(fps))+" FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Output', image)
    except:
        break
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
