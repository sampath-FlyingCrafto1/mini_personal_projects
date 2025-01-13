# Speech-to-Text with Text-to-Speech

This Python script demonstrates a simple speech-to-text and text-to-speech application.

**Features:**

- **Speech Recognition:** Uses the `speech_recognition` library to capture audio input from the microphone and convert it to text using Google Speech Recognition.
- **Text-to-Speech:** Uses the `pyttsx3` library to convert the recognized text to speech and play it back.
- **Error Handling:** Includes basic exception handling to gracefully manage potential errors during speech recognition, such as network issues or unrecognized speech.
- **Continuous Listening:** Runs in an infinite loop, continuously listening for user input and providing real-time speech-to-text and text-to-speech functionality.

**Requirements:**

- `speech_recognition` library: `pip install speechrecognition`
- `pyttsx3` library: `pip install pyttsx3`

**How to Run:**

1. Save the code as a Python file (e.g., `speech_to_text_tts.py`).
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using the following command:

```bash
python speech_to_text_tts.py