import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread

from utils.recognizer import listen_for_wake_word, get_command
from utils.speaker    import speak
from features.open_close import open_software, close_software
from features.time_info  import tell_time
from features.custom_commands import handle_custom_commands

class VoiceAssistantApp(QWidget):
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # no frameless window for now, you can remove these flags if you want titlebar
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.init_ui()
        self.log_signal.connect(self.log)

    def init_ui(self):
        # pick up the icon right beside main.py
        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("🧠 Voice Assistant")
        self.setGeometry(300, 200, 600, 400)
        self.setStyleSheet("background-color: #1e1e2f;")

        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor("white"))
        self.setPalette(palette)

        self.title = QLabel("🧠 Voice Assistant")
        self.title.setFont(QFont("Arial", 18, QFont.Bold))
        self.title.setStyleSheet("color: #f5f5f5;")
        self.title.setAlignment(Qt.AlignCenter)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setStyleSheet(
            "background-color: #2e2e3d; color: white; "
            "border: 1px solid #444; border-radius: 8px;"
        )

        self.start_btn = QPushButton("Start Listening 🎙️")
        self.start_btn.setFont(QFont("Arial", 14))
        self.start_btn.setStyleSheet(
            "background-color: #5b78f6; color: white; "
            "border: none; padding: 10px; border-radius: 10px;"
        )
        self.start_btn.clicked.connect(self.start_listening)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.log_box)
        layout.addWidget(self.start_btn)
        self.setLayout(layout)

    def log(self, message):
        self.log_box.append(f"→ {message}")

    def start_listening(self):
        # fire up the background thread
        self.log("Voice Assistant Initialized. Say your wake word to wake me up!")
        t = CommandThread(self)
        t.start()

class CommandThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        try:
            self.parent.log_signal.emit("Voice Assistant Activated")
            if listen_for_wake_word():
                self.parent.log_signal.emit("Wake word detected.")
                while True:
                    cmd = get_command()
                    if cmd:
                        self.parent.log_signal.emit(f"Command: {cmd}")
                        if 'stop' in cmd:
                            speak('Stopping. Goodbye!')
                            self.parent.log_signal.emit("Assistant stopped.")
                            QTimer.singleShot(500, self.parent.close)
                            break
                        elif 'open' in cmd:
                            open_software(cmd.replace('open','').strip())
                        elif 'close' in cmd:
                            close_software(cmd.replace('close','').strip())
                        elif 'time' in cmd:
                            tell_time()
                        else:
                            handle_custom_commands(cmd)
                    else:
                        self.parent.log_signal.emit("Didn't catch that.")
        except Exception as e:
            self.parent.log_signal.emit(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = VoiceAssistantApp()
    gui.show()
    sys.exit(app.exec_())
