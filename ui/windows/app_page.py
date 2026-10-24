from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget
from PySide6.QtCore import Qt
from ui.custom_widgets.general.footer_widgets import FooterLabel
from ui.custom_widgets.window_dialog_panels.bar_widgets import Navbar, StatusBar
from ui.windows.database_page import DatabasePage
from ui.windows.forms_page import FormsPage
from ui.windows.search_page import SearchPage
from ui.windows.shopping_list_page import ShoppingListPage
from core.control_functions import controller

class AppPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set the application page layout
        app_page_layout = QVBoxLayout()

        # Create a top status bar widget
        self.status_bar = StatusBar()
        self.status_bar.lbl_page_title.setText("Database Page")
        app_page_layout.addWidget(self.status_bar)

        # Create a main content area layout
        main_page_layout = QHBoxLayout()

        # Create a navigation bar widget
        self.v_nav_bar = Navbar()
        main_page_layout.addWidget(self.v_nav_bar)

        # Create a stacked widget to hold the application pages
        self.app_pages_stack = QStackedWidget()
        main_page_layout.addWidget(self.app_pages_stack)

        # Add the main content area layout to the application page layout
        app_page_layout.addLayout(main_page_layout)

        # Create a footer widget
        app_page_layout.addWidget(FooterLabel())

        # Set the main layout for the application page
        self.setLayout(app_page_layout)

        # Add the application pages to the stacked widget
        self.database_page = DatabasePage()
        self.app_pages_stack.addWidget(self.database_page)
        self.search_page = SearchPage()  
        self.app_pages_stack.addWidget(self.search_page)
        self.shopping_list_page = ShoppingListPage()  
        self.app_pages_stack.addWidget(self.shopping_list_page)
        self.forms_page = FormsPage()  # Placeholder for the forms page
        self.app_pages_stack.addWidget(self.forms_page)

        # Connect the page_selection signal to the method that switches to the internal application pages
        self.v_nav_bar.page_selection.connect(self.show_app_page)

    def show_app_page(self):
        # Switch to the appropriate application page based on the active_page value
        if controller.active_page == 1:
            self.app_pages_stack.setCurrentWidget(self.database_page)
            self.status_bar.lbl_page_title.setText("Database Page")
        elif controller.active_page == 2:
            self.app_pages_stack.setCurrentWidget(self.search_page)
            self.status_bar.lbl_page_title.setText("Search Page")
        elif controller.active_page == 3:
            self.app_pages_stack.setCurrentWidget(self.shopping_list_page)
            self.status_bar.lbl_page_title.setText("Shopping List Page")
        elif controller.active_page == 4:
            self.app_pages_stack.setCurrentWidget(self.forms_page)
            self.status_bar.lbl_page_title.setText("Forms Page")










    #     # Add the login page to the stack
    #     self.login_page = LoginPage()
    #     self.app_stack.addWidget(self.login_page)

    #     # Add the main application page to the stack
    #     self.app_page = AppPage()
    #     self.app_stack.addWidget(self.app_page)

    #     # Connect the login_successful signal to the method that switches to the main application page
    #     self.login_page.login_successful.connect(self.show_app_page)

    # def show_app_page(self):
    #     self.app_stack.setCurrentWidget(self.app_page)