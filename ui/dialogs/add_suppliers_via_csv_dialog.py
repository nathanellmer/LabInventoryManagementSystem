import csv
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QVBoxLayout, QFileDialog
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.window_dialog_panels.csv_interaction_widgets import CSVPanelWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_add_functions import add_supplier_to_db
from core.db_get_functions import get_suppliers_db_fieldnames

class AddSuppliersCSVDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Add Suppliers via CSV to Database")

        # Initialise the AddSuppliersCSVDialog layout and its margins (left, top, right, bottom)
        add_suppliers_csv_dialog_layout = QVBoxLayout()
        add_suppliers_csv_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the add item dialog layout
        add_suppliers_csv_dialog_layout.addWidget(FormHeaderWidget("Add Suppliers via CSV to Database:"))

        # Add stretch
        add_suppliers_csv_dialog_layout.addStretch()

        # Add the CSV panel widget
        self.csv_panel = CSVPanelWidget(self.btn_blank_csv, self.btn_upload_csv)
        add_suppliers_csv_dialog_layout.addWidget(self.csv_panel, stretch=1)

        # Add spacing
        add_suppliers_csv_dialog_layout.addSpacing(10)

        # Add a proceed button
        add_suppliers_csv_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        add_suppliers_csv_dialog_layout.addStretch()

        # Add the universal footer widget to the add item dialog layout
        controller.close_all_windows.connect(self.close)
        add_suppliers_csv_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(add_suppliers_csv_dialog_layout)


    def btn_blank_csv(self):
        # Create a blank CSV template with the appropriate headers
        headers = get_suppliers_db_fieldnames()
        with open("supplier_csv_template.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

        # Show a message dialog to indicate that the blank CSV template has been created
        msg_dialog = MsgDialog("CSV Template Created", "A blank CSV template has been created in the current folder.", "OK")
        msg_dialog.exec_()


    def btn_upload_csv(self):
        # Initialise the table widget
        headers = get_suppliers_db_fieldnames()
        self.csv_panel.csv_table.setColumnCount(len(headers))
        self.csv_panel.csv_table.setHorizontalHeaderLabels(headers)

        # Initialise a list to store the items from the CSV file
        self.csv_suppliers = []

        # Open a file dialog to select a CSV file to upload
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV files (*.csv)")
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            # Read the CSV file and add the items to the database
            with open(selected_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row_idx, row in enumerate(reader):
                    self.csv_panel.csv_table.insertRow(row_idx)
                    for col_idx, key in enumerate(row):
                        self.csv_panel.csv_table.setItem(row_idx, col_idx, QTableWidgetItem(row[key]))
                    self.csv_suppliers.append(row)


    def btn_proceed(self):
        # Loop through items to add
        for item in self.csv_suppliers:
            # Initialise lists to store the field values and a flag to check if all fields are complete
            field_values = []

            # Populate the field values lists
            for key in item:
                field_values.append(item[key])

            # Add the new item to the database
            dialog_close = add_supplier_to_db(field_values, False)

            # Close the dialog
            if dialog_close:
                self.close()

        # Show a message dialog to confirm the suppliers have been added
        msg_dialog = MsgDialog("Suppliers Added", "The suppliers from the CSV file have been added to the database.", "OK")
        msg_dialog.exec_()
