# Personal AI Assistant (“JARVIS”)    

## 🦾 Project Overview  
A voice-controlled personal assistant written in Python, leveraging speech recognition, text-to-speech, web interaction and automation libraries. On hearing the wake-word **“JARVIS”**, the system listens for commands like *“play [song]”*, *“search [query]”*, or *“news”*, and executes the appropriate action (YouTube play via `pywhatkit`, Google search in browser, top-headlines read-out via NewsAPI).  

## 📌 Key Features  
- Wake-word detection using `speech_recognition`.  
- Text-to-speech via `gTTS` + audio playback using `pygame`.  
- Voice command parsing and execution (play YouTube song, perform Google search, read news headlines).  
- Easily extensible for new command types and actions.  

## 🧰 Technologies & Libraries  
- Python 3.x  
- `speech_recognition` — capture and interpret microphone audio.  
- `gtts` & `pygame` — convert text to speech and play audio.  
- `pyttsx3` — alternative offline TTS (optional).  
- `pywhatkit` — YouTube search & play.  
- `requests` — HTTP calls to NewsAPI for headlines.  
- `webbrowser` — open default browser for Google searches. 
