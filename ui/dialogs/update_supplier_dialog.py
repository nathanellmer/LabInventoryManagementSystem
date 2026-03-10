from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidgetWide
from ui.custom_widgets.window_dialog_panels.db_supplier_widgets import SupplierPanelWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_supplier_info_by_name
from core.db_update_functions import update_supplier_in_db

class UpdateSupplierDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Update Supplier in Database")

        # Initialise the UpdateSupplierDialog layout and its margins (left, top, right, bottom)
        upd_supplier_dialog_layout = QVBoxLayout()
        upd_supplier_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the update supplier dialog layout
        upd_supplier_dialog_layout.addWidget(FormHeaderWidget("Update Supplier Information:"))

        # Add stretch
        upd_supplier_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a supplier:", "Supplier Name:", self.btn_search)
        upd_supplier_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        upd_supplier_dialog_layout.addStretch()

        # Add the supplier panel widget to the update supplier dialog layout
        self.supplier_form = SupplierPanelWidget()
        upd_supplier_dialog_layout.addWidget(self.supplier_form, alignment=Qt.AlignCenter)

        # Add spacing
        upd_supplier_dialog_layout.addSpacing(10)

        # Add a proceed button
        upd_supplier_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        upd_supplier_dialog_layout.addStretch()

        # Add the universal footer widget to the update supplier dialog layout
        controller.close_all_windows.connect(self.close)
        upd_supplier_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(upd_supplier_dialog_layout)
        

    def btn_search(self):
        # Gather the data from the form
        supplier_name = self.search_panel.search_txt.txt.text()

        # Search the database for the supplier
        supplier_info = get_supplier_info_by_name(supplier_name)

        # Populate the supplier form with the retrieved information
        if supplier_info:
            self.supplier_id = supplier_info[0]
            
            for idx, field in enumerate(self.supplier_form.findChildren(FormLabelTextWidgetWide)):
                field.txt.setText(supplier_info[idx + 1])


    def btn_proceed(self):
        field_values = [self.supplier_id]
        complete_flag = True

        for field in self.supplier_form.findChildren(FormLabelTextWidgetWide):
            if field.txt.text() == "":
                # If field is empty
                complete_flag = False
            else:
                # Otherwise add the field value to the list
                field_values.append(field.txt.text())

        if complete_flag:
            # Add the new supplier to the database
            dialog_close = update_supplier_in_db(field_values)

            # Close the dialog
            if dialog_close:
                self.close()
        else:
            # If any field is empty, show an error message
            msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
            msg_dialog.exec_()
