import time
import threading
import pyttsx3
import speech_recognition as sr
from batteryStatus import check_battery
from BertTextClassification import classify_text
from conversation_module import convo
from Internetquery import *
from system_applications import *
import warnings
from sentiment_anal import sentiment

warnings.simplefilter("ignore")

Internet_thread = None


def speak(text):
    engine = pyttsx3.init()
    # voices = engine.getProperty("voices")
    # for voice in voices:
    #     print(voice.id)
    #     print(voice.name)
    id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", id)
    engine.setProperty("rate", 175)  # for speech rate -> the higher - the more speed
    engine.say(text)
    engine.runAndWait()


# battery_thread.start()

# opening_internet = threading.Thread(target=internet, daemon=False)
# opening_internet.start()




def speech_recog():
    global Internet_thread
    if Internet_thread is None or not Internet_thread.is_alive():
        Internet_thread = threading.Thread(target=internet)
        Internet_thread.start()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio_data = r.listen(source, 0, 15)

        try:
            print("Recognizing..")
            q = r.recognize_google(audio_data, language="en")
            print(f"User spoke: {q}")
            x = classify_text(q)
            #  for conversational query
            if x == "Internet Query":
                print("calling conversational module")
                sentiment(q, speak)
                convo(q, speak)

            # for internet module
            elif x == "Conversation":
                print("calling internet query")
                sendkeys(q, speak)
            # for automation query
            else:
                print("calling automation query")
                application(q, speak)
        except Exception as e:
            print("Speech recognition error:", str(e))


print("about to start ")
while True:
    speech_recog()
    check_battery(speak)
    time.sleep(2)
#
#
# def classify_and_execute(q):
#     global micro_phone
#     """ Classifies the speech and executes respective module """
#     x = classify_text(q)
#     if x == "Internet Query":
#         micro_phone=False
#         print("Calling Internet module")
#         convo(q) # Uncomment if conversation module is implemented
#     elif x == "Conversation":
#         print("Calling Conversation module")
#         # speak(internet(q))
#     elif x == "Automation":
#         micro_phone = False
#         print("Calling Automation module")
#         automation_thread = threading.Thread(target=application, args=(q,), daemon=True)
#         automation_thread.start()
#         micro_phone=True
#         print("from jarvis")
#
#     else:
#         print("Not recognized")
#
# Run speech recognition in a separate thread
