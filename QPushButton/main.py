from PySide6.QtWidgets import QApplication
from qpush_button import PushButtonWindow
import sys

app = QApplication(sys.argv)
widget = PushButtonWindow()
widget.show()

app.exec() 
