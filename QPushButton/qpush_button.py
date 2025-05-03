from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

class PushButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Push Button Example")
        self.resize(300, 200)

        # Create a button
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_button_click)
        self.button.pressed.connect(self.button_pressed)
        self.button.released.connect(self.buttonrelesed)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        print("Button clicked!")
    
    def button_pressed(self):
        print("Button pressed!")
    
    def buttonrelesed(self):
        print("Button released!")