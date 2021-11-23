from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
import os
import pandas as pd
from random import randint, sample

from TestForm import TestForm


class MainForm(QWidget):
    """Class for main quiz window"""
    def __init__(self):
        """Initialize a window with quiz questions"""
        super().__init__(None)

        # main variables
        self.tests_dir = os.getcwd() + "\\" + "tests" + "\\"
        self.tests_address = os.listdir(self.tests_dir)
        self.tests_number = min(5, len(self.tests_address))
        self.main_layout = QVBoxLayout()

        self.tests_address = [self.tests_dir+address for address in self.tests_address]
        self.tests = []
        self.test_windows = []

        # tests selection
        self.tests = list(pd.Series(sample(self.tests_address, len(self.tests_address))).unique())
        if len(self.tests) > 5:
            self.tests = self.tests[:5]
        self.tests_number = len(self.tests)
        self.open_test_buttons = [QPushButton(f"Питання {i + 1}") for i in range(self.tests_number)]

        # set a basis style
        self.setStyleSheet("QWidget{background-color: aqua; font-weight: bold;}")
        self.setWindowTitle("Питання")
        try:
            self.setWindowIcon(QIcon(os.getcwd() + "/pictures/logo.png"))
        except:
            pass

        # tests generation
        for test in self.tests:
            with open(test, "r", encoding="utf-8") as test_datafile:
                test_info = test_datafile.readlines()
                test_window = TestForm(test_info[0], test_info[1:4], test_info[4])
                self.test_windows.append(test_window)

        # set connections
        for i in range(self.tests_number):
            self.open_test_buttons[i].clicked.connect(self.test_windows[i].show)

        # set window organization
        for button in self.open_test_buttons:
            self.main_layout.addWidget(button)
        self.setLayout(self.main_layout)
