from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon
import os, sys

from MainForm import MainForm
from MarkForm import MarkForm


class BeginForm(QWidget):
    """Class for begin window"""
    def __init__(self):
        """Initialize begin window"""
        super().__init__(None)

        # set main variables
        self.main_layout = QVBoxLayout()
        self.congrat_label = QLabel("Вітаю у вікторині про пожежну безпеку!")
        self.begin_quiz_button = QPushButton("Почати вікторину")
        self.end_quiz_button = QPushButton("Закінчити вікторину")
        self.quiz_window = MainForm()

        # set a basis style
        self.setStyleSheet("QWidget{background-color: aqua; font-weight: bold;}")
        self.congrat_label.setStyleSheet("QPushButton{background-color lightred;}")
        self.setWindowTitle("Вікторина")
        try:
            self.setWindowIcon(QIcon(os.getcwd() + "/pictures/logo.png"))
        except:
            pass

        # set connections
        self.begin_quiz_button.clicked.connect(self.start_quiz)
        self.end_quiz_button.clicked.connect(self.end_quiz)

        # window organization
        self.main_layout.addWidget(self.congrat_label)
        self.main_layout.addWidget(self.begin_quiz_button)
        self.main_layout.addWidget(self.end_quiz_button)
        self.setLayout(self.main_layout)

    def start_quiz(self):
        """To start a quiz"""
        self.quiz_window.show()

    def end_quiz(self):
        """To finish quiz and show quiz result"""
        self.quiz_window.close()
        tests = self.quiz_window.test_windows.copy()
        mark_window = MarkForm(tests)
        mark_window.exec_()

        del self.quiz_window
        self.quiz_window = MainForm()
