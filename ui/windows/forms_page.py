from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.header_widgets import MainMenuHeaderWidget
from ui.custom_widgets.general.footer_widgets import MainMenuFooterWidget
from ui.custom_widgets.window_dialog_panels.use_db_widgets import UseDBBtnPanelWidget, UseDBDropdownWidget
from core.control_functions import controller

class FormsPage(QWidget):
    def __init__(self):
        super().__init__()

        # Initialise the FormsPage layout
        forms_page_layout = QVBoxLayout()

        # Add stretch
        forms_page_layout.addStretch()

        # Add the button panel widget to the forms page layout
        forms_page_layout.addWidget(UseDBBtnPanelWidget())

        # Add stretch
        forms_page_layout.addStretch()

        # Add the dropdown widget to the forms page layout
        forms_page_layout.addWidget(UseDBDropdownWidget())

        # Add stretch
        forms_page_layout.addStretch()

        # Set the main layout for the window
        self.setLayout(forms_page_layout)
