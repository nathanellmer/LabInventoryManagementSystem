from PySide6.QtWidgets import QHBoxLayout, QListWidget, QWidget, QVBoxLayout
from core.db_delete_functions import delete_shopping_list_item_from_db
from core.db_get_functions import get_user_info_by_username, get_username_by_id, get_all_shopping_list_items
from core.db_add_functions import add_shopping_list_item_to_db
from core.control_functions import controller
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormLabelTextWidgetWide

# Panel widget for the shopping list based database information
class ShoppingListPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a form label/line edit widget for the new item
        self.item_description = FormLabelTextWidgetWide("Item Description:")
        form_panel_layout.addLayout(self.item_description)

        # Add buttons to add and remove items from the shopping list
        btn_panel_layout = QHBoxLayout()
        btn_panel_layout.addStretch()
        btn_panel_layout.addWidget(MainMenuButton("Add Item", self.btn_add_item))
        btn_panel_layout.addSpacing(10)
        btn_panel_layout.addWidget(MainMenuButton("Remove Item", self.btn_remove_item))
        btn_panel_layout.addStretch()
        form_panel_layout.addLayout(btn_panel_layout)

        # Add stretch to push the buttons to the top of the panel
        form_panel_layout.addStretch()

        # Add list widget to display the shopping list items
        self.shopping_list = QListWidget()
        self.shopping_list.setSelectionMode(QListWidget.MultiSelection)
        self.load_reorder_items()
        form_panel_layout.addWidget(self.shopping_list)

        # Add stretch to push the buttons to the top of the panel
        form_panel_layout.addStretch()

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)

    def btn_add_item(self):
        user_name = controller.logged_in_user
        user_info = get_user_info_by_username(user_name)
        add_shopping_list_item_to_db(user_info[0], self.item_description.txt.text())
        self.item_description.txt.clear()
        self.load_reorder_items()

    def btn_remove_item(self):
        selected_items = self.shopping_list.selectedItems()
        for item in selected_items:
            idx = self.shopping_list.row(item)
            delete_shopping_list_item_from_db(self.shopping_list_item_ids[idx])

        for item in selected_items:
            idx = self.shopping_list.row(item)
            self.shopping_list.takeItem(idx)
            

    def load_reorder_items(self):
        # Get the list of items that need to be reordered
        reorder_items = get_all_shopping_list_items()
        self.shopping_list_item_ids = []
        self.shopping_list.clear()

        for item in reorder_items:
            username = get_username_by_id(item[1])
            self.shopping_list.addItem(f"{item[3]} - {username} - {item[2]}")
            self.shopping_list_item_ids.append(item[0])

        print(self.shopping_list_item_ids)
