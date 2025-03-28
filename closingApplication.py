import win32com.client
from datetime import datetime
import time

import mediapipe as mp
import cv2
import pyautogui as py

application_closed = False


def close():
    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                           min_detection_confidence=0.5, min_tracking_confidence=0.5)

    mp_drawing = mp.solutions.drawing_utils

    while True:
        global application_closed
        application_closed = False
        ret, frame = cap.read()
        image_rbg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rbg)
        if results.multi_hand_landmarks:

            for hands_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hands_landmarks, mp_hands.HAND_CONNECTIONS)

                index_finger_tip = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                index_finger_pip = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y

                middle_finger_tip = hands_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                middle_finger_pip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y

                ring_finger_tip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                ring_finger_pip = hands_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y

                # other finger
                pinky_finger_pip = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
                pinky_finger_tip = hands_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

                if index_finger_tip < index_finger_pip and middle_finger_tip < middle_finger_pip and ring_finger_tip > ring_finger_pip and pinky_finger_tip > pinky_finger_pip:
                    cv2.putText(frame, "scissors gesture \n closing current application ", (50, 50),
                                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                    py.hotkey("alt", "f4")
                    py.sleep(2)
                    py.press("enter")
                    time.sleep(2)
                    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
                    file_name = f"Notes_{timestamp}.docx"
                    py.write(file_name)
                    py.sleep(2)
                    py.press("enter")
                    time.sleep(8)
                    py.hotkey('ctrl', 'f2')
                    application_closed = True
                    # print("closed closing application ")

                else:
                    cv2.putText(frame, "not detected  ", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

        # cv2.imshow("closing applications ", frame)

        if cv2.waitKey(1) & 0xFF == ord("q") or application_closed:
            break

    cap.release()
    cv2.destroyAllWindows()

# close()


# import mediapipe as mp
# import cv2
# import pyautogui
#
# # Initialize the camera
# cap = cv2.VideoCapture(0)
#
# # Initialize Mediapipe Hands
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
#                        min_detection_confidence=0.5, min_tracking_confidence=0.5)
#
# # Initialize Mediapipe Drawing
# mp_drawing = mp.solutions.drawing_utils
#
# def close():
#     while True:
#         # Capture the frame
#         ret, frame = cap.read()
#
#         # Check if frame was captured successfully
#         if not ret:
#             print("Failed to capture frame. Exiting...")
#             break
#
#         # Convert the frame to RGB
#         image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#         # Process the frame to detect hands
#         results = hands.process(image_rgb)
#
#         # Check if any hand landmarks are detected
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#
#                 # Get landmark positions
#                 index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
#                 index_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
#
#                 middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
#                 middle_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
#
#                 ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
#                 ring_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
#
#                 pinky_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
#                 pinky_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]
#
#                 # Detect "scissors gesture"
#                 if (
#                     index_finger_tip.y < index_finger_pip.y and
#                     middle_finger_tip.y < middle_finger_pip.y and
#                     ring_finger_tip.y > ring_finger_pip.y and
#                     pinky_finger_tip.y > pinky_finger_pip.y
#                 ):
#                     cv2.putText(frame, "Scissors gesture detected: Closing application",
#                                 (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
#                     pyautogui.hotkey("alt", "f4")
#                 else:
#                     cv2.putText(frame, "Gesture not detected",
#                                 (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
#
#         # Display the frame
#         cv2.imshow("Frame", frame)
#
#         # Break loop on 'q' key press
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#
#     # Release resources
#     cap.release()
#     cv2.destroyAllWindows()
#
# # Call the close function
# close()
