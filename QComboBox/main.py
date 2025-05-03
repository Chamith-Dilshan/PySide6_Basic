from PySide6.QtWidgets import QApplication
from qcombo_box import QComboBoxWidgetDemo
import sys

app = QApplication(sys.argv)
widget = QComboBoxWidgetDemo()
widget.show()

app.exec() 
