from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import  QRadioButton
from PyQt5.QtWidgets import QApplication
import sys, os
from random import sample
from TestForm import *

def generateForm():
    app = QApplication(sys.argv)

    testDir = os.getcwd() + "/tests/"
    testsData = os.listdir(testDir)
    tests = sample(testsData, min(len(testsData), 5))
    testForms = []
    for test in tests:
        testFile = open(testDir + test, "r", encoding='utf-8')
        lines = testFile.readlines()
        testForms.append(formTest(lines[0], lines[1:4], lines[4]))

    for test in testForms:
        test.show()

    app.exec_()