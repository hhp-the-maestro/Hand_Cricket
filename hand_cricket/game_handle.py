from predict_gestures import PredictGestures
from show_menu import ShowMenu
import cv2
import time
import numpy as np

pg = PredictGestures
sm = ShowMenu


class GameHandle:
    def __init__(self):
        self.past_time = 0
        self.total_time = self.itime = 0
        self.scale = 0.465
        self.num_dict = {}
        self.vis_ = 2
        self.total = 0
        self.user_num = 0
        self.com_num = None
        self.inn = 1
        self.to_win = 0
        self.choice = "bat"
        self.toss_won = None
        self.player_list = []
        self.computer_list = []

    def toss(self, choice, img, lm_list):

        start = 2
        p_choice = choice

        if p_choice == "odd":
            com_choice = "even"
        else:
            com_choice = "odd"

        cv2.putText(img, f"Player: {p_choice}", (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (190, 25, 200), 2)
        cv2.putText(img, f"Computer: {com_choice}", (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (120, 25, 20), 2)

        if self.vis_ != 2:
            current_time = time.time()
            if self.scale == 0.5:
                self.itime = 1
            self.scale += 0.035
            if self.itime == 1:
                self.total_time += current_time - self.past_time
                if self.total_time > 1:
                    cv2.putText(img, "Wait", (200, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (15, 25, 220), 2)

                    if self.scale > 2:
                        self.itime = 2
            self.past_time = current_time

            if self.itime == 2:

                cv2.putText(img, "Play Now", (200, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (15, 25, 220), 2)

                img, num = PredictGestures.predict_1_to_6(img, lm_list)

                if num is not None:
                    self.num_dict[num] = self.num_dict.get(num, 0) + 1

                if sum(self.num_dict.values()) >= 7:
                    rev_dict = dict(zip(self.num_dict.values(), self.num_dict.keys()))
                    max_key = max(list(rev_dict.keys()))
                    self.user_num = rev_dict[max_key]
                    self.com_num = np.random.randint(0, 7)

                    # print(self.user_num, self.com_num)
                    # cv2.putText(img, str(self.com_num), (304, 291), cv2.FONT_HERSHEY_DUPLEX, 1, (15, 25, 220), 2)

                    toss_num = self.user_num + self.com_num

                    if toss_num % 2 == 0:
                        toss_result = "even"
                    else:
                        toss_result = "odd"

                    if toss_result == p_choice:
                        start = 3
                        self.vis_ = 2
                        self.user_num = 0
                        self.com_num = 0
                    else:
                        start = 4
                        self.vis_ = 2
                        self.user_num = 0
                        self.com_num = 0

                    self.past_time = self.total_time = 0
                    self.num_dict = {}

            return img, start

        else:
            if len(lm_list) == 0:
                self.vis_ = 1

            start = 2

            return img, start

    def game_seq(self, img, lm_list, p_choice, c_choice, toss_won, player_list, computer_list):
        self.toss_won = toss_won
        self.player_list = player_list
        self.computer_list = computer_list
        winner = None
        start = 5
        out = False

        img = sm.game_seq_display(img, p_choice=p_choice, c_choice=c_choice,
                                  player_list=self.player_list, computer_list=self.computer_list,
                                  toss_won=self.toss_won, total=self.total, to_win=self.to_win,
                                  com_num=self.com_num, inn=self.inn)

        if self.vis_ == 1 and len(lm_list) != 0:

            img, num = pg.predict_1_to_6(img, lm_list)

            if num is not None:
                self.num_dict[num] = self.num_dict.get(num, 0) + 1

            if sum(self.num_dict.values()) >= 4:
                rev_dict = dict(zip(self.num_dict.values(), self.num_dict.keys()))
                max_key = max(list(rev_dict.keys()))
                self.user_num = rev_dict[max_key]

                self.player_list.append(self.user_num)
                self.computer_list.append(self.com_num)

                self.toss_won = None

                self.num_dict = {}

                if self.user_num == self.com_num:
                    # change the field
                    p_choice, c_choice, start, out = self.game_change(p_choice, c_choice)
                    self.user_num = 0
                    self.com_num = 0

                if p_choice == 'bat':
                    self.total += self.user_num
                else:
                    self.total += self.com_num

                if self.inn >= 2:
                    if self.total > self.to_win:
                        start = 6
                        self.to_win = 0
                        if c_choice == 'bat':
                            winner = 'Computer'
                        else:
                            winner = 'Player'

                        self.user_num = 0
                        self.com_num = 0
                        self.total = 0
                        self.to_win = 0
                        self.inn = 1

                if self.inn > 2:
                    start = 6
                    if self.total < self.to_win:

                        if c_choice == "bowl":
                            winner = 'computer'
                        else:
                            winner = "Player"

                    if self.total == self.to_win:
                        winner = "Draw"

                    self.user_num = 0
                    self.com_num = 0
                    self.total = 0
                    self.to_win = 0
                    self.inn = 1

                self.vis_ = 2

            if sum(self.num_dict.values()) == 3:
                self.com_num = np.random.randint(0, 7)

        else:
            if len(lm_list) == 0:
                self.vis_ = 1
                self.total_time = self.past_time = 0

            elif self.vis_ == 2:
                current_time = time.time()
                if self.past_time != 0:
                    self.total_time += current_time - self.past_time

                self.past_time = current_time

                if self.total_time > 0.3:
                    self.total_time = 0
                    self.past_time = 0
                    self.vis_ = 3

            elif self.vis_ == 3:
                cv2.putText(img, "Wait", (250, 230), cv2.FONT_HERSHEY_DUPLEX, 3, (15, 125, 220), 2)
                self.total_time = self.past_time = 0

        return img, start, winner, p_choice, c_choice, self.toss_won, self.to_win, self.player_list, self.computer_list, out

    def game_change(self, p_choice, c_choice):
        start = 5
        out = False
        if self.inn < 2:
            if p_choice == "bat":
                p_choice = "bowl"
                c_choice = "bat"
            else:
                p_choice = "bat"
                c_choice = "bowl"
            self.to_win = self.total
            self.total = 0
            start = 6
            out = True

        self.inn += 1

        return p_choice, c_choice, start, out
