from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtCore import QFile

def formTest(question="", options=["", "", ""], right=""):
    question = QLabel(question)
    answerCorrection = QLabel("")
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
    mainLayout.addWidget(answerCorrection)

    form = QWidget()
    form.trueAnswer = 0
    form.setLayout(mainLayout)

    def selectCorrectAnswer():
        rightStyleSheet = "QRadioButton{ background-color: lightgreen; font-weight: bold; color: blue; }"

        answer.setEnabled(False)
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
            #file = QFile("result.dat")
            #file.open(QFile.WriteOnly)
            #file.write("1")
            #file.close()
            form.trueAnswer = 1
        else:
            answerCorrection.setText("Неправильно")

    answer.clicked.connect(selectCorrectAnswer)
    form.setWindowTitle("Питання")
    form.setStyleSheet("QWidget{font-weight: bold; background-color: yellow; color: purple;}")
    question.setStyleSheet("QLabel{color: blue; background-color: lightgreen;}")
    return form