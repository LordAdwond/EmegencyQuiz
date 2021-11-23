from BeginForm import BeginForm
from PyQt5.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)
quiz = BeginForm()
quiz.show()
app.exec_()
