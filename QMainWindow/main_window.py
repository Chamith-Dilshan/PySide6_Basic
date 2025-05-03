from PySide6.QtWidgets import  QMainWindow, QToolBar, QStatusBar, QPushButton,QApplication
from PySide6.QtGui import QAction,QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app # Store the app instance in the window
        self.setWindowTitle("Main Window")

        #Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("&Exit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("&Undo")
        edit_menu.addAction("&Redo")
        edit_menu.addSeparator()
        edit_menu.addAction("&Copy")
        edit_menu.addAction("&Paste")
        edit_menu.addAction("&Cut")

        menu_bar.addMenu("&Window")
        menu_bar.addMenu("&Setting")
        menu_bar.addMenu("&Help")

        #Tool bar
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)

        tool_bar.addAction(quit_action)

        action1 = QAction("Action 1", self)
        action1.setStatusTip("This is action 1")
        action1.triggered.connect(self.action1_triggered)
        tool_bar.addAction(action1)

        action2 = QAction(QIcon("play_Img.png"),"Action 2", self)
        action2.setStatusTip("This is action 2")
        action2.triggered.connect(self.action2_triggered)
        tool_bar.addAction(action2)

        tool_bar.addSeparator()
        tool_bar.addWidget(QPushButton("Push Button"))

        #Status bar
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button 1")
        button1.setStatusTip("This is button 1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


    def quit_app(self):
        self.app.quit()

    def action1_triggered(self):
        print("Action 1 triggered")

    def action2_triggered(self):
        print("Action 2 triggered")
    
    def toolbar_button_clicked(self):
        self.statusBar().showMessage("Toolbar button clicked", 2000)
    
    def button1_clicked(self):
        print("Button 1 clicked")

