from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import MsgHeaderWidget
from ui.custom_widgets.general.button_widgets import MainMenuDropdownPanelWidget

class ChoiceSelectionDialogOne(QDialog):
    def __init__(self, title_text: str, message_text: str, lbl_text_optn_1: str, items_optn_1: list):
        super().__init__()
        # Set a blank selection parameter
        self.selected_idx = None

        # Set the window size and title
        self.resize(200, 200)
        self.setWindowTitle(title_text)

        # Initialise the AddUserDialog layout and its margins (left, top, right, bottom)
        msg_dialog_layout = QVBoxLayout()
        msg_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the message label
        msg_dialog_layout.addWidget(MsgHeaderWidget(title_text, message_text))

        # Add a dropdown menu
        self.cmb_optn_1 = MainMenuDropdownPanelWidget(lbl_text_optn_1, self.btn_proceed_optn_1)
        self.cmb_optn_1.cmb_dropdown.addItems(items_optn_1)
        msg_dialog_layout.addWidget(self.cmb_optn_1)

        # Set the main layout for the window
        self.setLayout(msg_dialog_layout)
        

    def btn_proceed_optn_1(self):
        # Set the selected option to the first dropdown menu
        self.selected_idx = self.cmb_optn_1.cmb_dropdown.currentIndex()

        # Accept the dialog
        self.accept()


class ChoiceSelectionDialogTwo(QDialog):
    def __init__(self, title_text: str, message_text: str, lbl_text_optn_1: str, lbl_text_optn_2: str, items_optn_1: list, items_optn_2: list):
        super().__init__()
        # Set a blank selection parameter
        self.selected_idx = None
        self.selected_optn = None

        # Set the window size and title
        self.resize(200, 200)
        self.setWindowTitle(title_text)

        # Initialise the AddUserDialog layout and its margins (left, top, right, bottom)
        msg_dialog_layout = QVBoxLayout()
        msg_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the message label
        msg_dialog_layout.addWidget(MsgHeaderWidget(title_text, message_text))

        # Add a dropdown menu
        self.cmb_optn_1 = MainMenuDropdownPanelWidget(lbl_text_optn_1, self.btn_proceed_optn_1)
        self.cmb_optn_1.cmb_dropdown.addItems(items_optn_1)
        msg_dialog_layout.addWidget(self.cmb_optn_1)

        # Add spacing
        msg_dialog_layout.addSpacing(10)
        
        # Add a dropdown menu
        self.cmb_optn_2 = MainMenuDropdownPanelWidget(lbl_text_optn_2, self.btn_proceed_optn_2)
        self.cmb_optn_2.cmb_dropdown.addItems(items_optn_2)
        msg_dialog_layout.addWidget(self.cmb_optn_2)

        # Set the main layout for the window
        self.setLayout(msg_dialog_layout)
        

    def btn_proceed_optn_1(self):
        # Set the selected option to the first dropdown menu
        self.selected_option = 1
        self.selected_idx = self.cmb_optn_1.cmb_dropdown.currentIndex()

        # Accept the dialog
        self.accept()


    def btn_proceed_optn_2(self):
        # Set the selected option to the second dropdown menu
        self.selected_option = 2
        self.selected_idx = self.cmb_optn_2.cmb_dropdown.currentIndex()

        # Accept the dialog
        self.accept()
