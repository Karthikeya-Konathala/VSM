import speech_recognition as sr
import pyttsx3
import webbrowser
import time
 
r = sr.Recognizer()
r.energy_threshold = 4000  # Adjust this value based on your environment
engine = pyttsx3.init()
 
def speak(text):
    engine.say(text)
    engine.runAndWait()
 
def extract_name(text):
    name = text.lower().split("my name is")[-1].strip()
    return name.capitalize()
 
def record_text():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source, timeout=10)  # Increase the timeout value
            text = r.recognize_google(audio)
            speak("You said: " + text)
            print("Recognized text: " + text)  # Debug print
            return text
    except sr.RequestError as e:
        speak("Could not request results; {0}".format(e))
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        speak("Speech recognition could not understand audio")
        print("Speech recognition could not understand audio")
    except sr.WaitTimeoutError:
        speak("Listening timed out. Please speak again.")
        print("Listening timed out. Please speak again.")
    return None
 
def get_yes_no_response(prompt):
    speak(prompt)
    while True:
        response = record_text()
        if response:
            if any(keyword in response.lower() for keyword in ["yes", "yeah", "sure", "okay", "absolutely"]):
                return True
            elif any(keyword in response.lower() for keyword in ["no", "not now", "nope", "skip"]):
                return False
            speak("I'm sorry, I didn't understand. Please respond with 'yes' or 'no.'")
 
def output_text(name, text):
    if text:
        with open("summary.txt", "a") as f:
            f.write(f"{name}:\n{text}\n\n")
        print(f"Wrote Text Successfully for {name}")
 
# Function to start a Teams meeting using a meeting URL
def start_teams_meeting(meeting_url):
    speak("Starting the meeting. Please wait for a moment.")
    time.sleep(1)
   
    # Turn off the microphone by default when opening the meeting
    with sr.Microphone() as source:
        pass
   
    webbrowser.open_new_tab(meeting_url)
    # Wait for the meeting to open, adjust this delay based on your system's performance and network speed
    time.sleep(10)
 
# Provide the Teams meeting URL here
meeting_url = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_OWVlZDdmYTEtMjllMy00MzYyLTllNzMtZjY3ZGE4YzA3ZGJm%40thread.v2/0?context=%7b%22Tid%22%3a%22e741d71c-c6b6-47b0-803c-0f3b32b07556%22%2c%22Oid%22%3a%22393222d9-0fe5-48dc-a2b9-d963416b4ce5%22%7d"
start_teams_meeting(meeting_url)
 
# Main loop for the virtual Scrum Master
while True:
    speak("Hello! I'm your virtual Scrum Master. Who do I have the pleasure of speaking with?")
    intro_text = record_text()
    name = extract_name(intro_text)
    speak(f"Welcome, {name}! How can I assist you in today's Scrum meeting?")
 
 
    provide_updates_response = get_yes_no_response("Would you like to provide updates? (yes/no):")
    if not provide_updates_response:
        speak("Thank you. If you have any other questions, feel free to ask. End of Scrum meeting.")
        print("End of Scrum meeting.")
        break
 
    speak(f"Please share your updates {name}. What have you been working on since our last meeting?")
    print("Before recording update text")  # Debug print
    while True:
        update_text = record_text()
        print("After recording update text")  # Debug print
        if not update_text:
            continue
        elif any(keyword in update_text.lower() for keyword in ["thank you", "done", "finished"]):
            output_text(name, update_text)
            break
        output_text(name, update_text)
        speak("Anything else? (yes/no):")
        response = get_yes_no_response("")
        if not response:
            break  # Break the loop if response is False
 
    speak("Is there another team member who would like to provide updates? (yes/no):")
    another_participant_response = get_yes_no_response("")
    if not another_participant_response:
        speak(f"Thank you for the updates, {name}. If you need further assistance, feel free to reach out. End of Scrum meeting.")
        print("End of Scrum meeting.")
        break


