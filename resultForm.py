from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication

import sys

def generateResultForm(mark=0):
    app = QApplication(sys.argv)

    resultForm = QWidget()
    mark = QLabel("Твоя оцінка: " + str(mark) + " з 5")
    exitButton = QPushButton("Вихід")
    mainLayout = QVBoxLayout()

    mainLayout.addWidget(mark)
    mainLayout.addWidget(exitButton)
    resultForm.setLayout(mainLayout)

    def endProgram():
        resultForm.close()

    exitButton.clicked.connect(endProgram)
    resultForm.setStyleSheet("QWidget{font-weight: bold;}")
    resultForm.setWindowTitle("Результати вікторини")
    resultForm.show()

    app.exec_()