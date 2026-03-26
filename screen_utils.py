import pyautogui
import cv2
import numpy as np
import threading
import time
import os

# ---------------------------
# Screenshot Function
# ---------------------------
def take_screenshot(filename=None):
    """
    Take a screenshot and save it.
    """
    if not filename:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved: {filename}")
    return filename


# ---------------------------
# Screen Recording Class
# ---------------------------
class ScreenRecorder:
    def __init__(self, output=None, fps=20):
        screen_size = pyautogui.size()
        self.screen_size = screen_size
        self.fps = fps
        self.recording = False
        self.thread = None
        if not output:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            output = f"screen_record_{timestamp}.avi"
        self.output = output

    def start(self):
        """
        Start screen recording in a separate thread.
        """
        if self.recording:
            print("Already recording!")
            return
        self.recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()
        print("Screen recording started...")

    def stop(self):
        """
        Stop screen recording.
        """
        if not self.recording:
            print("Not recording currently!")
            return
        self.recording = False
        self.thread.join()
        print(f"Screen recording saved as {self.output}")

    def _record(self):
        """
        Internal method to record the screen.
        """
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(self.output, fourcc, self.fps, self.screen_size)

        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)

        out.release()