import cv2
import mediapipe as mp
import random
import time

computer_choice_time = 0
gametime = time.time()


def ComputerChoice():
    # computer choice
    computer = ["rock", "paper", "scissors"]
    computerchoice = random.choice(computer)
    print("computers choice", computerchoice)
    return computerchoice


video_cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:

    ret, frame = video_cap.read()

    col = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(col)
    # This text instructs the user that pressing 'q' will exit the game, satisfying the requirement to ask if they want to play another round
    cv2.putText(frame, "to exit the game press 'q' else continue", (14, 461), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,255), 1)

    if results.multi_hand_landmarks:
        for hands_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hands_landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            index_pip = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
            middle_tip = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
            middle_pip = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
            ring_tip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
            ring_pip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
            pinky_tip = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
            pinky_pip = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

            userchoice = "undefined"
            if index_tip < index_pip and middle_tip < middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:  # scissors

                userchoice = "scissors"

            elif index_tip < index_pip and ring_tip < ring_pip and middle_tip < middle_pip and pinky_tip < pinky_pip:  # paper

                userchoice = "paper"

            elif index_tip > index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:  # rock

                userchoice = "rock"
            else:
                cv2.putText(frame, "un identified", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            current_time = time.time()
            if current_time - computer_choice_time >= 3:  # Wait 3 second before making a new computer choice
                computerchoice = ComputerChoice()
                computer_choice_time = current_time

            if computerchoice == userchoice:
                cv2.putText(frame, "draw", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            else:
                if userchoice == "rock":
                        if computerchoice == "scissors":
                            cv2.putText(frame, "user won", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                        elif computerchoice == "paper":
                            cv2.putText(frame, "computer  won", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        (255, 0, 0), 1)

                elif userchoice == "paper":
                        if computerchoice == "rock":
                            cv2.putText(frame, "user won ", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        (255, 0, 0), 1)
                        elif computerchoice == "scissors":
                            cv2.putText(frame, "computer  won", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        (255, 0, 0), 1)

                elif userchoice == "scissors":
                        if computerchoice == "paper":
                            cv2.putText(frame, "user won ", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        (255, 0, 0), 1)
                        elif computerchoice == "rock":
                            cv2.putText(frame, "computer  won ", (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1,
                                        (255, 0, 0), 1)

    cv2.imshow("live ", frame)
    #  check if 'q' is pressed to exit the game
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()

