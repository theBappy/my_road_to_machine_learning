import pyttsx3 
from PyPDF2 import PdfReader
import threading
import keyboard

pdf = None
stop_thread = False

def play(pdfReader):
    global pdf
    global stop_thread

    speaker = pyttsx3.init()
    for page_num in range(len(pdfReader.pages)):
        if stop_thread:
            break
        text = pdfReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()


def stop_playback():
    global stop_thread
    input("Press enter to stop playback...")
    stop_thread = False

file = input("Enter your PDF file name: ")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print("An error occurred:\n", e)
        print("\nEnter the file name again:\n")
        file = input("Enter your PDF file again: ")

playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

keyboard.add_hotkey("q", lambda: stop_playback())
keyboard.wait()

playback_thread.join()



