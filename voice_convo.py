import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
for voice in voices:
    print(voice.id)
    print(voice.name)

id= "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty("voice", id)
engine.setProperty("rate", 170)  #higher rate == higher speed
engine.say("hello world") #replace hello world with your own text
engine.runAndWait()
