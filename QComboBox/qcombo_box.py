from PySide6.QtWidgets import QPushButton, QWidget, QComboBox,QVBoxLayout

class QComboBoxWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox Demo")

        self.combo_box = QComboBox(self)
        self.setGeometry(100, 100, 300, 200)

        #Add items to the combo box
        self.combo_box.addItem("Item 1")
        self.combo_box.addItem("Item 2") 
        self.combo_box.addItem("Item 3")
        self.combo_box.addItem("Item 4")
        self.combo_box.addItem("Item 5")

        button_current_value = QPushButton("Get Current Value")
        button_current_value.clicked.connect(self.get_current_value)

        button_set_value = QPushButton("Set Value")
        button_set_value.clicked.connect(self.set_value)

        button_get_values = QPushButton("Get All Values")
        button_get_values.clicked.connect(self.get_all_values)

        #Layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_value)
        v_layout.addWidget(button_get_values)
        self.setLayout(v_layout)

    def get_current_value(self):
        current_value = self.combo_box.currentText()
        current_index = self.combo_box.currentIndex()
        print(f"Current Value: {current_value} - Index: {current_index}")
    
    def set_value(self):
        self.combo_box.setCurrentText("Item 3")
        print("Set value to Item 3")

    def get_all_values(self):
        all_values = [self.combo_box.itemText(i) for i in range(self.combo_box.count())]
        print(f"All Values: {all_values}")
