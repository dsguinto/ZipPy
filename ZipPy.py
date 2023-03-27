import threading
import tkinter as tk
from tkinter import scrolledtext as st
import speech_recognition as sr
import pyttsx3
import webbrowser

# Potential libs we may need
# import webbrowser
# import wikipedia
# from ttkthemes import themed_tk
# from PIL import ImageTk, Image
# import modules

# Create thread class to allow for for the speech recognition code to run a the same time as the Tkinter window Application code
class SpeechRecognitionThread(threading.Thread):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def run(self):
        main(self)


# Defines the main listening and response events
def main(self):
    try:
        while True:
            query = Application.takeCommand(self).lower()
            print(query)

            if "open google" in query:
                self.callback("Opening Google")
                webbrowser.open("https://www.google.com")
                continue

    except Exception as e:
        print("something failed :(")
        # root.quit() # To Close app on failure


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.speech_thread = SpeechRecognitionThread(self.updating_ST)
        self.speech_thread.start()

    # Listens for user voice input and returns it as text to be assigned as a query in the main() method
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                try:
                    self.callback("Listening...")
                    audio = r.listen(source, timeout=2)
                    self.callback("Recognizing...")
                    text = r.recognize_google(audio)
                    self.callback("You said: " + text)

                except sr.WaitTimeoutError:
                    self.callback("No response")
                    pass
                    return "None"

                return text

    # Create scrollable text section with placeholder text
    def create_widgets(self):
        self.scrollable_text = st.ScrolledText(
            root,
            state="normal",
            height=25,
            width=75,
            relief="sunken",
            bd=5,
            wrap=tk.WORD,
            bg="#d4f0fc",
            fg="#01303f",
        )
        self.scrollable_text.insert(tk.INSERT, "Hello, How can I help you?")
        self.scrollable_text.configure(state="disabled")
        self.scrollable_text.pack()

    # Update text on scrollable text section
    def updating_ST(self, text):
        self.scrollable_text.configure(state="normal")
        self.scrollable_text.insert(tk.END, "\n" + text + "\n")
        self.scrollable_text.configure(state="disabled")


# Set up tkinter window formatting
root = tk.Tk()
root.title("ZipPy")
root.resizable(True, True)
root.geometry("500x750")
root.configure(bg="#f5f5f5")

# Set up app variable to use the Application class methods
app = Application(master=root)
app.mainloop()
