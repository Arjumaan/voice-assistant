# Import necessary modules and libraries
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread

# Import custom utility and feature modules
from utils.recognizer import listen_for_wake_word, get_command
from utils.speaker import speak
from features.open_close import open_software, close_software
from features.time_info import tell_time
from features.custom_commands import handle_custom_commands

# Define the main application class for the Voice Assistant
class VoiceAssistantApp(QWidget):
    # Signal to log messages in the UI
    log_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # Set window flags and initialize the UI
        self.setWindowFlags(Qt.Window)
        self.init_ui()
        # Connect the log signal to the log method
        self.log_signal.connect(self.log)

    # Initialize the user interface
    def init_ui(self):
        # Set window properties
        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("🧠 Voice Assistant")
        self.setGeometry(300, 200, 600, 450)
        self.setStyleSheet("background-color: #1e1e2f;")

        # Set the color palette for the window
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor("white"))
        self.setPalette(palette)

        # Add a profile picture
        self.profile_pic = QLabel(self)
        pixmap = QPixmap("profile.png")  # Ensure the file matches the name
        self.profile_pic.setPixmap(pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.profile_pic.setAlignment(Qt.AlignCenter)

        # Add a title label
        self.title = QLabel("🧠 Voice Assistant")
        self.title.setFont(QFont("Arial", 18, QFont.Bold))
        self.title.setStyleSheet("color: #f5f5f5;")
        self.title.setAlignment(Qt.AlignCenter)

        # Add a log box for displaying messages
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setStyleSheet(
            "background-color: #2e2e3d; color: white; "
            "border: 1px solid #444; border-radius: 8px;"
        )

        # Add Start and Stop buttons
        self.start_btn = QPushButton("Start 🎙️")
        self.start_btn.setFont(QFont("Arial", 14))
        self.start_btn.setStyleSheet("background-color: #5b78f6; color: white; border-radius: 10px; padding: 10px;")
        self.start_btn.clicked.connect(self.start_listening)

        self.stop_btn = QPushButton("Stop 🔇")
        self.stop_btn.setFont(QFont("Arial", 14))
        self.stop_btn.setStyleSheet("background-color: #f65b5b; color: white; border-radius: 10px; padding: 10px;")
        self.stop_btn.clicked.connect(self.stop_listening)
        self.stop_btn.setEnabled(False)

        # Arrange buttons in a horizontal layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)

        # Arrange all elements in a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.profile_pic)
        layout.addWidget(self.title)
        layout.addWidget(self.log_box)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    # Method to log messages in the log box
    def log(self, message):
        self.log_box.append(f"→ {message}")

    # Start listening for commands
    def start_listening(self):
        self.log("🎙️ Voice Assistant Initialized. Say your wake word to wake me up!")
        self.thread = CommandThread(self)  # Create a new thread for listening
        self.thread.start()
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

    # Stop listening for commands
    def stop_listening(self):
        if hasattr(self, 'thread') and self.thread.isRunning():
            self.thread.terminate()  # Terminate the thread
        self.log("🔇 Assistant stopped by user.")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        # Optionally clear logs if needed
        # self.log_box.clear()

# Define a thread class for handling voice commands
class CommandThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    # Run method for the thread
    def run(self):
        try:
            self.parent.log_signal.emit("Listening for Wake Word...")
            if listen_for_wake_word():  # Wait for the wake word
                self.parent.log_signal.emit("✅ Wake Word detected!")
                while True:
                    cmd = get_command()  # Get the user's command
                    if cmd:
                        self.parent.log_signal.emit(f"🗣️ Command received: \"{cmd}\"")
                        if 'stop' in cmd:
                            speak('Stopping. Goodbye!')
                            self.parent.log_signal.emit("🔴 Assistant shutting down...")
                            QTimer.singleShot(500, self.parent.close)  # Close the app after a delay
                            break
                        elif 'open' in cmd:
                            app_name = cmd.replace('open', '').strip()
                            self.parent.log_signal.emit(f"📂 Opening: {app_name}")
                            open_software(app_name)  # Open the specified software
                        elif 'close' in cmd:
                            app_name = cmd.replace('close', '').strip()
                            self.parent.log_signal.emit(f"📁 Closing: {app_name}")
                            close_software(app_name)  # Close the specified software
                        elif 'time' in cmd:
                            self.parent.log_signal.emit("🕒 Telling the current time...")
                            tell_time()  # Provide the current time
                        else:
                            self.parent.log_signal.emit(f"⚡ Executing custom command: {cmd}")
                            handle_custom_commands(cmd)  # Handle other custom commands
                    else:
                        self.parent.log_signal.emit("🤔 Didn't catch that.")
        except Exception as e:
            self.parent.log_signal.emit(f"❌ Error: {e}")

# Main entry point of the application
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application
    gui = VoiceAssistantApp()  # Create the main window
    gui.show()  # Show the main window
    sys.exit(app.exec_())  # Execute the application
