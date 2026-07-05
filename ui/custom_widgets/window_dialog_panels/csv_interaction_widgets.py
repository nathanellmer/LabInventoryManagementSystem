from PySide6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton

# Panel widget for the csv interaction
class CSVPanelWidget(QWidget):
    def __init__(self, blank_csv_on_click=None, upload_csv_on_click=None):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a HBoxLayout for the two buttons
        btn_layout = QHBoxLayout()

        # Add the buttons
        btn_layout.addStretch()
        btn_layout.addWidget(MainMenuButton("Create Blank CSV Template", blank_csv_on_click))
        btn_layout.addSpacing(20)
        btn_layout.addWidget(MainMenuButton("Upload CSV File", upload_csv_on_click))
        btn_layout.addStretch()
        form_panel_layout.addLayout(btn_layout)

        # Add spacing
        form_panel_layout.addSpacing(20)

        # Add a table widget
        self.csv_table = QTableWidget()
        self.csv_table.setProperty("role", "form_csv_table")
        form_panel_layout.addWidget(self.csv_table)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)
