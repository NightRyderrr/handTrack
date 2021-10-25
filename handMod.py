import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList
def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(1)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__ == "__main__":
    main()
    
    """ error message i keep getting
    
    
   ceback (most recent call last):
  File "C:\Users\carkp\PycharmProjects\pythonProject\handMod.py", line 55, in <module>
    main()
  File "C:\Users\carkp\PycharmProjects\pythonProject\handMod.py", line 40, in main
    detector = handDetector()
  File "C:\Users\carkp\PycharmProjects\pythonProject\handMod.py", line 11, in __init__
    self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCon)
  File "C:\Users\carkp\PycharmProjects\pythonProject\venv\lib\site-packages\mediapipe\python\solutions\hands.py", line 114, in __init__
    super().__init__(
  File "C:\Users\carkp\PycharmProjects\pythonProject\venv\lib\site-packages\mediapipe\python\solution_base.py", line 258, in __init__
    self._input_side_packets = {
  File "C:\Users\carkp\PycharmProjects\pythonProject\venv\lib\site-packages\mediapipe\python\solution_base.py", line 259, in <dictcomp>
    name: self._make_packet(self._side_input_type_info[name], data)
  File "C:\Users\carkp\PycharmProjects\pythonProject\venv\lib\site-packages\mediapipe\python\solution_base.py", line 513, in _make_packet
    return getattr(packet_creator, 'create_' + packet_data_type.value)(data)
TypeError: create_int(): incompatible function arguments. The following argument types are supported:
    1. (arg0: int) -> mediapipe.python._framework_bindings.packet.Packet

Invoked with: 0.5


"""
    
