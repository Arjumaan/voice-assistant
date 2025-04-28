# 🧠 Voice Assistant

A smart **Voice Assistant** powered by **Python** and **PyQt5**.  
It listens for a wake word, executes commands like opening/closing apps, telling time, and even handling custom commands.  
The project features a clean GUI with profile picture, animated listening logs, start/stop buttons, and more!

---

## ✨ Features

- 🎙️ Start and Stop voice assistant easily from GUI
- 🧠 Wake-word based activation (e.g., "Hey Assistant!")
- 🗣️ Execute system commands:
  - Open/Close applications
  - Tell current time
  - Handle custom tasks
- 🔴 Stop assistant anytime safely
- 🚀 Animated "listening..." status in logs
- 🖼️ Profile picture display on GUI
- 🎨 Beautiful and responsive PyQt5 GUI
- 📦 Packaged into a single executable (`.exe`) for easy use

---

## 📸 Screenshots

| Main Interface | Listening Mode |
| :------------: | :-------------: |
| ![Voice Assistant GUI](assets/screenshot1.png) | ![Listening Animation](assets/screenshot2.png) |

*(Make sure to add your screenshots inside the `assets/` folder.)*

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```

### 2. Set up a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*Note: The project mainly uses PyQt5, SpeechRecognition, and pyttsx3 libraries.*

---

## 🚀 Running the Project

Simply run:

```bash
python main.py
```

---

## 🛑 Building Executable (EXE)

To create a `.exe` file from your project:

```bash
python -m PyInstaller --onefile --windowed --name "VoiceAssistant" --icon "icon.ico" main.py
```

The `.exe` file will be generated inside the `dist/` folder.

---

## 📁 Project Structure

```bash
voice-assistant/
│
├── assets/                # Images (profile picture, icons, screenshots)
├── features/
│   ├── open_close.py       # Open/close apps logic
│   ├── time_info.py        # Tell current time
│   └── custom_commands.py  # Handle custom commands
│
├── utils/
│   ├── recognizer.py       # Voice recognition utilities
│   └── speaker.py          # Text-to-speech utilities
│
├── main.py                 # Main GUI Application
├── icon.ico                # Application icon
├── profile.png             # User profile picture
├── requirements.txt        # Python dependencies
└── README.md               # README File
```

---

## 📜 Requirements

- Python 3.8 or above
- PyQt5
- SpeechRecognition
- PyAudio
- pyttsx3
- PyInstaller (for building `.exe`)

---

## 🙌 Credits

- Designed and Developed by **Arjumaan.M**.
- UI/UX enhancements by **Hadi**.

---

## 📣 Future Improvements

- Add microphone input selection
- Make wake-word customizable by user
- Add support for background noise handling
- Include weather, jokes, news fetching features 🌟

---

## 🧹 License

This project is private and belongs to the author.

