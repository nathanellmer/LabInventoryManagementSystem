from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.header_widgets import MainMenuHeaderWidget
from ui.custom_widgets.window_dialog_panels.edit_db_widgets import EditDBBtnPanelWidget, EditDBDropdownWidget

class DatabasePage(QWidget):
    def __init__(self):
        super().__init__()

        # Initialise the DatabasePage layout
        database_page_layout = QVBoxLayout()

        # Add stretch
        database_page_layout.addStretch()

        # Add the button panel widget to the database page layout
        database_page_layout.addWidget(EditDBBtnPanelWidget())

        # Add stretch
        database_page_layout.addStretch()

        # Add the dropdown widget to the database page layout
        database_page_layout.addWidget(EditDBDropdownWidget())

        # Add stretch
        database_page_layout.addStretch()

        # Set the main layout for the window
        self.setLayout(database_page_layout)
