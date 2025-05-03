from PySide6.QtWidgets import QPushButton, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel

class QlineWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit Example")
        self.setGeometry(100, 100, 300, 100)

        # QLabel
        qlable = QLabel("Enter text: ")
        # QLineEdit
        self.qLineEdit = QLineEdit()
        #self.qLineEdit.textChanged.connect(self.text_changed)
        #self.qLineEdit.cursorPositionChanged.connect(self.cursor_position_changed)
        #self.qLineEdit.editingFinished.connect(self.editing_finished)
        #self.qLineEdit.returnPressed.connect(self.returned_pressed)
        #self.qLineEdit.selectionChanged.connect(self.selection_changed)
        self.qLineEdit.textEdited.connect(self.text_edited)

        # Horizontal layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(qlable)
        h_layout.addWidget(self.qLineEdit)

        # Button
        button = QPushButton("Submit")
        button.clicked.connect(self.button_clicked)

        # Result
        self.result_lable = QLabel("Result:")

        # Vertical layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.result_lable)

        self.setLayout(v_layout)
    
    # Slots
    def button_clicked(self):
        print("Button clicked!")
        print("text: ", self.qLineEdit.text()) 
        self.result_lable.setText("Result: " + self.qLineEdit.text())
    
    def text_changed(self):
        self.result_lable.setText(self.qLineEdit.text())

    def cursor_position_changed(self, old:str, new:str):
        print("Cursor position changed from", old, "to", new)
        self.result_lable.setText(self.qLineEdit.text())

    def editing_finished(self):
        print("Editing Finished")

    def returned_pressed(self):
        print("Return Pressed")

    def selection_changed(self):
        print("Selection Changed: ", self.qLineEdit.selectedText())

    def text_edited(self, new_text: str) -> None:
        print("Text Edited. New Text: ", new_text)





