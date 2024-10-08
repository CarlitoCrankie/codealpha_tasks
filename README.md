# Jarvis - Virtual Assistant

Jarvis is a Python-based virtual assistant created as part of a task from Code Alpha. This assistant is capable of responding to user commands through both speech and text, utilizing various libraries to handle speech recognition, text-to-speech conversion, and web-based interactions.

## Features
- **Voice Commands**: Jarvis listens to user commands and processes them.
- **Text-to-Speech**: Responds to user commands verbally.
- **Web Automation**: Automates web tasks like Google searches and video playback.
- **GUI Integration**: A simple graphical interface for better interaction.

## Libraries Used and Their Functions

Here’s an overview of the key Python libraries used in building Jarvis and their functions:

1. **[`speech_recognition`](https://pypi.org/project/SpeechRecognition/)**  
   Used to convert speech into text, enabling Jarvis to process voice commands.
   
2. **[`pyttsx3`](https://pypi.org/project/pyttsx3/)**  
   Converts text into speech, allowing Jarvis to speak responses to user input.
   
3. **[`pywhatkit`](https://pypi.org/project/pywhatkit/)**  
   Simplifies automation tasks such as sending WhatsApp messages, performing Google searches, and playing YouTube videos.
   
4. **[`datetime`](https://docs.python.org/3/library/datetime.html)**  
   Handles date and time-related tasks, allowing Jarvis to provide the current time or schedule reminders.
   
5. **[`wikipedia`](https://pypi.org/project/wikipedia-api/)**  
   Allows Jarvis to fetch and provide information from Wikipedia based on user queries.
   
6. **[`requests`](https://pypi.org/project/requests/)**  
   A popular HTTP library used for making web requests, enabling Jarvis to fetch information from the web (e.g., weather updates, APIs).
   
7. **[`openpyxl`](https://pypi.org/project/openpyxl/)**  
   Enables Jarvis to read from and write to Excel files, useful for organizing or analyzing data.
   
8. **[`random`](https://docs.python.org/3/library/random.html)**  
   Used to generate random selections or responses, adding variety to Jarvis's interactions.
   
9. **[`time`](https://docs.python.org/3/library/time.html)**  
   Helps manage delays, scheduling, or measuring the duration of operations.
   
10. **[`threading`](https://docs.python.org/3/library/threading.html)**  
   Enables concurrent execution of tasks, allowing Jarvis to run multiple processes (e.g., listening and performing background tasks).
   
11. **[`subprocess`](https://docs.python.org/3/library/subprocess.html)**  
   Allows Jarvis to run system-level commands like opening files or executing programs.
   
12. **[`webbrowser`](https://docs.python.org/3/library/webbrowser.html)**  
   Opens web browsers for performing tasks like searching the web or navigating to specific websites.
   
13. **`jarvisGUI`**  
   A custom module created to provide a graphical user interface for Jarvis, enhancing user interaction through a visual platform.

## How to Use
1. **Clone the Repository**:  
   `git clone https://github.com/CarlitoCrankie/codealpha_tasks.git`

2. **Install Required Libraries**:  
   You can install the dependencies listed in the `requirements.txt` file by running:  
   `pip install -r requirements.txt`

3. **Run Jarvis**:  
   To start the assistant, run the main Python script:  
   `python secondTest.py`
