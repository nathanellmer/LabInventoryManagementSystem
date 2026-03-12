from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.button_widgets import MainMenuButton, MainMenuDropdownPanelWidget
from ui.custom_widgets.general.label_widgets import InfoLabel
from ui.dialogs.add_item_dialog import AddItemDialog
from ui.dialogs.add_user_dialog import AddUserDialog
from ui.dialogs.add_supplier_dialog import AddSupplierDialog
from ui.dialogs.add_grant_codes_dialog import AddGrantCodesDialog
from ui.dialogs.add_storage_locations_dialog import AddStorageLocationsDialog
from ui.dialogs.update_item_dialog import UpdateItemDialog
from ui.dialogs.update_user_dialog import UpdateUserDialog
from ui.dialogs.update_supplier_dialog import UpdateSupplierDialog
from ui.dialogs.update_grant_codes_dialog import UpdateGrantCodesDialog
from ui.dialogs.update_storage_locations_dialog import UpdateStorageLocationsDialog
from ui.dialogs.delete_item_dialog import DeleteItemDialog
from ui.dialogs.delete_user_dialog import DeleteUserDialog
from ui.dialogs.delete_supplier_dialog import DeleteSupplierDialog
from ui.dialogs.delete_grant_codes_dialog import DeleteGrantCodesDialog
from ui.dialogs.delete_storage_locations_dialog import DeleteStorageLocationsDialog


# Panel widget for the edit database menu
class EditDBBtnPanelWidget(QWidget):
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
        grid_layout.addWidget(MainMenuButton("Add Item", self.open_add_item_dialog), 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Update Item", self.open_update_item_dialog), 0, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Delete Item", self.open_delete_item_dialog), 0, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Add Supplier", self.open_add_supplier_dialog), 1, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Update Supplier", self.open_upd_supplier_dialog), 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Delete Supplier", self.open_delete_supplier_dialog), 1, 2, alignment=Qt.AlignCenter)

        # Add the grid layout to the panel layout
        panel_layout.addLayout(grid_layout)

        # Set the main layout for the widget
        self.setLayout(panel_layout)


    def open_add_item_dialog(self):
        add_item_dialog = AddItemDialog()
        add_item_dialog.exec()


    def open_update_item_dialog(self):
        update_item_dialog = UpdateItemDialog()
        update_item_dialog.exec()


    def open_delete_item_dialog(self):
        delete_item_dialog = DeleteItemDialog()
        delete_item_dialog.exec()


    def open_add_supplier_dialog(self):
        add_supplier_dialog = AddSupplierDialog()
        add_supplier_dialog.exec()


    def open_upd_supplier_dialog(self):
        upd_supplier_dialog = UpdateSupplierDialog()
        upd_supplier_dialog.exec()


    def open_delete_supplier_dialog(self):
        delete_supplier_dialog = DeleteSupplierDialog()
        delete_supplier_dialog.exec()


# Dropdown widget for the edit database menu
class EditDBDropdownWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set the layout for the widget
        dropdown_layout = QVBoxLayout()

        # Set the panel widget
        self.dropdown_widget = MainMenuDropdownPanelWidget("Other actions:", self.select_action)
        self.dropdown_widget.cmb_dropdown.addItems(["Select Action...", 
                                                    "Add Items via csv",
                                                    "Add User", "Update User", "Delete User",
                                                    "Add Grant Code", "Update Grant Code", "Delete Grant Code",
                                                    "Add Storage Location", "Update Storage Location", "Delete Storage Location"])
        dropdown_layout.addWidget(self.dropdown_widget)

        # Set the main layout for the widget
        self.setLayout(dropdown_layout)


    def select_action(self):
        action = self.dropdown_widget.cmb_dropdown.currentText()
        if action == "Add User":
            self.open_add_user_dialog()
        elif action == "Update User":
            self.open_update_user_dialog()
        elif action == "Delete User":
            self.open_delete_user_dialog()
        elif action == "Add Grant Code":
            self.open_add_grant_code_dialog()
        elif action == "Update Grant Code":
            self.open_update_grant_code_dialog()
        elif action == "Delete Grant Code":
            self.open_delete_grant_code_dialog()
        elif action == "Add Storage Location":
            self.open_add_storage_location_dialog()
        elif action == "Update Storage Location":
            self.open_update_storage_location_dialog()
        elif action == "Delete Storage Location":
            self.open_delete_storage_location_dialog()


    def open_add_user_dialog(self):
        add_user_dialog = AddUserDialog()
        add_user_dialog.exec()


    def open_update_user_dialog(self):
        update_user_dialog = UpdateUserDialog()
        update_user_dialog.exec()


    def open_delete_user_dialog(self):
        delete_user_dialog = DeleteUserDialog()
        delete_user_dialog.exec()


    def open_add_grant_code_dialog(self):
        add_grant_code_dialog = AddGrantCodesDialog()
        add_grant_code_dialog.exec()


    def open_update_grant_code_dialog(self):
        update_grant_code_dialog = UpdateGrantCodesDialog()
        update_grant_code_dialog.exec()


    def open_delete_grant_code_dialog(self):
        delete_grant_code_dialog = DeleteGrantCodesDialog()
        delete_grant_code_dialog.exec()


    def open_add_storage_location_dialog(self):
        add_storage_location_dialog = AddStorageLocationsDialog()
        add_storage_location_dialog.exec()


    def open_update_storage_location_dialog(self):
        update_storage_location_dialog = UpdateStorageLocationsDialog()
        update_storage_location_dialog.exec()


    def open_delete_storage_location_dialog(self):
        delete_storage_location_dialog = DeleteStorageLocationsDialog()
        delete_storage_location_dialog.exec()
        