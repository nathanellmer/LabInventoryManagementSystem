from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidgetWide
from ui.custom_widgets.window_dialog_panels.db_supplier_widgets import SupplierPanelWidget
from core.control_functions import controller
from core.db_get_functions import get_supplier_info_by_name
from core.db_delete_functions import delete_supplier_from_db

class DeleteSupplierDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Delete Supplier from Database")

        # Initialise the DeleteSupplierDialog layout and its margins (left, top, right, bottom)
        del_supplier_dialog_layout = QVBoxLayout()
        del_supplier_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the delete supplier dialog layout
        del_supplier_dialog_layout.addWidget(FormHeaderWidget("Delete Supplier Information:"))

        # Add stretch
        del_supplier_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a supplier:", "Supplier Name:", self.btn_search)
        del_supplier_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        del_supplier_dialog_layout.addStretch()

        # Add the supplier panel widget to the delete supplier dialog layout
        self.supplier_form = SupplierPanelWidget()
        del_supplier_dialog_layout.addWidget(self.supplier_form, alignment=Qt.AlignCenter)

        # Add spacing
        del_supplier_dialog_layout.addSpacing(10)

        # Add a proceed button
        del_supplier_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        del_supplier_dialog_layout.addStretch()

        # Add the universal footer widget to the delete supplier dialog layout
        controller.close_all_windows.connect(self.close)
        del_supplier_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(del_supplier_dialog_layout)
        

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
        # Gather the data from the form
        supplier_id = self.supplier_id

        # Delete the supplier from the database
        delete_supplier_from_db(supplier_id)
        self.close()
