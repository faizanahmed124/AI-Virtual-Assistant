import speech_recognition as sr
import pyttsx3

# ----------------------------
# Initialize TTS engine
# ----------------------------
engine = pyttsx3.init()

def speak(text):
    """
    Speak the given text using pyttsx3
    """
    engine.say(text)
    engine.runAndWait()


# ----------------------------
# Listen and recognize command
# ----------------------------
def listen_command():
    r = sr.Recognizer()
    r.energy_threshold = 300               # minimum energy to detect sound
    r.dynamic_energy_threshold = True      # auto adjust for background noise

    try:
        with sr.Microphone(device_index=8) as source:  # PipeWire device index
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=10)

            # DEBUG: check captured audio length
            print("Audio captured length:", len(audio.frame_data))

            # Recognize using Google API
            command = r.recognize_google(audio).lower()
            print("You said:", command)
            return command

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Speech service error.")
        return ""

    except Exception as e:
        print("Microphone error:", str(e))
        speak("Microphone error.")
        return ""