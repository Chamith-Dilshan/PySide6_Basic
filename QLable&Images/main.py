from PySide6.QtWidgets import QApplication
from image_window import ImageWindow
import sys

app = QApplication(sys.argv)
widget = ImageWindow()
widget.show()

app.exec() 
