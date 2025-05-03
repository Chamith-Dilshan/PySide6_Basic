from PySide6.QtWidgets import QMessageBox, QVBoxLayout, QPushButton, QWidget
from functools import partial
from typing import Callable, Optional
from enum import Enum
from dataclasses import dataclass

class MessageType(Enum):
    """Enumeration of supported message types."""
    INFORMATION = "information"
    WARNING = "warning"
    CRITICAL = "critical"
    QUESTION = "question"

@dataclass(frozen=True)
class MessageBoxConfig:
    """Configuration dataclass for message box settings."""
    title: str
    text: str
    icon: QMessageBox.Icon
    buttons: QMessageBox.StandardButton
    callback: Optional[Callable[[QMessageBox.StandardButton], None]]

class MessageWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Message Dialog Demo")
        self.setGeometry(100, 100, 300, 200)
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Initialize the UI with message type buttons."""
        layout = QVBoxLayout()
        
        # Define message types and their configurations
        message_types: list[tuple[MessageType, QMessageBox.Icon]] = [
            (MessageType.INFORMATION, QMessageBox.Icon.Information),
            (MessageType.WARNING, QMessageBox.Icon.Warning),
            (MessageType.CRITICAL, QMessageBox.Icon.Critical),
            (MessageType.QUESTION, QMessageBox.Icon.Question)
        ]
        
        # Create buttons for each message type
        for msg_type, icon in message_types:
            btn = QPushButton(msg_type.value.capitalize())
            btn.clicked.connect(
                partial(self._show_message_box, msg_type, icon)
            )
            layout.addWidget(btn)
        
        self.setLayout(layout)

    def _show_message_box(
        self, 
        message_type: MessageType, 
        icon: QMessageBox.Icon,
        callback: Optional[Callable[[QMessageBox.StandardButton], None]] = None
    ) -> None:
        """Display a message box with the specified type and handle response."""
        # Configure message box based on type
        config = self._create_config(message_type, icon, callback)
        
        # Create and show message box
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(config.title)
        msg_box.setText(config.text)
        msg_box.setIcon(config.icon)
        msg_box.setStandardButtons(config.buttons)
        
        # Show dialog and handle response
        response = msg_box.exec()
        
        # Handle response
        if callback:
            callback(QMessageBox.StandardButton(response))
        elif message_type == MessageType.QUESTION:
            self._handle_question_response(QMessageBox.StandardButton(response))

    def _create_config(
        self, 
        message_type: MessageType, 
        icon: QMessageBox.Icon,
        callback: Optional[Callable[[QMessageBox.StandardButton], None]]
    ) -> MessageBoxConfig:
        """Create configuration for message box."""
        config = MessageBoxConfig(
            title=f"{message_type.value.capitalize()} Message",
            text=f"This is a {message_type.value} message!",
            icon=icon,
            buttons=self._get_buttons_for_type(message_type),
            callback=callback
        )
        return config

    def _get_buttons_for_type(self, message_type: MessageType) -> QMessageBox.StandardButton:
        """Get appropriate buttons for message type."""
        if message_type == MessageType.QUESTION:
            return (
                QMessageBox.StandardButton.Yes 
                | QMessageBox.StandardButton.No
            )
        return QMessageBox.StandardButton.Ok

    def _handle_question_response(self, response: QMessageBox.StandardButton) -> None:
        """Handle Yes/No responses from question dialogs."""
        if response == QMessageBox.StandardButton.Yes:
            print("User selected Yes")
        elif response == QMessageBox.StandardButton.No:
            print("User selected No")