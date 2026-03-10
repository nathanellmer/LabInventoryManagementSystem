from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import MsgHeaderWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton

class MsgDialog(QDialog):
    def __init__(self, title_text: str, message_text: str, btn_text: str):
        super().__init__()

        # Set the window size and title
        self.resize(200, 200)
        self.setWindowTitle(title_text)

        # Initialise the AddUserDialog layout and its margins (left, top, right, bottom)
        msg_dialog_layout = QVBoxLayout()
        msg_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the message label
        msg_dialog_layout.addWidget(MsgHeaderWidget(title_text, message_text))

        # Add a proceed button
        msg_dialog_layout.addWidget(MainMenuButton(btn_text, self.btn_proceed), alignment=Qt.AlignCenter)

        # Set the main layout for the window
        self.setLayout(msg_dialog_layout)
        

    def btn_proceed(self):
        # Close the dialog
        self.close()
