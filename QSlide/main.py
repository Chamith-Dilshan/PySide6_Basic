from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
import sys

from widgets import MyButton
from widgets import MySlider

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
layout = QVBoxLayout()

# Add MyButton widget
button = MyButton()
layout.addWidget(button)

slider = MySlider(Qt.Orientation.Horizontal)
layout.addWidget(slider)

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
app.exec()