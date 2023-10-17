import cv2
import mediapipe as mp
import numpy
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
def angtxt(_1,_2,_3):
    cv2.putText(frame, str(int(ang(_1,_2,_3))),tuple(numpy.multiply(_2, [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

while cap.isOpened():
    _, frame = cap.read()
    try:
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(RGB)
        try:
            lanmak = results.pose_landmarks.landmark
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            angtxt((lanmak[11].x,lanmak[11].y),(lanmak[13].x,lanmak[13].y),(lanmak[15].x,lanmak[15].y))            
            angtxt((lanmak[12].x,lanmak[12].y),(lanmak[14].x,lanmak[14].y),(lanmak[16].x,lanmak[16].y))            
            angtxt((lanmak[13].x,lanmak[13].y),(lanmak[11].x,lanmak[11].y),(lanmak[23].x,lanmak[23].y))            
            angtxt((lanmak[14].x,lanmak[14].y),(lanmak[12].x,lanmak[12].y),(lanmak[24].x,lanmak[24].y))
        except Exception as e:
            pass
        cv2.imshow('Output', frame)
    except:
        break
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
