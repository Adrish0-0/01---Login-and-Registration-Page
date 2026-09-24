import sys

from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont

class LoginRegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PASSWORD VAULT")
        self.setFixedSize(1200, 800)
        self.setObjectName("MAINWINDOW")
        self.setContentsMargins(120, 80, 120, 80)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.login_widget = QWidget(self)
        self.login_widget.setFixedWidth(480)
        self.login_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
                border-bottom-left-radius: 20px;
            }
        """)
        self.setup_login_ui()
        
        self.register_widget = QWidget(self)
        self.register_widget.setFixedWidth(480)
        self.register_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border-top-left-radius: 0px;
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;
                border-bottom-left-radius: 0px;
            }
        """)
        self.setup_register_ui()

        main_layout.addWidget(self.login_widget)
        main_layout.addWidget(self.register_widget)

        self.overlay = QWidget(self)
        self.overlay.resize(480, 640)
        self.overlay.move(600, 80)
        self.overlay.setStyleSheet("""
            QWidget {
                background-color: #f73636;
                border-radius: 20px;
            }
        """)

        self.overlay_layout = QVBoxLayout(self.overlay)
        self.overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.overlay_text = QLabel("WELCOME!", self.overlay)
        self.overlay_text.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.overlay_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overlay_text.setStyleSheet("""
            QLabel {
                color: white;
            }
        """)

        self.overlay_button = QPushButton("Go to Registration", self.overlay)
        self.overlay_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid white;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: white;
                color: #dc2626;
            }
        """)
        self.overlay_button.clicked.connect(self.animate_overlay)


        self.overlay_layout.addWidget(self.overlay_text)
        self.overlay_layout.addSpacing(20)
        self.overlay_layout.addWidget(self.overlay_button)

        self.animation = QPropertyAnimation(self.overlay, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.current_state = "login"

    def setup_login_ui(self):
        layout = QVBoxLayout(self.login_widget)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("SIGN IN")
        title.setStyleSheet("""
            QLabel {
                color: #333333;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)

        self.login_username = QLineEdit()
        self.login_username.setPlaceholderText("Username")
        self.login_username.setStyleSheet("""
            QLineEdit {
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-bottom: 20px;
            }
        """)

        self.login_password = QLineEdit()
        self.login_password.setPlaceholderText("Password")
        self.login_password.setStyleSheet("""
            QLineEdit {
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-bottom: 20px;
            }
        """)

        submit = QPushButton("LOGIN")
        submit.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: white;
                border-radius: 20px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(self.login_username)
        layout.addWidget(self.login_password)
        layout.addWidget(submit)

    def setup_register_ui(self):
        layout = QVBoxLayout(self.register_widget)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("REGISTER")
        title.setStyleSheet("""
            QLabel {
                color: #333333;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)

        self.register_username = QLineEdit()
        self.register_username.setPlaceholderText("Username")
        self.register_username.setStyleSheet("""
            QLineEdit {
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-bottom: 20px;
            }
        """)

        self.register_password = QLineEdit()
        self.register_password.setPlaceholderText("Password")
        self.register_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_password.setStyleSheet("""
            QLineEdit {
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                margin-bottom: 20px;
            }
        """)

        submit = QPushButton("REGISTER")
        submit.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: white;
                border-radius: 20px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(self.register_username)
        layout.addWidget(self.register_password)
        layout.addWidget(submit)

    def animate_overlay(self):
        if self.animation.state() == QPropertyAnimation.State.Running:
            return

        if self.current_state == "login":
            self.animation.setStartValue(QRect(600, 80, 480, 640))
            self.animation.setEndValue(QRect(120, 80, 480, 640))
            self.overlay_text.setText("HELLO!")
            self.overlay_button.setText("Go to Login")
            self.current_state = "registration"
        else:
            self.animation.setStartValue(QRect(120, 80, 480, 640))
            self.animation.setEndValue(QRect(600, 80, 480, 640))
            self.overlay_text.setText("WELCOME!")
            self.overlay_button.setText("Go to Registration")
            self.current_state = "login"

        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginRegistrationWindow()
    window.show()
    sys.exit(app.exec())
