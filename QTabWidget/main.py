from PySide6.QtWidgets import QApplication
from qtab_widget import QTabWidgetDemo
import sys

app = QApplication(sys.argv)
widget = QTabWidgetDemo()
widget.show()

app.exec() 
