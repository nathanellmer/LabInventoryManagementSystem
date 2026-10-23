from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.custom_widgets.general.header_widgets import MainMenuHeaderWidget
from ui.custom_widgets.general.footer_widgets import MainMenuFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton, MainMenuDropdownButton, MainMenuLinkButton
from ui.dialogs.add_user_dialog import AddUserDialog
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_all_usernames

class LoginPage(QWidget):
    # Setup a signal for successful login
    login_successful = Signal()

    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 600)
        self.setWindowTitle("Laboratory Inventory Management System")
        self.setMaximumHeight(800)

        # Initialise the WelcomeWindow layout and its margins (left, top, right, bottom)
        login_page_layout = QVBoxLayout()
        login_page_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the welcome window layout
        login_page_layout.addWidget(MainMenuHeaderWidget("Welcome to LIMS! Please select your username to proceed:"))

        # Add stretch
        login_page_layout.addStretch()

        # Add a dropdown combobox
        self.cmb_usernames = MainMenuDropdownButton()
        self.load_usernames()
        login_page_layout.addWidget(self.cmb_usernames, alignment=Qt.AlignCenter)

        # Add spacing
        login_page_layout.addSpacing(10)

        # Add a proceed button
        login_page_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add spacing
        login_page_layout.addSpacing(5)

        # Add a link button
        login_page_layout.addWidget(MainMenuLinkButton("I cannot find my name...", self.open_add_user_dialog), alignment=Qt.AlignCenter)

        # Add stretch
        login_page_layout.addStretch()

        # Add the universal footer widget to the login page layout
        controller.close_all_windows.connect(self.close)
        login_page_layout.addWidget(MainMenuFooterWidget())

        # Set the main layout for the window
        self.setLayout(login_page_layout)


    def load_usernames(self):
        # Clear usernames from the dropdown
        self.cmb_usernames.clear()

        # Get the list of usernames from the database and add them to the dropdown
        usernames = get_all_usernames()
        usernames.insert(0, "Select User Name...")
        self.cmb_usernames.addItems(usernames)


    def open_add_user_dialog(self):
        add_user_dialog = AddUserDialog()
        add_user_dialog.db_updated.connect(self.load_usernames)
        add_user_dialog.exec()


    def btn_proceed(self):
        # Gather the data from the form
        username = self.cmb_usernames.currentText()

        # Check a user has been selected
        if username == "Select User Name...":
            # Show a message dialog to prompt the user to select a username
            msg_dialog = MsgDialog("No User Selected", "Please select a username from the dropdown to proceed.", "OK")
            msg_dialog.exec()
        else:
            # Set the user
            controller.logged_in_user = username

            # Open the main window
            self.login_successful.emit()