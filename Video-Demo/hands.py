import os
import sys
import cv2
import mediapipe as mp

class handDetector():
    def __init__(self, static_mode = False, max_hands = 2, detection_con = 0.6, track_con = 0.1):
        self.static_mode = static_mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con
        self.modelComplexity = 1

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=detection_con)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            return True
        else:
            return False

    def findPosition(self, img):
        lmlist = []
        myHand = self.results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmlist.append([cx, cy])
        return lmlist[4]

detector = handDetector()

def get_hand_vector_img(img):
    hand = 0
    is_hand_in_frame = detector.findHands(img)
    if is_hand_in_frame:
        # position = detector.findPosition(img)
        hand = 1
        # pos = position
    else:
        hand = 0
        # pos = -1
    # assert len(hand_vec) == len(img_list)
    return hand

def main(fpath, spath):
    hand_vec = []
    cap = cv2.VideoCapture(fpath)
    while True:
        ret, frame = cap.read()
        if ret:
            hand_vec.append(get_hand_vector_img(frame))
            print(len(hand_vec))
        else:
            break
    print(len(hand_vec))
    hand_vec = ''.join([str(i) for i in hand_vec])
    with open(spath +'.hands'+ '.txt', 'w+') as g:
        g.write(hand_vec)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])