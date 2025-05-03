from PySide6.QtWidgets import QApplication
from qline_edit import QlineWindow
import sys

app = QApplication(sys.argv)
widget = QlineWindow()
widget.show()

app.exec() 
