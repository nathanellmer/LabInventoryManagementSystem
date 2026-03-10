from PySide6.QtWidgets import QComboBox, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

# Main menu button widgets for the application
class MainMenuButton(QPushButton):
    def __init__(self, btn_text: str, on_click=None):
        super().__init__()
        self.setText(btn_text)
        self.setProperty("role", "universal_btn")
        
        if on_click:
            self.clicked.connect(on_click)


# Main menu link button widget for the application
class MainMenuLinkButton(QPushButton):
    def __init__(self, btn_text: str, on_click=None):
        super().__init__()
        self.setText(btn_text)
        self.setProperty("role", "universal_link_btn")
        
        if on_click:
            self.clicked.connect(on_click)


# Main menu dropdown button widget for the application
class MainMenuDropdownButton(QComboBox):
    def __init__(self):
        super().__init__()
        self.setProperty("role", "universal_cmb")


# Main menu dropdown button panel widget for the application
class MainMenuDropdownPanelWidget(QWidget):
    def __init__(self, lbl_text:str, on_click=None):
        super().__init__()
        # Set the layout for the widget
        panel_layout = QVBoxLayout()

        # Add a label to the panel
        self.lbl = QLabel(lbl_text)
        self.lbl.setProperty("role", "universal_info_line_lbl")
        self.lbl.setAlignment(Qt.AlignCenter)
        panel_layout.addWidget(self.lbl)

        # Add spacing
        panel_layout.addSpacing(5)

        # Add a dropdown combobox to the panel
        self.cmb_dropdown = MainMenuDropdownButton()
        panel_layout.addWidget(self.cmb_dropdown, alignment=Qt.AlignCenter)

        # Add spacing
        panel_layout.addSpacing(5)

        # Add proceed button to the panel
        panel_layout.addWidget(MainMenuButton("Proceed", on_click), alignment=Qt.AlignCenter)

        # Set the main layout for the widget
        self.setLayout(panel_layout)
