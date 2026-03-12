from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.button_widgets import MainMenuButton, MainMenuDropdownPanelWidget
from ui.custom_widgets.general.label_widgets import InfoLabel
from ui.dialogs.search_items_dialog import SearchItemDialog

# Panel widget for the use database menu
class UseDBBtnPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set the layout for the widget
        panel_layout = QVBoxLayout()

        # Add a label to the panel
        panel_layout.addWidget(InfoLabel("Quick actions:"))

        # Add spacing
        panel_layout.addSpacing(5)

        # Set the layout for a grid of buttons
        grid_layout = QGridLayout()

        # Set the buttons for the panel
        grid_layout.addWidget(MainMenuButton("Export All Items"), 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Search All Items", self.open_search_items_dialog), 0, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Generate Order Form"), 0, 2, alignment=Qt.AlignCenter)

        # Add the grid layout to the panel layout
        panel_layout.addLayout(grid_layout)

        # Set the main layout for the widget
        self.setLayout(panel_layout)


    def open_search_items_dialog(self):
        search_items_dialog = SearchItemDialog()
        search_items_dialog.exec()


# Dropdown widget for the use database menu
class UseDBDropdownWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set the layout for the widget
        dropdown_layout = QVBoxLayout()

        # Set the panel widget
        self.dropdown_widget = MainMenuDropdownPanelWidget("Other actions:")
        self.dropdown_widget.cmb_dropdown.addItems(["Select Action...", 
                                                    "See All Items", 
                                                    "See Users", "Generate CSV for All Users",
                                                    "See Companies", "Generate CSV for All Companies",
                                                    "See Grant Codes", "Generate CSV for All Grant Codes",
                                                    "Export All to CSV"])
        dropdown_layout.addWidget(self.dropdown_widget)

        # Set the main layout for the widget
        self.setLayout(dropdown_layout)
        