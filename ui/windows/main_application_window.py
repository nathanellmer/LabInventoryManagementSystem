from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.windows.login_page import LoginPage
from ui.windows.app_page import AppPage
from core.control_functions import controller

class MainApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and minimum size
        self.setWindowTitle("Laboratory Inventory Management System")
        self.setMinimumSize(800, 600)

        # Create a stacked widget to hold the login page and the main application page
        self.app_stack = QStackedWidget()
        self.setCentralWidget(self.app_stack)

        # Add the login page to the stack
        self.login_page = LoginPage()
        self.app_stack.addWidget(self.login_page)

        # Add the main application page to the stack
        self.app_page = AppPage()
        self.app_stack.addWidget(self.app_page)

        # Connect the login_successful signal to the method that switches to the main application page
        self.login_page.login_successful.connect(self.show_app_page)

    def show_app_page(self):
        # Show the main application page and update the status bar with the logged-in user's name
        self.app_stack.setCurrentWidget(self.app_page)
        self.app_page.status_bar.lbl_username.setText(controller.logged_in_user)
