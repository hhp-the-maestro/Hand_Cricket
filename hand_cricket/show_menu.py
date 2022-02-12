import cv2
import time
import random
from predict_gestures import PredictGestures

pg = PredictGestures


def menu_helper(colour, reset_colour, itime, total_time, past_time, start, new_start):
    colour = (colour[0] - 5, colour[1] + 8, colour[2] + 10)
    current_time = time.time()
    start = start
    if itime == 1:
        total_time += current_time - past_time
        if total_time > 1:
            start = new_start
            colour = reset_colour
            total_time = 0

    itime = 1
    past_time = current_time
    return colour, itime, total_time, past_time, start


class ShowMenu:
    def __init__(self):
        self.start_color = (170, 15, 155)
        self.quit_color = (170, 15, 155)
        self.odd_color = (100, 150, 155)
        self.even_color = (170, 155, 15)
        self.bat_color = (255, 5, 25)
        self.bowl_color = (255, 5, 25)
        self.cont_color = (50, 255, 25)
        self.start_pos = (180, 105), (480, 170)
        self.quit_pos = (180, 220), (480, 285)
        self.odd_pos = (210, 110), (400, 160)
        self.even_pos = (210, 190), (400, 240)
        self.back_pos = (210, 270), (400, 320)
        self.total_time = self.itime = self.past_time = 0

    def start_menu(self, img, lm_list):

        cv2.putText(img, "Hand Cricket", (135, 80), cv2.FONT_HERSHEY_DUPLEX, 2, (250, 215, 200), 3)

        cv2.rectangle(img, self.start_pos[0], self.start_pos[1], self.start_color, -1)
        cv2.putText(img, "Start Game", (190, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (50, 215, 100), 3)

        cv2.rectangle(img, self.quit_pos[0], self.quit_pos[1], self.quit_color, -1)
        cv2.putText(img, "Quit Game", (200, 260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (25, 105, 210), 3)

        is_start, is_quit = pg.cap_start_gesture(lm_list=lm_list)

        if is_start:
            start = 0

            self.start_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.start_color,
                                                                                               (170, 15, 155),
                                                                                               self.itime,
                                                                                               self.total_time,
                                                                                               self.past_time, start, 1)

        elif is_quit:
            self.quit_color = (self.quit_color[0] - 7, self.quit_color[1], self.quit_color[2])
            current_time = time.time()
            start = 0
            if self.itime == 1:
                self.total_time += current_time - self.past_time
                if self.total_time > 1:
                    quit()

            self.itime = 1
            self.past_time = current_time

        else:
            self.start_color = self.quit_color = (170, 15, 155)
            self.itime = 0
            self.total_time = 0
            self.past_time = 0
            start = 0

        if start == 1:
            self.itime = 0
            self.past_time = 0

        return img, start

    def odd_even_menu(self, img, lm_list):

        cv2.putText(img, "odd or even", (135, 80), cv2.FONT_HERSHEY_DUPLEX, 2, (250, 215, 200), 3)

        cv2.rectangle(img, self.odd_pos[0], self.odd_pos[1], self.odd_color, -1)
        cv2.putText(img, "Odd", (250, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (200, 255, 200), 3)

        cv2.rectangle(img, self.even_pos[0], self.even_pos[1], self.even_color, -1)
        cv2.putText(img, "Even", (250, 225), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (110, 115, 200), 3)

        cv2.rectangle(img, self.back_pos[0], self.back_pos[1], self.start_color, -1)
        cv2.putText(img, "Back", (250, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (250, 215, 200), 3)

        is_odd, is_even, is_back = pg.odd_even_gesture(lm_list)

        if is_odd:
            start = 1

            self.odd_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.odd_color,
                                                                                             (100, 150, 155),
                                                                                             self.itime,
                                                                                             self.total_time,
                                                                                             self.past_time, start, 2)
            choice = "odd"

        elif is_even:
            start = 1

            self.even_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.even_color,
                                                                                              (170, 155, 15),
                                                                                              self.itime,
                                                                                              self.total_time,
                                                                                              self.past_time, start, 2)
            choice = "even"

        elif is_back:
            start = 1

            self.start_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.start_color,
                                                                                               (170, 15, 155),
                                                                                               self.itime,
                                                                                               self.total_time,
                                                                                               self.past_time, start, 0)

            choice = None

        else:
            self.start_color = (170, 15, 155)
            self.odd_color = (100, 150, 155)
            self.even_color = (170, 155, 15)
            self.itime = 0
            self.total_time = 0
            start = 1
            choice = None

        if start == 2:
            self.itime = 0
            self.past_time = 0
            self.total_time = 0

        return img, start, choice

    def player_wins_toss(self, img, lm_list):

        start = 3
        cv2.rectangle(img, (170, 50), (480, 130), (255, 255, 255), -1)
        cv2.putText(img, "You Won The Toss", (180, 80), cv2.FONT_ITALIC, 1, (15, 150, 200), 4)
        cv2.putText(img, "Choose to", (220, 120), cv2.FONT_ITALIC, 1, (15, 150, 200), 4)

        cv2.rectangle(img, (230, 160), (400, 210), self.bat_color, -1)
        cv2.putText(img, "Batting", (260, 190), cv2.FONT_ITALIC, 1, (255, 250, 200), 3)

        cv2.rectangle(img, (230, 240), (400, 290), self.bowl_color, -1)
        cv2.putText(img, "Bowling", (260, 270), cv2.FONT_ITALIC, 1, (255, 250, 200), 3)

        is_batting, is_bowling = pg.bat_or_bowl_gesture(lm_list=lm_list)

        if is_batting:

            self.bat_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.bat_color,
                                                                                             (255, 5, 25),
                                                                                             self.itime,
                                                                                             self.total_time,
                                                                                             self.past_time, start, 5)

        elif is_bowling:

            self.bowl_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.bowl_color,
                                                                                              (255, 5, 25),
                                                                                              self.itime,
                                                                                              self.total_time,
                                                                                              self.past_time, start, 5)
        else:
            self.itime = 0
            self.total_time = 0
            self.bat_color = (255, 5, 25)
            self.bowl_color = (255, 5, 25)

        if is_batting:
            p_choice = "bat"
            c_choice = "bowl"
        elif is_bowling:
            p_choice = "bowl"
            c_choice = "bat"
        else:
            p_choice = None
            c_choice = None

        return img, start, p_choice, c_choice

    @staticmethod
    def computer_wins_toss():
        start = 4
        choices = ["bat", "bowl"]
        com_choice = random.choice(choices)

        if com_choice == "bat":
            c_choice = "bowl"
            p_choice = "bat"
            start = 5
        else:
            c_choice = "bat"
            p_choice = "bowl"
            start = 5
        return start, p_choice, c_choice

    def game_over(self, img, lm_list, winner):
        start = 6
        if winner == "Draw":
            cv2.rectangle(img, (210, 50), (450, 100), (225, 250, 225), -1)
            cv2.putText(img, "Match Draw", (230, 80), cv2.FONT_ITALIC, 1, (15, 250, 200), 3)
        else:
            cv2.rectangle(img, (210, 50), (450, 100), (225, 250, 225), -1)
            cv2.putText(img, str(winner) + ' Wins', (230, 80), cv2.FONT_ITALIC, 1, (15, 250, 200), 3)

        cv2.rectangle(img, (230, 200), (400, 250), self.cont_color, -1)
        cv2.putText(img, "Continue", (245, 230), cv2.FONT_ITALIC, 1, (115, 20, 20), 3)

        is_cont = pg.continue_gesture(lm_list=lm_list)

        if is_cont:
            self.cont_color, self.itime, self.total_time, self.past_time, start = menu_helper(self.cont_color,
                                                                                              (50, 255, 25),
                                                                                              self.itime,
                                                                                              self.total_time,
                                                                                              self.past_time, start, 0)
        else:
            self.itime = 0
            self.total_time = 0
            self.cont_color = (50, 255, 25)

        return img, start

    @staticmethod
    def game_seq_display(img, p_choice, c_choice, inn, com_num, total, toss_won, to_win=None):
        if toss_won is not None:
            if toss_won == "player":
                cv2.putText(img, f"Player won the toss and choose to {p_choice}", (100, 20), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (15, 17, 185), 1)
            else:
                cv2.putText(img, f"Computer won the toss and choose to {c_choice}", (100, 20), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (15, 17, 180), 1)

            cv2.putText(img, f"{p_choice}", (300, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (15, 25, 220), 2)
        else:
            cv2.putText(img, f"{p_choice}", (300, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (15, 25, 220), 2)
        # cv2.rectangle(img, (150, 65), (190, 100), (216, 213, 224), -1)
        # cv2.rectangle(img, (200, 60), (250, 105), (216, 213, 224), -1)
        # cv2.rectangle(img, (260, 55), (320, 110), (216, 213, 224), -1)
        # cv2.rectangle(img, (330, 50), (400, 115), (216, 213, 224), -1)
        cv2.putText(img, f"{c_choice}", (300, 460), cv2.FONT_HERSHEY_DUPLEX, 1, (15, 25, 220), 2)

        cv2.rectangle(img, (480, 200), (560, 240), (127, 135, 148), -1)
        cv2.rectangle(img, (560, 200), (650, 240), (255, 255, 255), -1)
        cv2.putText(img, "Total", (480, 230), cv2.FONT_HERSHEY_DUPLEX, 1, (215, 255, 120), 2)
        cv2.putText(img, str(total), (565, 230), cv2.FONT_ITALIC, 1, (0, 25, 10), 1)

        if inn == 2:
            cv2.rectangle(img, (480, 240), (560, 280), (127, 135, 148), -1)
            cv2.rectangle(img, (560, 240), (650, 280), (255, 255, 255), -1)
            cv2.putText(img, "To Win", (480, 270), cv2.FONT_HERSHEY_DUPLEX, 0.75, (215, 255, 120), 2)
            cv2.putText(img, str(to_win), (565, 270), cv2.FONT_ITALIC, 0.75, (0, 25, 10), 1)

        if com_num:
            cv2.putText(img, str(com_num), (304, 291), cv2.FONT_HERSHEY_DUPLEX, 2, (15, 225, 220), 2)

        return img
