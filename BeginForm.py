from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import os
import sys

def generateBeginForm():
    app = QApplication(sys.argv)

    beginForm = QWidget()
    congratulation = QLabel("Вітаю у вікторині про пожежну безпеку!")
    beginQuizButton = QPushButton("Почати вікторину")
    mainLayout = QVBoxLayout()

    def startQuiz():
        beginForm.close()

    beginForm.setStyleSheet("QWidget{background-color: aqua; font-weight: bold;}")
    congratulation.setStyleSheet("QPushButton{background-color lightred;}")

    mainLayout.addWidget(congratulation)
    mainLayout.addWidget(beginQuizButton)
    beginQuizButton.clicked.connect(startQuiz)
    beginForm.setWindowTitle("Вікторина")
    beginForm.setLayout(mainLayout)
    try:
        beginForm.setWindowIcon( QIcon(os.getcwd()+"/pictures/logo.png") )
    except:
        pass

    beginForm.show()

    app.exec_()