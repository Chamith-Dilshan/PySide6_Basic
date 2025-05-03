from PySide6.QtWidgets import QApplication
from size_policies import PoliciesWidget
import sys

app = QApplication(sys.argv)
widget = PoliciesWidget()
widget.show()

app.exec() 
