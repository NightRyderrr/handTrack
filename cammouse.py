import cv2
import mediapipe as mp
import time
import handMod as htm
from handMod import  main
import pyautogui
import keyboard as kb

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(False, 1)
print(pyautogui.size())
nativex, nativey = pyautogui.size()
camx = 480
camy = 640






while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    #print(lmList, len(lmList))
    #if len(lmList) != 0:
    print(main().x1, main().y1)
       # coordx, coordy = int(camx
      #  print(coordx, coordy)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
  #  cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
               # (255, 0, 255), 3)
    cv2.imshow("Img", cv2.flip(img, 1))
    cv2.waitKey(1)



