# 🗣️ Voice Assistant

A modular Python-based voice assistant that listens for a wake word, executes commands to open/close software, plays YouTube videos, tells the time, and handles custom queries.

## 🛠️ Features

- 🔊 Speech-to-text (using `speech_recognition`)
- 🔈 Text-to-speech (using `pyttsx3`)
- 🌐 Play YouTube videos via `pywhatkit`
- ⏰ Tell the current time
- 🔓 Open and close applications
- 📝 Easily extendable with custom commands

## 📁 Project Structure

## 🚀 Setup & Run

1. **Clone the repo**:
    ```bash
    git clone https://github.com/YourUsername/voice-assistant.git
    cd voice-assistant
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the assistant**:
    ```bash
    python main.py
    ```

4. **Use the wake word** (e.g., “Assistant”) to activate.

## ⚙️ Customize

- **Wake word**: edit `listen_for_wake_word()` default parameter in `utils/recognizer.py`.
- **Add commands**: expand `handle_custom_commands()` in `features/custom_commands.py`.

---

Made with ❤️ by Arju (ByteForge Community)