from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import MainMenuHeaderWidget
from ui.custom_widgets.general.footer_widgets import MainMenuFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton, MainMenuDropdownButton, MainMenuLinkButton
from ui.dialogs.add_user_dialog import AddUserDialog
from ui.dialogs.msg_dialog import MsgDialog
from ui.windows.main_window import MainWindow
from core.control_functions import controller
from core.db_get_functions import get_all_usernames

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 600)
        self.setWindowTitle("Laboratory Inventory Management System")
        self.setMaximumHeight(800)

        # Initialise the WelcomeWindow layout and its margins (left, top, right, bottom)
        welcome_window_layout = QVBoxLayout()
        welcome_window_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the welcome window layout
        welcome_window_layout.addWidget(MainMenuHeaderWidget("Welcome to LIMS! Please select your username to proceed:"))

        # Add stretch
        welcome_window_layout.addStretch()

        # Add a dropdown combobox
        self.cmb_usernames = MainMenuDropdownButton()
        self.load_usernames()
        welcome_window_layout.addWidget(self.cmb_usernames, alignment=Qt.AlignCenter)

        # Add spacing
        welcome_window_layout.addSpacing(10)

        # Add a proceed button
        welcome_window_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add spacing
        welcome_window_layout.addSpacing(5)

        # Add a link button
        welcome_window_layout.addWidget(MainMenuLinkButton("I cannot find my name...", self.open_add_user_dialog), alignment=Qt.AlignCenter)

        # Add stretch
        welcome_window_layout.addStretch()

        # Add the universal footer widget to the welcome window layout
        controller.close_all_windows.connect(self.close)
        welcome_window_layout.addWidget(MainMenuFooterWidget())

        # Set the main layout for the window
        self.setLayout(welcome_window_layout)


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
            self.main_window = MainWindow()
            self.main_window.show()
