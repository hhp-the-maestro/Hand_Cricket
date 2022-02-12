import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, mode=False, max_hands=1, model_complexity=1, detection_con=0.7, track_con=0.7):
        self.mode = mode
        self.maxHands = max_hands
        self.modelComplexity = model_complexity
        self.detectionCon = detection_con
        self.trackCon = track_con
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_hands(self, img, draw=True):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb_img)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, hand_no=0, draw=True):
        lm_list = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lm_list.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 150, 150), cv2.FILLED)
        return lm_list


