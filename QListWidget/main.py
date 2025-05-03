from PySide6.QtWidgets import QApplication
from qlist_widget import QListWidgetDemo
import sys

app = QApplication(sys.argv)
widget = QListWidgetDemo()
widget.show()

app.exec() 
