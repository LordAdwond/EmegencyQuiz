from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import  QRadioButton

def formTest(question="", options=["", "", ""], right=""):
    question = QLabel(question)
    result = QLabel("")
    v1 = QRadioButton(text=options[0])
    v2 = QRadioButton(text=options[1])
    v3 = QRadioButton(text=options[2])
    answer = QPushButton("Відповісти")

    mainLayout = QVBoxLayout()
    mainLayout.addWidget(question)
    mainLayout.addWidget(v1)
    mainLayout.addWidget(v2)
    mainLayout.addWidget(v3)
    mainLayout.addWidget(answer)
    mainLayout.addWidget(result)

    form = QWidget()
    form.setLayout(mainLayout)

    def selectCorrectAnswer():
        if( right == "1" ):
            if( v1.isChecked() ):
                result.setText("Правильно")
            else:
                result.setText("Неправильно")
        elif (right == "2"):
            if (v2.isChecked()):
                result.setText("Правильно")
            else:
                result.setText("Неправильно")
        elif (right == "3"):
            if (v2.isChecked()):
                result.setText("Правильно")
            else:
                result.setText("Неправильно")

    answer.clicked.connect(selectCorrectAnswer)
    return form