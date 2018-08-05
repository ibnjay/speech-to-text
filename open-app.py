import subprocess
import random
import time
import webbrowser as wb

import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
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

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def open_an_app(name):
    if name == "photos" : 
       subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Photos.app"])
    if name == "notes" :
       subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Notes.app"])
    if name == "siri" :
       subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Siri.app"])
    if name == "safari" :
       subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/safari.app"])
    if name == "facetime" :
       subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/FaceTime.app"])
    if name == "whatsapp" :
       subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/WhatsApp.app"])
    
    print "Comleted Open_an_app"

if __name__ == "__main__":

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # format the instructions string
    command = recognize_speech_from_mic(recognizer, microphone)
    user_input = command["transcription"].lower() or " Nothing Detected"
    print "You saild " + user_input


    if "open" in user_input :
        if "photos" in user_input:
            open_an_app("photos")
        if "notes" in user_input:
            open_an_app("notes")
        if "siri" in user_input:
            open_an_app("siri")
        if "safari" in user_input:
            open_an_app("safari")
        if "facetime" in user_input:
            open_an_app("facetime")
        if "whatsapp" in user_input:
            open_an_app("whatsapp")
        print "Didn't match an app Name"
    
    else :
        print "Didn't match open clause"
