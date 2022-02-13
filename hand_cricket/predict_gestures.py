import cv2


class PredictGestures:

    @staticmethod
    def predict_1_to_6(img, lm_list):

        num = None
        if len(lm_list) != 0:

            if lm_list[8][2] < lm_list[5][2] < lm_list[12][2] \
                    and lm_list[5][2] < lm_list[16][2] and lm_list[5][2] < lm_list[20][2] \
                    and lm_list[5][2] < lm_list[4][2]:

                cv2.putText(img, "One", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 1
                print("one")

            elif lm_list[8][2] < lm_list[5][2] < lm_list[4][2] and lm_list[12][2] < lm_list[9][2] \
                    < lm_list[16][2]:

                cv2.putText(img, "Two", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 2
                print("Two")

            elif lm_list[8][2] < lm_list[5][2] < lm_list[4][2] and lm_list[12][2] < lm_list[9][2] \
                    < lm_list[20][2] and lm_list[16][2] < lm_list[13][2]:

                cv2.putText(img, "Three", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 3
                print("Three")

            elif lm_list[20][2] < lm_list[17][2] and lm_list[16][2] < lm_list[13][2] \
                    and lm_list[12][2] < lm_list[9][2] < lm_list[8][2] \
                    and lm_list[9][2] < lm_list[4][2]:

                cv2.putText(img, "Three", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 3
                print("Three")

            elif lm_list[8][2] < lm_list[5][2] and lm_list[12][2] < lm_list[9][2] < lm_list[4][2]\
                    and lm_list[16][2] < lm_list[13][2] and lm_list[20][2] < lm_list[17][2] \
                    and lm_list[4][1] < lm_list[5][1]:

                cv2.putText(img, "Four", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 4
                print("Four")

            elif lm_list[8][2] < lm_list[5][2] and lm_list[12][2] < lm_list[9][2] and\
                    lm_list[16][2] < lm_list[13][2] and lm_list[20][2] < lm_list[17][2] \
                    and lm_list[4][1] > lm_list[5][1]:

                cv2.putText(img, "Five", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 5
                print("Five")

            elif lm_list[4][2] < lm_list[5][2] and lm_list[4][2] < lm_list[3][2]:

                cv2.putText(img, "Six", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 6
                print("Six")

            elif (lm_list[5][2] < lm_list[6][2] and lm_list[9][2] < lm_list[10][2] and
                  lm_list[13][2] < lm_list[14][2] and lm_list[17][2] < lm_list[18][2]) or\
                 (lm_list[5][2] < lm_list[9][2] < lm_list[13][2]):

                cv2.putText(img, "Zero", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = 0
                print("Zero")

            else:

                cv2.putText(img, "Unknown", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
                num = None
                print("Unknown")

        return img, num

    @staticmethod
    def cap_start_gesture(lm_list):

        if len(lm_list) != 0:

            if (105 <= lm_list[8][2] <= 170 and 105 <= lm_list[12][2] <= 170) and \
                    (180 <= lm_list[8][1] <= 480 and 180 <= lm_list[12][1] <= 480):

                return True, False

            elif (220 <= lm_list[8][2] <= 285 and 220 <= lm_list[12][2] <= 285) and \
                    (180 <= lm_list[8][1] <= 480 and 180 <= lm_list[12][1] <= 480):

                return False, True

        return False, False

    @staticmethod
    def odd_even_gesture(lm_list):

        if len(lm_list) != 0:

            if (110 <= lm_list[8][2] <= 160 and 110 <= lm_list[12][2] <= 160) and \
                    (210 <= lm_list[8][1] <= 400 and 210 <= lm_list[12][1] <= 400):

                return True, False, False

            elif (190 <= lm_list[8][2] <= 240 and 190 <= lm_list[12][2] <= 240) and \
                    (210 <= lm_list[8][1] <= 400 and 210 <= lm_list[12][1] <= 400):

                return False, True, False

            elif (270 <= lm_list[8][2] <= 320 and 270 <= lm_list[12][2] <= 320) and \
                    (210 <= lm_list[8][1] <= 400 and 210 <= lm_list[12][1] <= 400):

                return False, False, True

        return False, False, False

    @staticmethod
    def bat_or_bowl_gesture(lm_list):

        if len(lm_list) != 0:

            if (160 <= lm_list[8][2] <= 210 and 160 <= lm_list[12][2] <= 210) and \
                    (230 <= lm_list[8][1] <= 400 and 230 <= lm_list[12][1] <= 400):

                return True, False

            elif (240 <= lm_list[8][2] <= 290 and 240 <= lm_list[12][2] <= 290) and \
                    (230 <= lm_list[8][1] <= 400 and 230 <= lm_list[12][1] <= 400):

                return False, True

        return False, False

    @staticmethod
    def continue_gesture(lm_list):

        if len(lm_list) != 0:

            if (250 <= lm_list[8][2] <= 300 and 250 <= lm_list[12][2] <= 300) and \
                    (230 <= lm_list[8][1] <= 400 and 230 <= lm_list[12][1] <= 400):

                return True

        return False






