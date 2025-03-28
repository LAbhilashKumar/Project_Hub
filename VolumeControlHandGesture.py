import cv2
import pyautogui
import mediapipe as mp

def volume_adjust():
    cap = cv2.VideoCapture(0)

    # mp

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # to draw landmarks

    mp_drawings = mp.solutions.drawing_utils

    while True:
        ret, frame = cap.read()
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        if results.multi_hand_landmarks:
            for hands_landmarks in results.multi_hand_landmarks:
                mp_drawings.draw_landmarks(frame, hands_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hands_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_y = hands_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            thumb_x, thumb_y = int(thumb_y.x * frame.shape[1]), int(thumb_y.y * frame.shape[0])
            index_finger_x, index_finger_y = int(index_finger_y.x * frame.shape[1]), int(
                index_finger_y.y * frame.shape[0])

            # Calculate distance between thumb and index finger
            distance = ((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2) ** 0.5

            if distance > 40:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

        cv2.imshow("volume adjust", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
# volume_adjust()