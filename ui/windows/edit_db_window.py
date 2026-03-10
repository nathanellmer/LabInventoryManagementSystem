from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.header_widgets import MainMenuHeaderWidget
from ui.custom_widgets.general.footer_widgets import MainMenuFooterWidget
from ui.custom_widgets.window_dialog_panels.edit_db_widgets import EditDBBtnPanelWidget, EditDBDropdownWidget
from core.control_functions import controller

class EditDBWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 600)
        self.setWindowTitle("Laboratory Inventory Management System")

        # Initialise the EditDBWindow layout and its margins (left, top, right, bottom)
        edit_db_window_layout = QVBoxLayout()
        edit_db_window_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the edit database window layout
        edit_db_window_layout.addWidget(MainMenuHeaderWidget("Edit LIMS Database"))

        # Add stretch
        edit_db_window_layout.addStretch()

        # Add the button panel widget to the edit database window layout
        edit_db_window_layout.addWidget(EditDBBtnPanelWidget())

        # Add stretch
        edit_db_window_layout.addStretch()

        # Add the dropdown widget to the edit database window layout
        edit_db_window_layout.addWidget(EditDBDropdownWidget())

        # Add stretch
        edit_db_window_layout.addStretch()

        # Add the universal footer widget to the edit database window layout
        controller.close_all_windows.connect(self.close)
        edit_db_window_layout.addWidget(MainMenuFooterWidget())

        # Set the main layout for the window
        self.setLayout(edit_db_window_layout)
