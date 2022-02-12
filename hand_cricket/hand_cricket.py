import cv2
import time
import hand_tracking as ht
from predict_gestures import PredictGestures
from game_handle import GameHandle
from show_menu import ShowMenu

""" cv2 config """
w_cam, h_cam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, w_cam)
cap.set(4, h_cam)

"""fps config"""
c_time = p_time = 0

"""game start config"""
start = 1
# choice = "bat"
win_ = "player"

"""Instantiating the classes"""
detector = ht.HandDetector()
pg = PredictGestures
sm = ShowMenu()
gh = GameHandle()


"""The Game Loop"""

while True:

    _, img = cap.read()
    img_shift = cv2.flip(img, 1)
    img = detector.find_hands(img, draw=False)
    lm_list = detector.find_position(img, draw=False)
    img = img_shift
    if start == 0:
        img, start = sm.start_menu(img=img, lm_list=lm_list)

    elif start == 1:
        img, start, choice = sm.odd_even_menu(img=img, lm_list=lm_list)

    elif start == 2:
        img, start = gh.toss(choice, img, lm_list=lm_list)

    elif start == 3:
        img, start, p_choice, c_choice = sm.player_wins_toss(img, lm_list=lm_list)
        toss_won = "player"

    elif start == 4:
        start, p_choice, c_choice = sm.computer_wins_toss()
        toss_won = "computer"

    elif start == 5:
        img, start, win_, p_choice, c_choice, toss_won = gh.game_seq(img, lm_list=lm_list, p_choice=p_choice,
                                                                     c_choice=c_choice, toss_won=toss_won)

    elif start == 6:
        img, start = sm.game_over(img, lm_list=lm_list, winner=win_)

    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time

    cv2.putText(img, str(int(fps)), (550, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
    img = cv2.resize(img, (800, 650))
    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break
