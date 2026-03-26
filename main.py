from voice_assistant import listen_command, speak
from screen_utils import take_screenshot, ScreenRecorder

def main():
    speak("Hello, I am Jarvis. How can I help you?")
    
    recorder = ScreenRecorder()  # Threaded screen recorder

    while True:
        command = listen_command()

        # -----------------------------
        # Screenshot Command
        # -----------------------------
        if "screenshot" in command:
            filename = take_screenshot()
            speak(f"Screenshot saved as {filename}")

        # -----------------------------
        # Start Screen Recording
        # -----------------------------
        elif "start recording" in command:
            if recorder.recording:
                speak("Screen recording is already running.")
            else:
                recorder.start()
                speak("Screen recording started.")

        # -----------------------------
        # Stop Screen Recording
        # -----------------------------
        elif "stop recording" in command:
            if recorder.recording:
                recorder.stop()
                speak("Screen recording stopped.")
            else:
                speak("No active screen recording to stop.")

        # -----------------------------
        # Greeting Command
        # -----------------------------
        elif "hello" in command or "hi" in command:
            speak("Hello! I am here.")

        # -----------------------------
        # Exit Command
        # -----------------------------
        elif "exit" in command or "quit" in command or "bye" in command:
            if recorder.recording:
                recorder.stop()
            speak("Goodbye! Have a nice day.")
            break

        # -----------------------------
        # Unknown Command
        # -----------------------------
        elif command != "":
            speak("Sorry, I did not understand that command.")


if __name__ == "__main__":
    main()