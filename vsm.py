# import tkinter as tk
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3
# import time

# class SpeechRecognitionApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Speech Recognition App")

#         self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
#         self.text_box.pack(padx=10, pady=10)

#         self.is_conversing = False
#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()

#         self.members = ["Karthikeya", "Nirupam"]
#         self.conversation_thread = threading.Thread(target=self.conversation_thread_func)

#     def start_conversation(self):
#         if not self.is_conversing:
#             self.is_conversing = True
#             self.conversation_thread.start()

#     def conversation_thread_func(self):
#         for member in self.members:
#             # App speaks
#             app_message = f"{member}, what are your plans for today?"
#             self.update_text_box("App: " + app_message)
#             self.engine.say(app_message)
#             self.engine.runAndWait()

#             # User responds with a reduced timeout
#             user_response = self.listen_for_response(timeout=5)  # Adjust the timeout as needed (in seconds)
#             self.update_text_box(f"{member}: " + user_response)

#         self.is_conversing = False

#     def listen_for_response(self, timeout=10):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening for response...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout)
#                 response = self.recognizer.recognize_google(audio)
#                 print("User said:", response)
#                 return response
#             except sr.UnknownValueError:
#                 print("Sorry, could not understand audio.")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#             except sr.WaitTimeoutError:
#                 print("Listening timed out.")
#         return "No response."

#     def update_text_box(self, text):
#         self.text_box.insert(tk.END, text + "\n")
#         self.text_box.yview(tk.END)

#     def run(self):
#         self.start_conversation()
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = SpeechRecognitionApp()
#     app.run()

# import tkinter as tk     #recognizing and by telling thanks buddy it will close
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3
# import time

# class SpeechRecognitionApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Speech Recognition App")

#         self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
#         self.text_box.pack(padx=10, pady=10)

#         self.is_conversing = False
#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()

#         self.members = ["Karthikeya", "Nirupam"]
#         self.conversation_thread = threading.Thread(target=self.conversation_thread_func)

#     def start_conversation(self):
#         if not self.is_conversing:
#             self.is_conversing = True
#             self.conversation_thread.start()

#     def conversation_thread_func(self):
#         for member in self.members:
#             # App speaks
#             app_message = f"{member}, what are your plans for today?"
#             self.update_text_box("App: " + app_message)
#             self.engine.say(app_message)
#             self.engine.runAndWait()

#             # User responds with a reduced timeout
#             user_response = self.listen_for_response(timeout=5)  # Adjust the timeout as needed (in seconds)
#             self.update_text_box(f"{member}: " + user_response)

#             # Check if user response contains "Thanks buddy"
#             if "Thanks buddy" in user_response:
#                 break  # Exit the loop and close GUI

#         self.is_conversing = False
#         self.root.destroy()  # Close the GUI

#     def listen_for_response(self, timeout=10):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening for response...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout)
#                 response = self.recognizer.recognize_google(audio)
#                 print("User said:", response)
#                 return response
#             except sr.UnknownValueError:
#                 print("Sorry, could not understand audio.")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#             except sr.WaitTimeoutError:
#                 print("Listening timed out.")
#         return "No response."

#     def update_text_box(self, text):
#         self.text_box.insert(tk.END, text + "\n")
#         self.text_box.yview(tk.END)

#     def run(self):
#         self.start_conversation()
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = SpeechRecognitionApp()
#     app.run()



# import tkinter as tk            #complete working mvp without teams
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3
# import time

# class SpeechRecognitionApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Speech Recognition App")

#         self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
#         self.text_box.pack(padx=10, pady=10)

#         self.is_conversing = False
#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()

#         self.members = ["Karthikeya", "Nirupam"]
#         self.conversation_thread = threading.Thread(target=self.conversation_thread_func)

#     def start_conversation(self):
#         if not self.is_conversing:
#             self.is_conversing = True
#             self.conversation_thread.start()

#     def conversation_thread_func(self):
#         conversation_summary = ""
#         for member in self.members:
#             # Bot speaks
#             bot_message = f"{member}, what are your plans for today?"
#             self.update_text_box("VSM: " + bot_message)
#             self.engine.say(bot_message)
#             self.engine.runAndWait()

#             # User responds with a reduced timeout
#             user_response = self.listen_for_response(timeout=5)  # Adjust the timeout as needed (in seconds)
#             self.update_text_box(f"{member}: " + user_response)

#             # Add both the question and response to the conversation summary
#             conversation_summary += f"VSM: {bot_message}\n"
#             conversation_summary += f"{member}: {user_response}\n"

#             # Check if user response contains "Thanks buddy"
#             if "Thanks buddy" in user_response:
#                 break  # Exit the loop and close GUI

#         # Save conversation summary to the output file
#         self.save_to_output_file(conversation_summary)

#         self.is_conversing = False
#         self.root.destroy()  # Close the GUI

#     def listen_for_response(self, timeout=10):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening for response...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout)
#                 response = self.recognizer.recognize_google(audio)
#                 print("User said:", response)
#                 return response
#             except sr.UnknownValueError:
#                 print("Sorry, could not understand audio.")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#             except sr.WaitTimeoutError:
#                 print("Listening timed out.")
#         return "No response."

#     def update_text_box(self, text):
#         self.text_box.insert(tk.END, text + "\n")
#         self.text_box.yview(tk.END)

#     def save_to_output_file(self, text):
#         with open("output.txt", "w") as file:
#             file.write(text)

#     def run(self):
#         self.start_conversation()
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = SpeechRecognitionApp()
#     app.run()




# import tkinter as tk
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3
# import schedule
# import webbrowser
# import requests
# import time

# class SpeechRecognitionApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Speech Recognition App")

#         self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
#         self.text_box.pack(padx=10, pady=10)

#         self.is_conversing = False
#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()

#         self.members = ["Karthikeya", "Nirupam"]
#         self.conversation_thread = threading.Thread(target=self.conversation_thread_func)

#     def start_conversation(self):
#         if not self.is_conversing:
#             self.is_conversing = True
#             self.conversation_thread.start()

#     def conversation_thread_func(self):
#         conversation_summary = ""
#         for member in self.members:
#             # Bot speaks
#             bot_message = f"{member}, what are your plans for today?"
#             self.update_text_box("VSM: " + bot_message)
#             self.engine.say(bot_message)
#             self.engine.runAndWait()

#             # User responds with a reduced timeout
#             user_response = self.listen_for_response(timeout=5)  # Adjust the timeout as needed (in seconds)
#             self.update_text_box(f"{member}: " + user_response)

#             # Add both the question and response to the conversation summary
#             conversation_summary += f"VSM: {bot_message}\n"
#             conversation_summary += f"{member}: {user_response}\n"

#             # Check if user response contains "Thanks buddy"
#             if "Thanks buddy" in user_response:
#                 break  # Exit the loop and close GUI

#         # Save conversation summary to the output file
#         self.save_to_output_file(conversation_summary)

#         self.is_conversing = False
#         self.root.destroy()  # Close the GUI

#     def listen_for_response(self, timeout=10):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening for response...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout)
#                 response = self.recognizer.recognize_google(audio)
#                 print("User said:", response)
#                 return response
#             except sr.UnknownValueError:
#                 print("Sorry, could not understand audio.")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#             except sr.WaitTimeoutError:
#                 print("Listening timed out.")
#         return "No response."

#     # def update_text_box(self, text):
#     #     self.text_box.insert(tk.END, text + "\n")
#     #     self.text_box.yview(tk.END)
    
#     def update_text_box(self, text):
#         self.root.after(0, self.text_box.insert, tk.END, text + "\n")
#         self.root.after(0, self.text_box.yview, tk.END)



#     def save_to_output_file(self, text):
#         with open("output.txt", "w") as file:
#             file.write(text)

#     def schedule_meeting(self):
#         # Define a function to join the meeting
#         def join_meeting():
#             # Replace these values with your own meeting ID and password
#             meeting_id = "956 827 639 964 3"
#             meeting_pass = "29dpKH"

#             # Construct the meeting URL with the ID and password
#             meeting_url = f"https://teams.live.com/meet/9568276399643?p=X90bATWnRFAIpbbH{meeting_id}?pwd={meeting_pass}"

#             print(f"Opening the meeting URL: {meeting_url}")

#             # Open the meeting URL in the default browser
#             webbrowser.open(meeting_url)

#         # Schedule the function to run at 10:00 AM
#         schedule.every().day.at("14:00").do(join_meeting)

#         # Loop until the scheduled time is reached
#         while True:
#             # Run the pending tasks
#             schedule.run_pending()
#             # Wait for one second
#             time.sleep(1)

#     def run(self):
#         self.start_conversation()
#         self.schedule_meeting()
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = SpeechRecognitionApp()
#     app.run()



# import tkinter as tk
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3
# import schedule
# import webbrowser
# import requests
# import time
# import queue

# class SpeechRecognitionApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Speech Recognition App")

#         self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
#         self.text_box.pack(padx=10, pady=10)

#         self.is_conversing = False
#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()

#         self.members = ["Karthikeya", "Nirupam"]
#         self.conversation_thread = threading.Thread(target=self.conversation_thread_func)

#         self.queue = queue.Queue()

#     def start_conversation(self):
#         if not self.is_conversing:
#             self.is_conversing = True
#             self.conversation_thread.start()

#     def conversation_thread_func(self):
#         for member in self.members:
#             # Bot speaks
#             bot_message = f"{member}, what are your plans for today?"
#             self.queue.put("VSM: " + bot_message)
#             self.engine.say(bot_message)
#             self.engine.runAndWait()

#             # User responds with a reduced timeout
#             user_response = self.listen_for_response(timeout=5)  # Adjust the timeout as needed (in seconds)
#             self.queue.put(f"{member}: " + user_response)

#             # Check if user response contains "Thanks buddy"
#             if "Thanks buddy" in user_response:
#                 break  # Exit the loop and close GUI

#         self.is_conversing = False
#         self.root.destroy()  # Close the GUI

#     def listen_for_response(self, timeout=10):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening for response...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout)
#                 response = self.recognizer.recognize_google(audio)
#                 print("User said:", response)
#                 return response
#             except sr.UnknownValueError:
#                 print("Sorry, could not understand audio.")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#             except sr.WaitTimeoutError:
#                 print("Listening timed out.")
#         return "No response."

#     def update_text_box(self):
#         while True:
#             try:
#                 item = self.queue.get(block=False)
#             except queue.Empty:
#                 break
#             else:
#                 self.text_box.insert(tk.END, item + "\n")
#                 self.text_box.yview(tk.END)

#         self.root.after(100, self.update_text_box)

#     def schedule_meeting(self):
#         # Define a function to join the meeting
#         def join_meeting():
#             # Replace these values with your own meeting ID and password
#             meeting_id = "956 827 639 964 3"
#             meeting_pass = "29dpKH"

#             # Construct the meeting URL with the ID and password
#             meeting_url = f"https://teams.live.com/meet/9568276399643?p=X90bATWnRFAIpbbH{meeting_id}?pwd={meeting_pass}"

#             print(f"Opening the meeting URL: {meeting_url}")

#             # Open the meeting URL in the default browser
#             webbrowser.open(meeting_url)

#         # Schedule the function to run at 10:00 AM
#         schedule.every().day.at("15:13").do(join_meeting)

#         # Loop until the scheduled time is reached
#         while True:
#             # Run the pending tasks
#             schedule.run_pending()
#             # Wait for one second
#             time.sleep(1)

#     def run(self):
#         self.start_conversation()
#         self.update_text_box()
#         self.schedule_meeting()
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = SpeechRecognitionApp()
#     app.run()

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
        schedule.every().day.at("17:24").do(self.display_alert_message)

        # Schedule joining the meeting after 2 minutes
        schedule.every().day.at("17:25").do(self.join_meeting)

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
        meeting_id = "956 827 639 964 3"
        meeting_pass = "29dpKH"

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
    
    
# import tkinter as tk                              
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3
# import schedule
# import webbrowser
# import pyautogui
# import time

# class SpeechRecognitionApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Speech Recognition App")

#         self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=10)
#         self.text_box.pack(padx=10, pady=10)

#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()

#         self.members = ["Karthikeya", "Nirupam"]

#     def start_conversation(self):
#         # Start a new thread for scheduling the meeting
#         threading.Thread(target=self.schedule_meeting).start()

#     def schedule_meeting(self):
#         # Schedule displaying the alert message after 1 minute
#         schedule.every().day.at("16:40").do(self.display_alert_message)

#         # Schedule joining the meeting after 2 minutes
#         schedule.every().day.at("16:41").do(self.join_meeting)

#         # Run the pending tasks
#         while True:
#             schedule.run_pending()

#     def display_alert_message(self):
#         for member in self.members:
#             alert_message = f"Alert: Please be prepared for the meeting in 1 minute, {member}."
#             self.update_text_box(alert_message)
#             self.engine.say(alert_message)
#             self.engine.runAndWait()

#     def join_meeting(self):
#         # Replace these values with your own meeting ID and password
#         meeting_id = "956 827 639 964 3"
#         meeting_pass = "29dpKH"

#         # Construct the meeting URL with the ID and password
#         meeting_url = f"https://teams.live.com/meet/{meeting_id}?pwd={meeting_pass}"

#         print(f"Opening the meeting URL: {meeting_url}")

#         # Open the meeting URL in the default browser
#         webbrowser.open(meeting_url)

#         # Wait for the page to load
#         time.sleep(5)

#         # Simulate keyboard input to enter the password
#         pyautogui.write(meeting_pass)
#         pyautogui.press('enter')

#         for member in self.members:
#             # Bot speaks
#             bot_message = f"{member}, what are your plans for today?"
#             self.update_text_box("VSM: " + bot_message)
#             self.engine.say(bot_message)
#             self.engine.runAndWait()

#             # User responds
#             user_response = self.listen_for_response(timeout=5)
#             self.update_text_box(f"{member}: " + user_response)

#             # Save the conversation to output file
#             self.save_to_output_file(f"VSM: {bot_message}\n{member}: {user_response}\n")

#             # Check if user response contains "Thanks buddy"
#             if "Thanks buddy" in user_response:
#                 break

#         self.root.destroy()  # Close the GUI

#     def listen_for_response(self, timeout=10):
#         with sr.Microphone() as source:
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening for response...")
#             try:
#                 audio = self.recognizer.listen(source, timeout=timeout)
#                 response = self.recognizer.recognize_google(audio)
#                 print("User said:", response)
#                 return response
#             except sr.UnknownValueError:
#                 print("Sorry, could not understand audio.")
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#             except sr.WaitTimeoutError:
#                 print("Listening timed out.")
#         return "No response."

#     def update_text_box(self, text):
#         self.text_box.insert(tk.END, text + "\n")
#         self.text_box.yview(tk.END)

#     def save_to_output_file(self, text):
#         with open("output.txt", "a") as file:
#             file.write(text)

#     def run(self):
#         self.start_conversation()
#         self.root.mainloop()

# if __name__ == "__main__":
#     app = SpeechRecognitionApp()
#     app.run()




