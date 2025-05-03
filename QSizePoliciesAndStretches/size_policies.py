from PySide6.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QLabel, QLineEdit,QPushButton,QVBoxLayout

class PoliciesWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policies")

        lable = QLabel("Some text: ")
        lineEdit = QLineEdit()

        lineEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        lable.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(lable)
        h_layout_1.addWidget(lineEdit)

        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1,2)
        h_layout_2.addWidget(button_2,1)
        h_layout_2.addWidget(button_3,1)

        v_layout  = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)