from PySide6.QtWidgets import QGroupBox, QWidget, QCheckBox, QButtonGroup, QHBoxLayout,QRadioButton,QVBoxLayout

class CheckBoxRadioButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButton Example")

        #Checkboxses : Operating Systems
        os = QGroupBox("Operating Systems")

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.Windows_box_toggled)
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.Linux_box_toggled)
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.Mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        #Exclusive Checkboxses : Drinks
        drink = QGroupBox("Drinks")

        wine = QCheckBox("Wine")
        wine.setChecked(True)
        wine.toggled.connect(self.Wine_box_toggled)
        beer = QCheckBox("Beer")
        beer.toggled.connect(self.Beer_box_toggled)
        coffee = QCheckBox("Coffee")
        coffee.toggled.connect(self.Coffee_box_toggled)

        #Loggicaly make it a set of button to make it exclusive
        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(wine)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(wine)
        drink_layout.addWidget(beer)
        drink_layout.addWidget(coffee)
        drink.setLayout(drink_layout)

        #Radio buttons : answers
        answers = QGroupBox("Answers")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)

        # Adding the checkboxes to the main horizontal layout
        layout = QHBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drink)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addWidget(answers)
        self.setLayout(main_layout)

    def Windows_box_toggled(self, checked: bool):
        if checked:
            print("Windows is selected")
        else:
            print("Windows is deselected")
    
    def Linux_box_toggled(self, checked: bool):
        if checked:
            print("Linux is selected")
        else:
            print("Linux is deselected")

    def Mac_box_toggled(self, checked: bool):
        if checked:
            print("Mac is selected")
        else:
            print("Mac is deselected")
    
    def Wine_box_toggled(self, checked: bool):
        if checked:
            print("Wine is selected")
        else:
            print("Wine is deselected")
    
    def Beer_box_toggled(self, checked: bool):
        if checked:
            print("Beer is selected")
        else:
            print("Beer is deselected")
    
    def Coffee_box_toggled(self, checked: bool):
        if checked:
            print("Coffee is selected")
        else:
            print("Coffee is deselected")


