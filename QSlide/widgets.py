from PySide6.QtWidgets import QMainWindow, QPushButton,QSlider
from PySide6.QtCore import Qt

#sub class
class MyButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        button = QPushButton("Click Me")
        button.setCheckable(True)
        button.clicked.connect(lambda: self.button_clicked(button))
        self.setCentralWidget(button)
    
    def button_clicked(self, button: QPushButton): 
        if button.isChecked():
            print("Button is checked!")
        else:
            print("Button is unchecked!")
        # This function is called when the button is clicked
        print("Button clicked!")

#sub class 
class MySlider(QSlider):
    def __init__(self, orientation: Qt.Orientation):
        super().__init__(orientation)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(50)
        self.valueChanged.connect(lambda: self.slider_changed(self.value()))

    def value(self):
        # Override the value method to return a int value
        return super().value()

    def slider_changed(self, data: int):
        # This function is called when the slider value changes
        print(f"Slider value changed: {data}")