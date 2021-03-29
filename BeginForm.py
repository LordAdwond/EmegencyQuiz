from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
import sys

def generateBeginForm():
    app = QApplication(sys.argv)

    beginForm = QWidget()
    congratulation = QLabel("Вітаю у вікторині про пожежну безпеку!")
    beginQuizButton = QPushButton("Почати вікторину")
    mainLayout = QVBoxLayout()
    congratulationStyleSheet = "QLabel{font-size: 250%; font-weight: bold; color: purple;}"

    def startQuiz():
        beginForm.close()

    mainLayout.addWidget(congratulation)
    mainLayout.addWidget(beginQuizButton)
    beginQuizButton.clicked.connect(startQuiz)
    congratulation.setStyleSheet(congratulationStyleSheet)
    beginForm.setWindowTitle("Вікторина")
    beginForm.setLayout(mainLayout)
    beginForm.show()

    app.exec_()