from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QWidget
from PySide6.QtCore import Qt
from ui.custom_widgets.general.label_widgets import InfoLabel
from ui.custom_widgets.general.button_widgets import MainMenuButton

# Form label/line edit widget for the application
class FormLabelTextWidget(QHBoxLayout):
    def __init__(self, lbl_text: str):
        super().__init__()

        # Create a label and line edit
        self.lbl = QLabel(lbl_text)
        self.txt = QLineEdit()

        # Set properties for the label and line edit
        self.lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lbl.setProperty("role", "std_form_lbl")
        self.txt.setProperty("role", "std_form_txt")

        # Add the label and line edit to the layout
        self.addWidget(self.lbl)
        self.addWidget(self.txt)


# Form label/line edit widget for the application (widened)
class FormLabelTextWidgetWide(QHBoxLayout):
    def __init__(self, lbl_text: str):
        super().__init__()

        # Create a label and line edit
        self.lbl = QLabel(lbl_text)
        self.txt = QLineEdit()

        # Set properties for the label and line edit
        self.lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lbl.setProperty("role", "std_form_lbl")
        self.txt.setProperty("role", "wide_form_txt")

        # Add the label and line edit to the layout
        self.addWidget(self.lbl)
        self.addWidget(self.txt)


# Form search panel widget for the application
class FormSearchPanelWidget(QWidget):
    def __init__(self, info_text:str, lbl_text: str, on_click):
        super().__init__()

        # Set the layout for the search panel
        search_panel_layout = QVBoxLayout()

        # Add an info line label
        search_panel_layout.addWidget(InfoLabel(info_text))

        # Add spacing
        search_panel_layout.addSpacing(5)

        # Add a form label/line edit widget for the search query
        self.search_txt = FormLabelTextWidget(lbl_text)
        search_panel_layout.addLayout(self.search_txt)

        # Add spacing
        search_panel_layout.addSpacing(5)

        # Add a proceed button
        search_panel_layout.addWidget(MainMenuButton("Search", on_click), alignment=Qt.AlignCenter)

        # Set the main layout for the widget
        self.setLayout(search_panel_layout)