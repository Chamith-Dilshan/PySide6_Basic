from PySide6.QtWidgets import QPushButton, QWidget, QListWidget, QAbstractItemView, QVBoxLayout

class QListWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list_widget.addItem("Item 1")
        self.list_widget.addItems(["Item 2", "Item 3", "Item 4"])

        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        #Function Buttons
        button_add_item = QPushButton("Add Item")
        button_add_item.clicked.connect(self.addItem)

        button_delete_item = QPushButton("Delete Item")
        button_delete_item.clicked.connect(self.deleteItem)

        button_item_count = QPushButton("Item Count")
        button_item_count.clicked.connect(self.itemCount)

        button_selected_items = QPushButton("Selected Items")
        button_selected_items.clicked.connect(self.selectedItems)


        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(button_add_item)
        v_layout.addWidget(button_delete_item)
        v_layout.addWidget(button_item_count)
        v_layout.addWidget(button_selected_items)

        self.setLayout(v_layout)

    def current_item_changed(self, current:str, previous:str):
        if current:
            print(f"Current item changed: {current}")
        if previous:
            print(f"Previous item: {previous}")
    
    def current_text_changed(self, current_text:str):
        print(f"Current text changed: {current_text}")

    def addItem(self):
        self.list_widget.addItem("New Item")
        print("Added new item")
    
    def deleteItem(self):
       self.list_widget.takeItem(self.list_widget.currentRow())
       print("Deleted current item")
    
    def itemCount(self):
        count = self.list_widget.count()
        print(f"Item count: {count}")
    
    def selectedItems(self):
        selected_items = self.list_widget.selectedItems()
        print("Selected items:")
        for item in selected_items:
            print(item.text())