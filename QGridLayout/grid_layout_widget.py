from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton
from PySide6.QtWidgets import QSizePolicy

class GridLayoutWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout")

        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        button_3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_4 = QPushButton("Button 4")
        button_5 = QPushButton("Button 5")
        button_6 = QPushButton("Button 6")
        button_7 = QPushButton("Button 7")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1, 0, 0)
        grid_layout.addWidget(button_2, 0, 1)
        grid_layout.addWidget(button_3, 0, 2)
        grid_layout.addWidget(button_4, 1, 0)
        grid_layout.addWidget(button_5, 1, 1)
        grid_layout.addWidget(button_6, 1, 2)
        grid_layout.addWidget(button_7, 2, 0, 1, 3)

        self.setLayout(grid_layout)
