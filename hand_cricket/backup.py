if len(lm_list) != 0:

    if lm_list[8][2] < lm_list[5][2] and lm_list[5][2] < lm_list[12][2] \
            and lm_list[5][2] < lm_list[16][2] and lm_list[5][2] < lm_list[20][2] \
            and lm_list[5][2] < lm_list[4][2]:

        cv2.putText(img, "One", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("one")

    elif lm_list[8][2] < lm_list[5][2] and lm_list[12][2] < lm_list[9][2] \
            and lm_list[9][2] < lm_list[16][2] and lm_list[5][2] < lm_list[4][2]:

        cv2.putText(img, "Two", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Two")

    elif lm_list[8][2] < lm_list[5][2] and lm_list[12][2] < lm_list[9][2] \
            and lm_list[16][2] < lm_list[13][2] and lm_list[9][2] < lm_list[20][2] \
            and lm_list[5][2] < lm_list[4][2]:

        cv2.putText(img, "Three", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Three")

    elif lm_list[20][2] < lm_list[17][2] and lm_list[16][2] < lm_list[13][2] \
            and lm_list[12][2] < lm_list[9][2] and lm_list[9][2] < lm_list[8][2] \
            and lm_list[9][2] < lm_list[4][2]:

        cv2.putText(img, "Three", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Three")

    elif lm_list[8][2] < lm_list[5][2] and lm_list[12][2] < lm_list[9][2] \
            and lm_list[16][2] < lm_list[13][2] and lm_list[20][2] < lm_list[17][2] \
            and lm_list[9][2] < lm_list[4][2] and lm_list[4][1] < lm_list[5][1]:

        cv2.putText(img, "Four", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Four")

    elif lm_list[8][2] < lm_list[5][2] and lm_list[12][2] < lm_list[9][2] \
            and lm_list[16][2] < lm_list[13][2] and lm_list[20][2] < lm_list[17][2] \
            and lm_list[4][1] > lm_list[5][1]:

        cv2.putText(img, "Five", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Five")

    elif lm_list[3][2] < lm_list[5][2]:

        cv2.putText(img, "Six", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Six")

    else:

        cv2.putText(img, "Unknown", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 100, 100), 3)
        print("Unknown")