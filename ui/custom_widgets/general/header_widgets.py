from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from core.utility_functions import resource_path

# Title label widget for the application
class TitleLabel(QLabel):
    def __init__(self, lbl_text: str):
        super().__init__()
        self.setText(lbl_text)
        self.setProperty("role", "universal_title_lbl")
        self.setAlignment(Qt.AlignCenter)


# Logo label widget for the application
class LabLogoLabel(QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(resource_path("assets/Lab_logo.png"))
        self.setPixmap(pixmap.scaledToWidth(150, Qt.SmoothTransformation))
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(50)


# Information line label widget for the application
class InfoLineLabel(QLabel):
    def __init__(self, lbl_text: str):
        super().__init__()
        self.setText(lbl_text)
        self.setProperty("role", "universal_info_line_lbl")
        self.setAlignment(Qt.AlignCenter)


# Messagebox title label widget for the application
class MsgTitleLabel(QLabel):
    def __init__(self, lbl_text: str):
        super().__init__()
        self.setText(lbl_text)
        self.setProperty("role", "msg_title_lbl")
        self.setAlignment(Qt.AlignCenter)


# Messagebox information line label widget for the application
class MsgInfoLineLabel(QLabel):
    def __init__(self, lbl_text: str):
        super().__init__()
        self.setText(lbl_text)
        self.setProperty("role", "msg_info_line_lbl")
        self.setAlignment(Qt.AlignCenter)


# Header widget for the application main menus
class MainMenuHeaderWidget(QWidget):
    def __init__(self, info_line_text: str):
        super().__init__()

        # Setup a layout for the widget
        header_layout = QVBoxLayout()

        # Add the title label to the header layout
        header_layout.addWidget(TitleLabel("Laboratory Inventory Management System"))

        # Add a logo to the header layout
        header_layout.addWidget(LabLogoLabel())

        # Add spacing
        header_layout.addSpacing(10)

        # Add the information line to the header layout
        header_layout.addWidget(InfoLineLabel(info_line_text))

        # Set the main layout for the widget
        self.setLayout(header_layout)


# Header widget for the application forms
class FormHeaderWidget(QWidget):
    def __init__(self, info_line_text: str):
        super().__init__()

        # Setup a layout for the widget
        header_layout = QVBoxLayout()

        # Add the information line to the header layout
        header_layout.addWidget(InfoLineLabel(info_line_text))

        # Set the main layout for the widget
        self.setLayout(header_layout)


# Header widget for the application message boxes
class MsgHeaderWidget(QWidget):
    def __init__(self, title_text: str, info_line_text: str):
        super().__init__()

        # Setup a layout for the widget
        header_layout = QVBoxLayout()

        # Add the title label to the header layout
        header_layout.addWidget(MsgTitleLabel(title_text))

        # Add spacing
        header_layout.addSpacing(5)

        # Add the information line to the header layout
        header_layout.addWidget(MsgInfoLineLabel(info_line_text))

        # Set the main layout for the widget
        self.setLayout(header_layout)