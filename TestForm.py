from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtGui import QIcon
import os

def formTest(question="", options=["", "", ""], right=""):
    question = QLabel(question)
    answerCorrection = QLabel("")
    v1 = QRadioButton(text=options[0])
    v2 = QRadioButton(text=options[1])
    v3 = QRadioButton(text=options[2])
    form = QWidget()
    form.answer = QPushButton("Відповісти")

    mainLayout = QVBoxLayout()
    mainLayout.addWidget(question)
    mainLayout.addWidget(v1)
    mainLayout.addWidget(v2)
    mainLayout.addWidget(v3)
    mainLayout.addWidget(form.answer)
    mainLayout.addWidget(answerCorrection)


    form.trueAnswer = 0
    form.setLayout(mainLayout)

    def selectCorrectAnswer():
        rightStyleSheet = "QRadioButton{ background-color: lightgreen; font-weight: bold; color: blue; }"

        form.answer.setEnabled(False)
        v1.setEnabled(False)
        v2.setEnabled(False)
        v3.setEnabled(False)

        if( right=="1" ):
            v1.setStyleSheet(rightStyleSheet)
        elif( right=="2" ):
            v2.setStyleSheet(rightStyleSheet)
        elif( right == "3" ):
            v3.setStyleSheet(rightStyleSheet)

        if( (right=="1" and v1.isChecked()) or (right=="2" and v2.isChecked()) or (right=="3" and v3.isChecked()) ):
            answerCorrection.setText("Правильно")
            form.trueAnswer = 1
        else:
            answerCorrection.setText("Неправильно")

    form.answer.clicked.connect(selectCorrectAnswer)
    form.setWindowTitle("Питання")
    form.setStyleSheet("QWidget{font-weight: bold; background-color: yellow; color: purple;}")
    question.setStyleSheet("QLabel{color: blue; background-color: lightgreen;}")
    try:
        form.setWindowIcon( QIcon(os.getcwd()+"/pictures/logo.png") )
    except:
        pass

    return form