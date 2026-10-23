from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.window_dialog_panels.shopping_list_db_widgets import ShoppingListPanelWidget
from core.control_functions import controller

class ShoppingListPage(QWidget):
    def __init__(self):
        super().__init__()

        # Initialise the ShoppingListPage layout
        shopping_list_dialog_layout = QVBoxLayout()

        # Add the header widget to the add user dialog layout
        shopping_list_dialog_layout.addWidget(FormHeaderWidget("View and Edit the Shopping List:"))

        # Add stretch
        shopping_list_dialog_layout.addStretch()

        # Add the shopping list panel widget to the dialog layout
        self.shopping_list_form = ShoppingListPanelWidget()
        shopping_list_dialog_layout.addWidget(self.shopping_list_form, alignment=Qt.AlignCenter)

        # Add stretch
        shopping_list_dialog_layout.addStretch()

        # Add the universal footer widget to the shopping list dialog layout
        controller.close_all_windows.connect(self.close)
        shopping_list_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(shopping_list_dialog_layout)
