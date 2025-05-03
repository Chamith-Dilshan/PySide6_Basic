from PySide6.QtWidgets import QHBoxLayout, QTextEdit, QVBoxLayout, QWidget, QPushButton

class QTextEditWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit Example")
        self.resize(400, 300)

        # Create a QTextEdit widget
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Type something here...")

        #Buttons
        current_text_button = QPushButton("currentText")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        copy_button = QPushButton("copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("paste")
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton("undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("setPlainText")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("setHtml")
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("clear")
        clear_button.clicked.connect(self.text_edit.clear)

        # Set the layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(h_layout)
        main_layout.addWidget(self.text_edit)
        self.setLayout(main_layout)

    def current_text_button_clicked(self):
        current_text = self.text_edit.toPlainText()
        print(f"Current text: {current_text}")

    def set_plain_text(self):
        self.text_edit.setPlainText("This is plain text.")

    def set_html(self):
        self.text_edit.setHtml("<h1>This is HTML text.</h1>")
    


