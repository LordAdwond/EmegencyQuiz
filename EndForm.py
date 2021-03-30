from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel


def generateEndForm(forms=[]):
    endForm = QWidget()
    thank = QLabel("Було весело! Задь іще!")
    endForm.endQuizButton = QPushButton("Завершити вікторину")
    mainLayout = QVBoxLayout()

    def startQuiz():
        endForm.endQuizButton.setEnabled(False)
        for form in forms:
            form.close()
        endForm.close()

    mainLayout.addWidget(thank)
    mainLayout.addWidget(endForm.endQuizButton)
    endForm.endQuizButton.clicked.connect(startQuiz)
    endForm.setLayout(mainLayout)
    endForm.setWindowTitle("Завершити вікторину")
    endForm.setStyleSheet("QWidget{background-color: aqua; font-weight: bold;}")
    return endForm