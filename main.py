import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QFont, QColor, QTextCharFormat, QTextCursor
from utils.recognizer import listen_for_wake_word, get_command
from utils.speaker import speak
from features.open_close import open_software, close_software
from features.time_info import tell_time
from features.custom_commands import handle_custom_commands

class AssistantThread(QThread):
    update_text = pyqtSignal(str, str)  # message, type (info, success, error)

    def run(self):
        speak("Voice Assistant Initialized. Say 'Jarvis' to wake me up!")
        self.update_text.emit("Voice Assistant Initialized. Say 'Jarvis' to wake me up!", "info")
        while True:
            if listen_for_wake_word():
                self.update_text.emit("Wake word detected!", "success")
                while True:
                    command = get_command()
                    if command:
                        if 'stop' in command:
                            self.update_text.emit("Stopping the program. Goodbye!", "info")
                            speak('Stopping the program. Goodbye!')
                            sys.exit()
                        elif 'open' in command:
                            software = command.replace('open', '').strip()
                            open_software(software)
                            self.update_text.emit(f"Opening {software}...", "success")
                        elif 'close' in command:
                            software = command.replace('close', '').strip()
                            close_software(software)
                            self.update_text.emit(f"Closing {software}...", "success")
                        elif 'time' in command:
                            tell_time()
                        else:
                            handle_custom_commands(command)
                            self.update_text.emit(f"Executed: {command}", "info")

class VoiceAssistantApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Assistant - Jarvis")
        self.setGeometry(200, 150, 600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Segoe UI;
            }
            QPushButton {
                background-color: #2d89ef;
                border: none;
                padding: 10px;
                font-size: 14px;
                border-radius: 8px;
                color: white;
            }
            QPushButton:hover {
                background-color: #1b5fbd;
            }
            QTextEdit {
                background-color: #2d2d30;
                color: white;
                border: 1px solid #444;
                border-radius: 8px;
                padding: 8px;
                font-size: 13px;
            }
        """)

        layout = QVBoxLayout()
        self.label = QLabel("👋 Voice Assistant is Ready")
        self.label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        self.start_button = QPushButton("▶️ Start Assistant")
        self.start_button.clicked.connect(self.start_assistant)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("⏹️ Stop Assistant")
        self.stop_button.clicked.connect(self.stop_assistant)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

        self.assistant_thread = AssistantThread()
        self.assistant_thread.update_text.connect(self.display_message)

    def start_assistant(self):
        self.assistant_thread.start()
        self.display_message("Voice Assistant Started...", "info")

    def stop_assistant(self):
        self.assistant_thread.terminate()
        self.display_message("Voice Assistant Stopped.", "error")

    def display_message(self, message, msg_type="info"):
        fmt = QTextCharFormat()
        if msg_type == "info":
            fmt.setForeground(QColor("white"))
        elif msg_type == "success":
            fmt.setForeground(QColor("#00ff7f"))
        elif msg_type == "error":
            fmt.setForeground(QColor("#ff4c4c"))

        self.text_area.moveCursor(QTextCursor.End)
        self.text_area.setCurrentCharFormat(fmt)
        self.text_area.insertPlainText(f"{message}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    assistant_app = VoiceAssistantApp()
    assistant_app.show()
    sys.exit(app.exec_())
