from PySide6.QtWidgets import QApplication
from qtext_edit_window import QTextEditWindow
import sys

app = QApplication(sys.argv)
widget = QTextEditWindow()
widget.show()

app.exec() 
