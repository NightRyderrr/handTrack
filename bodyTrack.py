import cv2
import mediapipe as mp
import time

mp
mpPose = mp.solutions.pose
pose = mpPose.Pose()


pTime = 0

while True:
   # success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RBG)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    ptime = cTime
    cv2.putText(img,str(int(fps)), (70 , 50 ),cv2.FONT_HERSHEY_PLAIN, 3,
               (255,0, 0),3)
    cap = cv2.VideoCapture(0)
    cv2.imshow("Image", img)
    cv2.waitKey(1)