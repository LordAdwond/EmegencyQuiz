from PyQt5.QtWidgets import QApplication
import sys, os
from random import sample
from TestForm import *
from EndForm import *
from resultForm import *
from PyQt5.QtCore import QFile

def generateForm():
    app = QApplication(sys.argv)

    testDir = os.getcwd() + "/tests/"
    testsData = os.listdir(testDir)
    tests = sample(testsData, min(len(testsData), 5))
    testForms = []

    for test in tests:
        testFile = open(testDir + test, "r", encoding='utf-8')
        lines = testFile.readlines()
        testForms.append(formTest(lines[0], lines[1:4], lines[4]))

    testForms.append(generateEndForm(testForms))
    for test in testForms:
        test.show()

    app.exec_()

    app1 = QApplication(sys.argv)

    mark = sum([testForms[0].trueAnswer, testForms[1].trueAnswer, testForms[2].trueAnswer, testForms[3].trueAnswer,
                testForms[4].trueAnswer])
    generateResultForm(mark)

    app1.exec_()