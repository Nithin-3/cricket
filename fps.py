import cv2
import threading
import time
import mediapipe as mp
import numpy
import urllib
class FPS:
    url = 'http://192.168.137.39:8080/shot.jpg'

    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
        self.frame = None
        self.shows = None
        self.capt = None
        self.run = False
        self.strt = 0
        self.end = 0
        self.fps = 0
        self.start()
        threading.Thread(target=self.update,args=()).start()
        threading.Thread(target=self.show,args=()).start()
        
    def start(self,src=0):
        self.capt = cv2.VideoCapture(self.url)
        self.run = True
    def update(self):
        while self.run:
            # imgResp = urllib.urlopen(self.url)
            self.frame = numpy.array(bytearray(self.capt.read()), dtype=numpy.uint8)
            self.strt = time.time()
            self.i(self.frame)
    def i(self,img):
        try:
            img = cv2.flip(img,1)
            results = self.pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            lanmak = results.pose_landmarks.landmark
            self.mp_drawing.draw_landmarks(img, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

            angle = int(self.ang((lanmak[11].x,lanmak[11].y),(lanmak[13].x,lanmak[13].y),(lanmak[15].x,lanmak[15].y)))
            cv2.putText(img, "hhh"+str(angle),tuple(numpy.multiply((lanmak[13].x,lanmak[13].y), [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            
            angle1 = int(self.ang((lanmak[12].x,lanmak[12].y),(lanmak[14].x,lanmak[14].y),(lanmak[16].x,lanmak[16].y)))
            cv2.putText(img, str(angle1),tuple(numpy.multiply((lanmak[14].x,lanmak[14].y), [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            
            angle2 = int(self.ang((lanmak[13].x,lanmak[13].y),(lanmak[11].x,lanmak[11].y),(lanmak[23].x,lanmak[23].y)))
            cv2.putText(img, str(angle2),tuple(numpy.multiply((lanmak[11].x,lanmak[11].y), [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            
            angle3 = int(self.ang((lanmak[14].x,lanmak[14].y),(lanmak[12].x,lanmak[12].y),(lanmak[24].x,lanmak[24].y)))
            cv2.putText(img, str(angle3),tuple(numpy.multiply((lanmak[12].x,lanmak[12].y), [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            
            angle4 = int(self.ang((lanmak[23].x,lanmak[23].y),(lanmak[25].x,lanmak[25].y),(lanmak[27].x,lanmak[27].y)))
            cv2.putText(img, str(angle4),tuple(numpy.multiply((lanmak[25].x,lanmak[25].y), [640, 480]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    
            self.shows = img
        except Exception as e:
            print(f"ERROR => {e}")
            self.shows = img  
        finally:
            self.end = self.strt
    def ang(self,_1:list,_2:list,_3:list):
        _1,_2,_3 = numpy.array(_1), numpy.array(_2), numpy.array(_3) 
        radians = numpy.arctan2(_3[1]-_2[1], _3[0]-_2[0]) - numpy.arctan2(_1[1]-_2[1], _1[0]-_2[0])
        angle = numpy.abs(radians*180.0/numpy.pi)
        if angle >180.0:
            angle = 360-angle
        return angle 
    def show(self):
        while self.run:
            try:
                self.fps = 1 / (self.strt-self.end)
                cv2.putText(self.shows, str(int(self.fps))+" FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow("fps-test",self.shows)
                if cv2.waitKey(1) == ord('q'):
                    self.run = False
                    break
            except:
                pass
if __name__ == "__main__":
    FPS()