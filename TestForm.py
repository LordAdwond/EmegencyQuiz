from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import os

class TestForm(QWidget):
    """Class for test window"""
    def __init__(self, question="", options=["", "", ""], right=""):
        """Initialize a quiz question window"""
        super().__init__(None)

        # main variables
        self.question_label = QLabel(question)
        self.variants_group = QGroupBox("Варіанти")
        self.v1 = QRadioButton(text=f"а) {options[0]}")
        self.v2 = QRadioButton(text=f"б) {options[1]}")
        self.v3 = QRadioButton(text=f"в) {options[2]}")
        self.send_answer_button = QPushButton("Відповісти")
        self.is_answer_correct_label = QLabel("")
        self.answer_variants_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.right_answer = right
        self.mark = 0

        # set window organization
        self.answer_variants_layout.addWidget(self.v1)
        self.answer_variants_layout.addWidget(self.v2)
        self.answer_variants_layout.addWidget(self.v3)
        self.variants_group.setLayout(self.answer_variants_layout)
        self.main_layout.addWidget(self.question_label)
        self.main_layout.addWidget(self.variants_group)
        self.main_layout.addWidget(self.is_answer_correct_label)
        self.main_layout.addWidget(self.send_answer_button)
        self.setLayout(self.main_layout)

        # set a basis style
        self.setStyleSheet("QWidget{background-color: aqua; font-weight: bold;}")
        self.setWindowTitle("Питання")
        try:
            self.setWindowIcon(QIcon(os.getcwd() + "/pictures/logo.png"))
        except:
            pass

        # set connections
        self.send_answer_button.clicked.connect(lambda : self.check_answer())

    def check_answer(self):
        """To check is answer correct"""

        # make a message
        is_correct_message = QMessageBox()
        message = ""

        # unlock all buttons
        self.v1.setDisabled(True)
        self.v2.setDisabled(True)
        self.v3.setDisabled(True)
        self.send_answer_button.setDisabled(True)

        # answer check
        if((self.right_answer=="1" and self.v1.isChecked()) or (self.right_answer=="2" and self.v2.isChecked()) or (self.right_answer=="3" and self.v3.isChecked())):
            message = "Правильно"
            self.mark = 1
        else:
            message = "Неправильно\nПравильна відповідь: "
            if self.right_answer == "1":
                message += "а)"
            elif self.right_answer == "2":
                message += "б)"
            elif self.right_answer == "3":
                message += "в)"

        # show a result of answer
        self.is_answer_correct_label.setText(message)
        is_correct_message.setText(message)
        is_correct_message.exec_()
