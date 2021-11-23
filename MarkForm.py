from TestForm import TestForm
from PyQt5.QtWidgets import QMessageBox


class MarkForm(QMessageBox):
    """Class for mark window"""
    def __init__(self, tests : list[TestForm]):
        """Initialize a mark window"""
        super().__init__(None)

        self.general_mark = sum([ test.mark for test in tests ])
        self.setText(f"Набрано {self.general_mark} балів з 5 можливих")
        self.setWindowTitle("Результат вікторини")
