from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Window")
        self.setGeometry(100, 100, 800, 600)

        # Create a layout
        layout = QVBoxLayout()

        # Create a image  widget
        image_lable = QLabel()
        image_lable.setPixmap(QPixmap("images/car.jpg"))
        
        # Add widgets to the layout
        layout.addWidget(image_lable)

        # Set the layout for the main window
        self.setLayout(layout)