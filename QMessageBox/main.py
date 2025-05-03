from PySide6.QtWidgets import QApplication
from qmesasge_widget import MessageWidget
import sys

app = QApplication(sys.argv)
widget = MessageWidget()
widget.show()

app.exec() 
