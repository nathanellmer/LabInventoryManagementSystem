from PySide6.QtWidgets import QDialog, QGridLayout, QVBoxLayout
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
        select_dialog_layout = QVBoxLayout()
        select_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the message label
        select_dialog_layout.addWidget(MsgHeaderWidget(title_text, message_text))

        # Add a dropdown menu
        self.cmb_optn_1 = MainMenuDropdownPanelWidget(lbl_text_optn_1, self.btn_proceed_optn_1)
        self.cmb_optn_1.cmb_dropdown.addItems(items_optn_1)
        select_dialog_layout.addWidget(self.cmb_optn_1)

        # Set the main layout for the window
        self.setLayout(select_dialog_layout)
        

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
        select_dialog_layout = QVBoxLayout()
        select_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the message label
        select_dialog_layout.addWidget(MsgHeaderWidget(title_text, message_text))

        # Add a dropdown menu
        self.cmb_optn_1 = MainMenuDropdownPanelWidget(lbl_text_optn_1, self.btn_proceed_optn_1)
        self.cmb_optn_1.cmb_dropdown.addItems(items_optn_1)
        select_dialog_layout.addWidget(self.cmb_optn_1)

        # Add spacing
        select_dialog_layout.addSpacing(10)
        
        # Add a dropdown menu
        self.cmb_optn_2 = MainMenuDropdownPanelWidget(lbl_text_optn_2, self.btn_proceed_optn_2)
        self.cmb_optn_2.cmb_dropdown.addItems(items_optn_2)
        select_dialog_layout.addWidget(self.cmb_optn_2)

        # Set the main layout for the window
        self.setLayout(select_dialog_layout)
        

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


class ChoiceSelectionDialogFour(QDialog):
    def __init__(self, title_text: str, message_text: str, lbl_text_optn_1: str, lbl_text_optn_2: str, lbl_text_optn_3: str, lbl_text_optn_4: str, items_optn_1: list, items_optn_2: list, items_optn_3: list, items_optn_4: list):
        super().__init__()
        # Set a blank selection parameter
        self.selected_idx = None
        self.selected_optn = None

        # Set the window size and title
        self.resize(200, 200)
        self.setWindowTitle(title_text)

        # Initialise the AddUserDialog layout and its margins (left, top, right, bottom)
        select_dialog_layout = QVBoxLayout()
        select_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the message label
        select_dialog_layout.addWidget(MsgHeaderWidget(title_text, message_text))

        grid_layout = QGridLayout()

        # Add a dropdown menu
        self.cmb_optn_1 = MainMenuDropdownPanelWidget(lbl_text_optn_1, self.btn_proceed_optn_1)
        self.cmb_optn_1.cmb_dropdown.addItems(items_optn_1)
        grid_layout.addWidget(self.cmb_optn_1, 0, 0)
        
        # Add a dropdown menu
        self.cmb_optn_2 = MainMenuDropdownPanelWidget(lbl_text_optn_2, self.btn_proceed_optn_2)
        self.cmb_optn_2.cmb_dropdown.addItems(items_optn_2)
        grid_layout.addWidget(self.cmb_optn_2, 0, 1)

        # Add a dropdown menu
        self.cmb_optn_3 = MainMenuDropdownPanelWidget(lbl_text_optn_3, self.btn_proceed_optn_3)
        self.cmb_optn_3.cmb_dropdown.addItems(items_optn_3)
        grid_layout.addWidget(self.cmb_optn_3, 1, 0)

        # Add spacing
        select_dialog_layout.addSpacing(10)
        
        # Add a dropdown menu
        self.cmb_optn_4 = MainMenuDropdownPanelWidget(lbl_text_optn_4, self.btn_proceed_optn_4)
        self.cmb_optn_4.cmb_dropdown.addItems(items_optn_4)
        grid_layout.addWidget(self.cmb_optn_4, 1, 1)

        select_dialog_layout.addLayout(grid_layout)

        # Set the main layout for the window
        self.setLayout(select_dialog_layout)
        

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


    def btn_proceed_optn_3(self):
        # Set the selected option to the third dropdown menu
        self.selected_option = 3
        self.selected_idx = self.cmb_optn_3.cmb_dropdown.currentIndex()

        # Accept the dialog
        self.accept()


    def btn_proceed_optn_4(self):
        # Set the selected option to the fourth dropdown menu
        self.selected_option = 4
        self.selected_idx = self.cmb_optn_4.cmb_dropdown.currentIndex()

        # Accept the dialog
        self.accept()
