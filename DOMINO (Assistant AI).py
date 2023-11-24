import speech_recognition as sr
import pyttsx3
import datetime
import The_View as tv


# Finding time
def time():
    ty = datetime.datetime.now()
    fy = ty.strftime("%m/%d/%Y %H:%M:%S")
    tyi = str(fy)
    return tyi[11:-3]


# Vivi's talking function
def vivi_replies(talk, speed=130):
    eng = pyttsx3.init()
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[1].id)
    eng.setProperty('rate', speed)
    eng.say(talk)
    eng.runAndWait()


r = sr.Recognizer()


# Microphone from laptop
with sr.Microphone() as source:
    vivi_replies("Hi! How may I help you?", 200)
    r.adjust_for_ambient_noise(source, duration=1)
    r.dynamic_energy_threshold = True
    audio = r.listen(source, timeout=10, phrase_time_limit=10)
    vivi_replies("Please wait a moment....")

# Processing text
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))

    if text in tv.list_of_possible_time_phrases:
        vivi_replies("The time is {}".format(time()))


except sr.UnknownValueError:
    vivi_replies("Sorry, Vivi could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except sr.WaitTimeoutError:
    vivi_replies("TimeOut Error", 200)
