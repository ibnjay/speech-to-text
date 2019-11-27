from gtts import gTTS
from playsound import playsound
import os
import subprocess
import speech_recognition as sr

## test change
def get_users_word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print "Speak Please:"
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response["transcription"]


def speak(words_to_say):
    tts = gTTS(text=words_to_say, lang='en')
    local_audio_file = "local_temp.mp3"
    tts.save(local_audio_file)

    #Play the file and remove
    playsound(local_audio_file)
    os.remove(local_audio_file)

def greet():
    speak("Good Morning, what can i do for you?")

def repeat():
    input = get_users_word()
    speak("Did you say? " + input)
    input = get_users_word()
    if "yes" in input.lower() :
       speak("Okay")

if __name__ == '__main__':
    greet()
    repeat()
