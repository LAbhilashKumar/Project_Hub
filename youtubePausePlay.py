# import time
# import cv2
# import mediapipe as mp
# import pyautogui as py
# import threading
# scissors_event = threading.Event()
# # global scissors
# #
# scissors = False
#
#
# def play_pause():
#     global scissors
#     # scissors= False
#     cap = cv2.VideoCapture(0)
#
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands(static_image_mode=False,
#                            max_num_hands=1, min_tracking_confidence=0.5,
#                            min_detection_confidence=0.5)
#
#     mp_drawings = mp.solutions.drawing_utils
#
#     while True:
#         # scissors=False
#         print("play paue thread", scissors)
#         ret, frame = cap.read()
#         image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = hands.process(image_rgb)
#         if results.multi_hand_landmarks:
#             for hands_landmarks in results.multi_hand_landmarks:
#                 mp_drawings.draw_landmarks(frame, hands_landmarks, mp_hands.HAND_CONNECTIONS)
#
#                 # for pip
#                 index_pip = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
#                 middle_pip = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
#                 ring_pip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
#                 pinky_pip = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
#                 thumb_ip = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
#
#                 # thumb mcp
#                 thumb_mcp = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
#
#                 # for tip
#                 index_tip = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
#                 middle_tip = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
#                 ring_tip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
#                 pinky_tip = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
#                 thumb_tip = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
#                 if index_tip < index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
#                     cv2.putText(frame, "volume control ", (50, 50),
#                                 cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
#                     thumb_x, thumb_tip = int(thumb_tip * frame.shape[1]), int(thumb_tip * frame.shape[0])
#                     index_finger_x, index_tip = int(index_tip * frame.shape[1]), int(
#                         index_tip * frame.shape[0])
#
#                     # Calculate distance between thumb and index finger
#                     distance = ((index_finger_x - thumb_x) ** 2 + (index_tip - thumb_tip) ** 2) ** 0.5
#                     # time.sleep(2)
#                     if distance > 40:
#                         py.press("volumeup")
#                     else:
#                         py.press("volumedown")
#                 # for  play
#                 elif index_tip < index_pip and middle_tip < middle_pip and ring_tip < ring_pip and pinky_tip < pinky_pip:
#                     cv2.putText(frame, "play ", (50, 50),
#                                 cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#                     py.press("space")
#                     time.sleep(2)
#                 # for pause
#                 elif index_tip > index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
#                     cv2.putText(frame, "pause ", (50, 50),
#                                 cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#                     py.press("space")
#                     time.sleep(2)
#                 # for scissor gesture
#
#                 elif index_tip < index_pip and middle_tip < middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
#                     cv2.putText(frame, "scissors", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#                     scissors = True
#                     py.hotkey("ctrl", "w")
#                     time.sleep(1)
#                     py.press("enter")
#                     time.sleep(3)
#                     # py.hotkey("ctrl","f2")
#
#                     # print("from paly and pause")
#                     # break
#
#                 else:
#                     cv2.putText(frame, "not detected  ", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#
#         # cv2.imshow("youtube play pause ", frame)
#
#         if cv2.waitKey(1) & 0xFF == ord("q") or scissors == True:
#             print("from cv2,waitkey", scissors)
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#
# # play_pause()

import time
import cv2
import mediapipe as mp
import pyautogui as py
import threading
import math
stop_thread = False
# Event to signal when the scissors gesture is detected
scissors_event = threading.Event()

def play_pause():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=1, min_tracking_confidence=0.5,
                           min_detection_confidence=0.5)
    mp_drawings = mp.solutions.drawing_utils

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hands_landmarks in results.multi_hand_landmarks:
                mp_drawings.draw_landmarks(frame, hands_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmarks
                index_pip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_PIP].y
                middle_pip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP].y
                ring_pip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_PIP].y
                pinky_pip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_PIP].y

                index_tip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y
                middle_tip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y
                ring_tip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP].y
                pinky_tip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP].y

                thumb_tip = hands_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].y

                # Play/Pause gesture
                if index_tip< index_pip and middle_tip< middle_pip and ring_tip < ring_pip and pinky_tip < pinky_pip:
                    cv2.putText(frame, "play", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                    py.press("space")
                    time.sleep(2)
                elif index_tip > index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
                    cv2.putText(frame, "pause", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                    py.press("space")
                    time.sleep(2)

                # Volume control gesture
                if index_tip < index_pip and middle_tip > middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip:
                    cv2.putText(frame, "volume control ", (50, 50),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

                    thumb_x, thumb_tip = int(thumb_tip * frame.shape[1]), int(thumb_tip * frame.shape[0])
                    index_finger_x, index_tip = int(index_tip * frame.shape[1]), int(
                        index_tip * frame.shape[0])

                    # Calculate distance between thumb and index finger
                    distance = ((index_finger_x - thumb_x) ** 2 + (index_tip - thumb_tip) ** 2) ** 0.5
                    # time.sleep(2)
                    if distance > 40:
                        py.press("volumeup")
                    else:
                        py.press("volumedown")

                # Scissor gesture (to close the application)
                elif index_tip< index_pip and middle_tip< middle_pip and ring_tip > ring_pip and pinky_tip > pinky_pip and thumb_tip > ring_pip:
                    cv2.putText(frame, "scissors (closing app)", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                    time.sleep(2)
                    py.hotkey("ctrl", "w")  # Close the browser tab or window
                    time.sleep(1)
                    py.press("enter")  # Confirm any prompts if necessary
                    scissors_event.set()  # Signal the scissors event
                    time.sleep(1)
                    break  # Exit the loop to stop the thread

        # Display the frame (optional, for debugging)
        # cv2.imshow("Hand Gesture Control", frame)

        # Break the loop if 'q' is pressed or scissors gesture is detected
        if cv2.waitKey(1) & 0xFF == ord("q") or scissors_event.is_set():
            break

    cap.release()
    cv2.destroyAllWindows()