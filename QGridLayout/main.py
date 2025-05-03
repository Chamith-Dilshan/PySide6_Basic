from PySide6.QtWidgets import QApplication
from grid_layout_widget import GridLayoutWidget
import sys

app = QApplication(sys.argv)
widget = GridLayoutWidget()
widget.show()

app.exec() 
