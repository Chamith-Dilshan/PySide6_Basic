from PySide6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout,QTabWidget,QVBoxLayout

class QTabWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Demo")

        tab_widget = QTabWidget(self)

        #Information Tab
        widget_form = QWidget()
        lable_full_name  = QLabel("Full Name:")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(lable_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

        #Buttons Tab
        widget_buttons = QWidget()
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.on_button1_clicked)
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        widget_buttons.setLayout(button_layout)

        #Add tabs to widget
        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def on_button1_clicked(self):
        print("Button 1 clicked")