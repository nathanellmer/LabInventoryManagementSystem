import csv
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.button_widgets import MainMenuButton, MainMenuDropdownPanelWidget
from ui.custom_widgets.general.label_widgets import InfoLabel
from ui.dialogs.msg_dialog import MsgDialog
from ui.dialogs.search_items_dialog import SearchItemDialog
from ui.dialogs.generate_order_forms_dialog import GenerateOrderFormsDialog
from core.db_get_functions import get_users_db_fieldnames, get_all_users_info, get_suppliers_db_fieldnames, get_all_suppliers_info, get_grant_codes_db_fieldnames, get_all_grant_codes_info, get_locations_db_fieldnames, get_all_locations_info, get_items_db_fieldnames, get_all_items_info

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
        grid_layout.addWidget(MainMenuButton("Export All Databases", self.export_all_databases), 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Search All Items", self.open_search_items_dialog), 0, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(MainMenuButton("Generate Order Form", self.open_generate_order_forms_dialog), 0, 2, alignment=Qt.AlignCenter)

        # Add the grid layout to the panel layout
        panel_layout.addLayout(grid_layout)

        # Set the main layout for the widget
        self.setLayout(panel_layout)


    def export_all_databases(self):
        self.export_users(msg_dialog=False)
        self.export_suppliers(msg_dialog=False)
        self.export_grant_codes(msg_dialog=False)
        self.export_storage_locations(msg_dialog=False)
        self.export_items(msg_dialog=False)

        msg_dialog = MsgDialog("All databases exported", "All databases information exported to CSV files", "OK")
        msg_dialog.exec()


    def open_search_items_dialog(self):
        search_items_dialog = SearchItemDialog()
        search_items_dialog.exec()


    def open_generate_order_forms_dialog(self):
        generate_order_forms_dialog = GenerateOrderFormsDialog()
        generate_order_forms_dialog.exec()


    def export_users(self, msg_dialog=True):
        # Get the fieldnames for the users table
        fieldnames = get_users_db_fieldnames()

        # Get all users information
        users_info = get_all_users_info()

        # Export the users information to a CSV file
        with open('users_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users_info:
                row_info = {}
                for idx, value in enumerate(user[1:len(user)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Users information exported", "Users information exported to users_info.csv", "OK")
            msg_dialog.exec()


    def export_suppliers(self, msg_dialog=True):
        # Get the fieldnames for the suppliers table
        fieldnames = get_suppliers_db_fieldnames()

        # Get all suppliers information
        suppliers_info = get_all_suppliers_info()

        # Export the suppliers information to a CSV file
        with open('suppliers_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for supplier in suppliers_info:
                row_info = {}
                for idx, value in enumerate(supplier[1:len(supplier)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Suppliers information exported", "Suppliers information exported to suppliers_info.csv", "OK")
            msg_dialog.exec()


    def export_grant_codes(self, msg_dialog=True):
        # Get the fieldnames for the grant codes table
        fieldnames = get_grant_codes_db_fieldnames()

        # Get all grant codes information
        grant_codes_info = get_all_grant_codes_info()

        # Export the grant codes information to a CSV file
        with open('grant_codes_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for grant_code in grant_codes_info:
                row_info = {}
                for idx, value in enumerate(grant_code[1:len(grant_code)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Grant Codes information exported", "Grant Codes information exported to grant_codes_info.csv", "OK")
            msg_dialog.exec()


    def export_storage_locations(self, msg_dialog=True):
        # Get the fieldnames for the storage locations table
        fieldnames = get_locations_db_fieldnames()

        # Get all storage locations information
        storage_locations_info = get_all_locations_info()

        # Export the storage locations information to a CSV file
        with open('storage_locations_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for storage_location in storage_locations_info:
                row_info = {}
                for idx, value in enumerate(storage_location[1:len(storage_location)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Storage Locations information exported", "Storage Locations information exported to storage_locations_info.csv", "OK")
            msg_dialog.exec()


    def export_items(self, msg_dialog=True):
        # Get the fieldnames for the items table
        fieldnames = get_items_db_fieldnames()

        # Get all items information
        items_info = get_all_items_info()

        # Export the items information to a CSV file
        with open('items_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in items_info:
                row_info = {}
                for idx, value in enumerate(item[1:len(item)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Items information exported", "Items information exported to items_info.csv", "OK")
            msg_dialog.exec()


# Dropdown widget for the use database menu
class UseDBDropdownWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set the layout for the widget
        dropdown_layout = QVBoxLayout()

        # Set the panel widget
        self.dropdown_widget = MainMenuDropdownPanelWidget("Other actions:", self.select_action)
        self.dropdown_widget.cmb_dropdown.addItems(["Select Action...", 
                                                    "Export Items",
                                                    "Export Users",
                                                    "Export Suppliers",
                                                    "Export Grant Codes",
                                                    "Export Storage Locations"])
        dropdown_layout.addWidget(self.dropdown_widget)

        # Set the main layout for the widget
        self.setLayout(dropdown_layout)


    def select_action(self):
        action = self.dropdown_widget.cmb_dropdown.currentText()
        if action == "Export Users":
            self.export_users()
        elif action == "Export Suppliers":
            self.export_suppliers()
        elif action == "Export Grant Codes":
            self.export_grant_codes()
        elif action == "Export Storage Locations":
            self.export_storage_locations()
        elif action == "Export Items":
            self.export_items()


    def export_users(self, msg_dialog=True):
        # Get the fieldnames for the users table
        fieldnames = get_users_db_fieldnames()

        # Get all users information
        users_info = get_all_users_info()

        # Export the users information to a CSV file
        with open('users_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users_info:
                row_info = {}
                for idx, value in enumerate(user[1:len(user)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Users information exported", "Users information exported to users_info.csv", "OK")
            msg_dialog.exec()


    def export_suppliers(self, msg_dialog=True):
        # Get the fieldnames for the suppliers table
        fieldnames = get_suppliers_db_fieldnames()

        # Get all suppliers information
        suppliers_info = get_all_suppliers_info()

        # Export the suppliers information to a CSV file
        with open('suppliers_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for supplier in suppliers_info:
                row_info = {}
                for idx, value in enumerate(supplier[1:len(supplier)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Suppliers information exported", "Suppliers information exported to suppliers_info.csv", "OK")
            msg_dialog.exec()


    def export_grant_codes(self, msg_dialog=True):
        # Get the fieldnames for the grant codes table
        fieldnames = get_grant_codes_db_fieldnames()

        # Get all grant codes information
        grant_codes_info = get_all_grant_codes_info()

        # Export the grant codes information to a CSV file
        with open('grant_codes_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for grant_code in grant_codes_info:
                row_info = {}
                for idx, value in enumerate(grant_code[1:len(grant_code)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Grant Codes information exported", "Grant Codes information exported to grant_codes_info.csv", "OK")
            msg_dialog.exec()


    def export_storage_locations(self, msg_dialog=True):
        # Get the fieldnames for the storage locations table
        fieldnames = get_locations_db_fieldnames()

        # Get all storage locations information
        storage_locations_info = get_all_locations_info()

        # Export the storage locations information to a CSV file
        with open('storage_locations_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for storage_location in storage_locations_info:
                row_info = {}
                for idx, value in enumerate(storage_location[1:len(storage_location)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Storage Locations information exported", "Storage Locations information exported to storage_locations_info.csv", "OK")
            msg_dialog.exec()


    def export_items(self, msg_dialog=True):
        # Get the fieldnames for the items table
        fieldnames = get_items_db_fieldnames()

        # Get all items information
        items_info = get_all_items_info()

        # Export the items information to a CSV file
        with open('items_info.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in items_info:
                row_info = {}
                for idx, value in enumerate(item[1:len(item)+1]):
                    row_info[fieldnames[idx]] = str(value)
                writer.writerow(row_info)

        if msg_dialog:
            msg_dialog = MsgDialog("Items information exported", "Items information exported to items_info.csv", "OK")
            msg_dialog.exec()