from PySide6.QtWidgets import QApplication
from qcheckbox_radiobutton import CheckBoxRadioButtonWidget
import sys

app = QApplication(sys.argv)
widget = CheckBoxRadioButtonWidget()
widget.show()

app.exec() 
