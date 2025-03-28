import webbrowser
import winsound
import re
import subprocess
import pywhatkit as pk
import pyautogui as py
from sklearn.metrics.pairwise import cosine_similarity
from conversation_module import model
# from youtubePausePlay import play_pause,scissors
from youtubePausePlay import play_pause, scissors_event, stop_thread

from closingApplication import application_closed, close
import threading
import time

# from VolumeControlHandGesture import volume_adjust
# youtube_status = False


# def opening_music():
#     # global scissors
#     print("from system applications",scissors)
#     global youtube_status
#     if not youtube_status:
#         webbrowser.open("https://music.youtube.com/watch?v=_PBlykN4KIY&list=LM")
#         time.sleep(5)
#         play_pause_thread = threading.Thread(target=play_pause, daemon=True)
#         play_pause_thread.start()
#         # volume.start()
#
#         print("from opening_music",scissors)
#         # time.sleep()
#         while not scissors:
#         #     time.sleep(3)
#             print("in while loop",scissors)
#         #     pass
#
#
#
#
#     else:
#         print("already opened")
#     print(youtube_status)
# import webbrowser
import threading
import time
from youtubePausePlay import play_pause, scissors_event, stop_thread

youtube_status = False


def opening_music():
    global youtube_status, stop_thread
    if not youtube_status:
        # Open YouTube Music
        webbrowser.open("https://music.youtube.com/watch?v=_PBlykN4KIY&list=LM")
        youtube_status = True
        time.sleep(5)

        # Start the hand gesture detection thread
        stop_thread = False  # Reset the thread stop flag
        scissors_event.clear()  # Reset the scissors event
        play_pause_thread = threading.Thread(target=play_pause, daemon=True)
        play_pause_thread.start()

        # Wait until the scissors gesture is detected
        while not scissors_event.is_set():
            time.sleep(1)
            print("Waiting for scissors gesture...")

        print("Scissors gesture detected. Closing application.")
        stop_thread = True  # Signal the thread to stop
        youtube_status = False  # Reset the status
    else:
        print("Already opened")


# playing videos of users interest...
# def opening_video(user_request):
#     commands = {"play", "search", "open", "watch", "listen", "find", "show", "start", "put on", "can you",
#                 "youtube"}
#     user_request = " ".join([word for word in user_request.lower().split() if word not in commands])
#     pk.playonyt(user_request)
#     time.sleep(3)
#     py.press("f")
#     play_pause_thread = threading.Thread(target=play_pause, daemon=True)
#     play_pause_thread.start()
#     # while not scissors:
#     #     time.sleep(1)
import threading
import time
from youtubePausePlay import play_pause, scissors_event, stop_thread
# import pywhatkit as pk
# import pyautogui as py


def opening_video(user_request):
    global stop_thread
    # Remove common commands from the user request
    commands = {"play", "search", "open", "watch", "listen", "find", "show", "start", "put on", "can you", "youtube"}
    user_request = " ".join([word for word in user_request.lower().split() if word not in commands])

    # Open the requested video on YouTube
    pk.playonyt(user_request)
    time.sleep(3)  # Wait for the browser to load the video
    py.press("f")  # Fullscreen the video

    # Start the hand gesture detection thread
    stop_thread = False  # Reset the thread stop flag
    scissors_event.clear()  # Reset the scissors event
    play_pause_thread = threading.Thread(target=play_pause, daemon=True)
    play_pause_thread.start()

    # Wait until the scissors gesture is detected
    while not scissors_event.is_set():
        time.sleep(1)
        print("Waiting for scissors gesture...")

    print("Scissors gesture detected. Closing application.")
    stop_thread = True  # Signal the thread to stop


def opening_new_doc():
    global application_closed
    print("Alright! Setting up a new document for you")
    time.sleep(2)
    subprocess.Popen("start winword", shell=True)
    time.sleep(2)
    py.press("enter")
    time.sleep(3)
    py.hotkey("win", "h")
    close_thread = threading.Thread(target=close, daemon=True)
    close_thread.start()
    # speak("You're good to go! Start speaking, and I'll take notes.")

    while not application_closed:
        time.sleep(1)
    # else:
    #     py.hotkey("ctrl","f2")


def setting_break(x,speak):
    int_d=re.findall(r"\d+",x)
    if int_d:
        int_d=int(int_d[0])
        speak(f"Initiating a {int_d}-minute pause ")
    else:
        int_d=5
        speak(f"Break set for {int_d} minutes. I'll notify you when it's over.")
    time.sleep(int_d*60)

    winsound.Beep(1000, 7000)
    speak("Boss, your scheduled break has ended. Resuming operations now.")
# setting_break("can you set the break for 10 mins")


def application(x, speak):
    automated_tasks = {
        # YouTube / Video Playback
        "play a video": [
            "open YouTube and play a video",
            "play a video on YouTube",
            "start playing a clip",
            "launch a video",
            "show me a video on YouTube",
            "play a YouTube video",
            "can you play a scene from YouTube?"
        ],

        # Music Playback
        "play music": [
            "play some music",
            "start playing songs",
            "can you turn on some music?",
            "put on a song",
            "start my playlist",
            "I want to listen to music",
            "play a song for me"
        ],

        # Word Document
        "open a word document": [
            "create a new Word file",
            "open a blank Word document",
            "can you take down notes for me?",
            "start a new document",
            "open Microsoft Word",
            "I need to write something, open Word",
            "launch a text editor"
        ],

        # Taking a Break
        "set a break": [
            "set a break for me",
            "pause my work",
            "stop working for now",
            "remind me to take a break",
            "wait a moment",
            "hold on for some time",
            "tell me when to resume work"
        ]
    }
    for i in automated_tasks.keys():
        encoded_vers = model.encode(i)
        automated_tasks[i] = encoded_vers
    # print(automated_tasks)
    user_input = x  # should be replaced -> first captured userinput variable (from speech_reco)
    encoded_userinput = model.encode(user_input)
    # print(automated_tasks)
    # print("user input ",encoded_userinput)

    a = []

    for i in automated_tasks.values():
        red = cosine_similarity([encoded_userinput], [i])
        a.append(red)
    if max(a) < 0.4:
        a = []
        print("can you say that again or applicatiion you specified does ot exists")

    # else:
    index=a.index(max(a))
    print(index)
    print(list(automated_tasks.keys())[index])

    if list(automated_tasks.keys())[index] == list(automated_tasks.keys())[0]:

        print("opening yt for video")
        opening_video(user_input)

    elif list(automated_tasks.keys())[index] == list(automated_tasks.keys())[1]:
        opening_music()
        print("opened music and closed")


    elif list(automated_tasks.keys())[index] == list(automated_tasks.keys())[2]:
        opening_new_doc()
    elif list(automated_tasks.keys())[index] == list(automated_tasks.keys())[3]:
        setting_break(x,speak)

# application("play some music")

# else:
#     print("opening word")

#
# def opening_music():
#     global youtube_status
#     if not youtube_status:
#         webbrowser.open("https://music.youtube.com/watch?v=_PBlykN4KIY&list=LM")
#         youtube_status = True
#
#     else:
#         print("already opened")
#     print(youtube_status)
#
#
# # playing videos of users interest...
# def opening_video(user_request):
#     #     for opening video
#     pk.playonyt(user_request)


# opening_video(input("what do you want to play.."))


# opening_music()
# py.press("spacebar")
# opening_youtube()
# opening_youtube()
