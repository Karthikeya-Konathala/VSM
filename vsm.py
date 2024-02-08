import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import schedule
import webbrowser

class SpeechRecognitionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speech Recognition App")

        self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
        self.text_box.pack(padx=10, pady=10)

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.members = ["Karthikeya", "Nirupam"]

    def start_conversation(self):
        # Start a new thread for scheduling the meeting
        threading.Thread(target=self.schedule_meeting).start()

    def schedule_meeting(self):
        # Schedule displaying the alert message after 1 minute
        self.root.after(1000 * 60, self.display_alert_message) # Run after 1 minute

        #schedule.every().day.at("9:41").do(self.display_alert_message)

        # Schedule joining the meeting after 2 minutes
        self.root.after(1000 * 120, self.join_meeting) # Run after 2 minutes

        #schedule.every().day.at("9:42").do(self.join_meeting)

        # Run the pending tasks
        while True:
            schedule.run_pending()

    def display_alert_message(self):
        for member in self.members:
            alert_message = f"Alert: Please be prepared for the meeting in 1 minute, {member}."
            self.update_text_box(alert_message)
            self.engine.say(alert_message)
            self.engine.runAndWait()

    def join_meeting(self):
        # Replace these values with your own meeting ID and password
        meeting_id = "240 574 856 395"
        meeting_pass = "uX6xpT"

        # Construct the meeting URL with the ID and password
        meeting_url = f"https://teams.live.com/meet/{meeting_id}?pwd={meeting_pass}"

        print(f"Opening the meeting URL: {meeting_url}")

        # Open the meeting URL in the default browser
        webbrowser.open(meeting_url)

        for member in self.members:
            # Bot speaks
            bot_message = f"{member}, what are your plans for today?"
            self.update_text_box("VSM: " + bot_message)
            self.engine.say(bot_message)
            self.engine.runAndWait()

            # User responds
            user_response = self.listen_for_response(timeout=5)
            self.update_text_box(f"{member}: " + user_response)

            # Save the conversation to output file
            self.save_to_output_file(f"VSM: {bot_message}\n{member}: {user_response}\n")

            # Check if user response contains "Thanks buddy"
            if "Thanks buddy" in user_response:
                break

        self.root.destroy()  # Close the GUI

    def listen_for_response(self, timeout=10):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening for response...")
            try:
                audio = self.recognizer.listen(source, timeout=timeout)
                response = self.recognizer.recognize_google(audio)
                print("User said:", response)
                return response
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.WaitTimeoutError:
                print("Listening timed out.")
        return "No response."

    def update_text_box(self, text):
        self.text_box.insert(tk.END, text + "\n")
        self.text_box.yview(tk.END)

    def save_to_output_file(self, text):
        with open("output.txt", "a") as file:
            file.write(text)

    def run(self):
        self.start_conversation()
        self.root.mainloop()

if __name__ == "__main__":
    app = SpeechRecognitionApp()
    app.run()
