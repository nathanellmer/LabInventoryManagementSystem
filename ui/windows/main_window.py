from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import MainMenuHeaderWidget
from ui.custom_widgets.general.footer_widgets import MainMenuFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.windows.edit_db_window import EditDBWindow
from ui.windows.use_db_window import UseDBWindow
from core.control_functions import controller

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 600)
        self.setWindowTitle("Laboratory Inventory Management System")

        # Initialise the MainWindow layout and its margins (left, top, right, bottom)
        main_window_layout = QVBoxLayout()
        main_window_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the main window layout
        main_window_layout.addWidget(MainMenuHeaderWidget(f"Welcome to LIMS {controller.logged_in_user}! Please select an option:"))

        # Add stretch
        main_window_layout.addStretch()

        # Add a button to move to edit database menu
        main_window_layout.addWidget(MainMenuButton("Edit Database", self.btn_edit_db), alignment=Qt.AlignCenter)

        # Add spacing
        main_window_layout.addSpacing(10)

        # Add a button to move to use database menu
        main_window_layout.addWidget(MainMenuButton("Use Database", self.btn_use_db), alignment=Qt.AlignCenter)

        # Add stretch
        main_window_layout.addStretch()

        # Add the universal footer widget to the main window layout
        controller.close_all_windows.connect(self.close)
        main_window_layout.addWidget(MainMenuFooterWidget())

        # Set the main layout for the window
        self.setLayout(main_window_layout)


    def btn_edit_db(self):
        # Open the menu to edit the database
        self.edit_db_window = EditDBWindow()
        self.edit_db_window.show()


    def btn_use_db(self):
        # Open the menu to use the database
        self.use_db_window = UseDBWindow()
        self.use_db_window.show()
            
