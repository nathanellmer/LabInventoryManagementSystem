from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from core.control_functions import controller
from core.control_functions import db_info
from core.utility_functions import resource_path
from ui.styles.load_themes import THEMES

# Footer label widget for the application
class FooterLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Lab Inventory Management System - LIMS v0.3 - Developed by Nathan Ellmer")
        self.setProperty("role", "universal_footer_lbl")
        self.setAlignment(Qt.AlignCenter)


# Logo label widget for the application
class SULogoLabel(QLabel):
    def __init__(self):
        super().__init__()
        theme = THEMES.get(db_info.COLOUR_SCHEME)
        pixmap = QPixmap(theme["logo"])
        self.setPixmap(pixmap.scaledToWidth(150, Qt.SmoothTransformation))
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(150)


# Close button widget for the application
class CloseButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Close the Application")
        self.setProperty("role", "universal_close_btn")
        self.clicked.connect(self.close_application)

    def close_application(self):
        controller.close_all_windows.emit()


# Footer widget for the applications main menus
class MainMenuFooterWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Setup a layout for the widget
        footer_layout = QVBoxLayout()

        # Add a logo to the footer layout
        footer_layout.addWidget(SULogoLabel())

        # Add the close button to the footer layout
        footer_layout.addWidget(CloseButton(), alignment=Qt.AlignCenter)

        # Add the title label to the footer layout
        footer_layout.addWidget(FooterLabel())

        # Set the main layout for the widget
        self.setLayout(footer_layout)


# Footer widget for the applications forms
class FormFooterWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Setup a layout for the widget
        footer_layout = QVBoxLayout()

        # Add the close button to the footer layout
        footer_layout.addWidget(CloseButton(), alignment=Qt.AlignCenter)

        # Set the main layout for the widget
        self.setLayout(footer_layout)
        