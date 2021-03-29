from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel


def generateEndForm(forms=[]):
    endForm = QWidget()
    thank = QLabel("Було весело! Задь іще!")
    endQuizButton = QPushButton("Завершити вікторину")
    mainLayout = QVBoxLayout()

    def startQuiz():
        for form in forms:
            form.close()
        endForm.close()

    mainLayout.addWidget(thank)
    mainLayout.addWidget(endQuizButton)
    endQuizButton.clicked.connect(startQuiz)
    endForm.setLayout(mainLayout)

    return endForm