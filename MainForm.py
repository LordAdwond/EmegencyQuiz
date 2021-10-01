from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import sys, os
from random import sample
from random import randint

from TestForm import *

def generateForm():
    mark = 0

    app = QApplication(sys.argv)

    # tests data
    testDir = os.getcwd() + "/tests/" # directory with tests
    testsData = os.listdir(testDir) # list of tests

    testsNumbers = []
    while(len(testsNumbers)<min(len(testsData), 5)):
        num = randint(0, len(testsData)-1)
        if(num not in testsNumbers):
            testsNumbers.append(num)

    tests = [ testsData[num] for num in testsNumbers ] # test selection
    testForms = [] # list for test forms

    # variables for form
    mainForm = QWidget()
    mainLayout = QVBoxLayout()
    mainLabel = QLabel("Виберіть питання")
    buttons = [ QPushButton("Питання "+str(i)) for i in range(1, len(tests)+1) ]

    # making of test forms
    for test in tests:
        testFile = open(testDir + test, "r", encoding='utf-8')
        lines = testFile.readlines()
        testForms.append(formTest(lines[0], lines[1:4], lines[4]))

    # forming of main form and connecting of components
    mainLayout.addWidget(mainLabel)
    for button in buttons:
        mainLayout.addWidget(button)

    try:
        buttons[0].clicked.connect(lambda: testForms[0].show())
    except:
        pass
    try:
        buttons[1].clicked.connect(lambda: testForms[1].show())
    except:
        pass
    try:
        buttons[2].clicked.connect(lambda: testForms[2].show())
    except:
        pass
    try:
        buttons[3].clicked.connect(lambda: testForms[3].show())
    except:
        pass
    try:
        buttons[4].clicked.connect(lambda: testForms[4].show())
    except:
        pass

    mainForm.setLayout(mainLayout)
    mainForm.setStyleSheet("QWidget{font-weight: bold;}")
    try:
        mainForm.setWindowIcon( QIcon(os.getcwd()+"/pictures/logo.png") )
    except:
        pass
    mainForm.setWindowTitle("Питання")
    mainForm.setGeometry(300, 300, 350, 100)
    mainForm.show()

    if(mainForm.isVisible()):
        app.exec_()
    else:
        app.exit(0)


    exit_app = QApplication(sys.argv)
    mark = sum([testForms[0].trueAnswer, testForms[1].trueAnswer, testForms[2].trueAnswer, testForms[3].trueAnswer,
                testForms[4].trueAnswer])

    messBoxIcon = QIcon(os.getcwd() + "/pictures/logo.png")
    resultWidget = QWidget()
    mainLayout = QVBoxLayout()
    markLabel = QLabel("Твоя оцінка: {}".format(mark))
    exitButton = QPushButton("Вийти")

    exitButton.clicked.connect(lambda: exit(0))
    mainLayout.addWidget(markLabel)
    mainLayout.addWidget(exitButton)
    resultWidget.setLayout(mainLayout)

    resultWidget.setWindowTitle("Результат")
    resultWidget.setWindowIcon(messBoxIcon)

    resultWidget.show()
    exit_app.exec_()