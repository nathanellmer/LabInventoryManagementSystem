from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.window_dialog_panels.db_supplier_widgets import SupplierPanelWidget
from ui.custom_widgets.general.form_widgets import FormLabelTextWidgetWide
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_add_functions import add_supplier_to_db

class AddSupplierDialog(QDialog):
    # Signal to trigger update
    db_updated = Signal()

    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(500, 400)
        self.setWindowTitle("Add Supplier to Database")

        # Initialise the AddSupplierDialog layout and its margins (left, top, right, bottom)
        add_supplier_dialog_layout = QVBoxLayout()
        add_supplier_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the add supplier dialog layout
        add_supplier_dialog_layout.addWidget(FormHeaderWidget("Add a New Supplier to the Database:"))

        # Add stretch
        add_supplier_dialog_layout.addStretch()

        # Add the supplier panel widget to the add supplier dialog layout
        self.supplier_form = SupplierPanelWidget()
        add_supplier_dialog_layout.addWidget(self.supplier_form, alignment=Qt.AlignCenter)

        # Add spacing
        add_supplier_dialog_layout.addSpacing(10)

        # Add a proceed button
        add_supplier_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        add_supplier_dialog_layout.addStretch()

        # Add the universal footer widget to the add supplier dialog layout
        controller.close_all_windows.connect(self.close)
        add_supplier_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(add_supplier_dialog_layout)
        

    def btn_proceed(self):
        field_values = []
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
            dialog_close = add_supplier_to_db(field_values)

            # Emit the signal to trigger the update in the welcome window
            self.db_updated.emit()

            # Close the dialog
            if dialog_close:
                self.close()
        else:
            # If any field is empty, show an error message
            msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
            msg_dialog.exec_()
