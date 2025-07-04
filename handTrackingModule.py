import cv2
import mediapipe as mp
import time


class handDetector:
    def __init__(self,mode=False,maxhands=2,detectionConfidence=0.5,trackConfidence=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxhands,
            min_detection_confidence=self.detectionConfidence,
            min_tracking_confidence=self.trackConfidence
        )

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


    def findPosition(self,img,handNo=0,draw=True):
        lmLlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                    #print(id,lm)
                h, w, c = img.shape

                cx,cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                lmLlist.append([id,cx,cy])
                #if id == 0: #first point
                if draw:
                    cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)

        return lmLlist

def main():
    prevTime = 0
    currTime = 0
    cap = cv2.VideoCapture(0)

    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        currTime = time.time()
        fps = 1/(currTime-prevTime)
        prevTime = currTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()