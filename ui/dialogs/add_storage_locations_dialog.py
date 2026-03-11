from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.custom_widgets.general.form_widgets import FormLabelTextWidgetWide
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.window_dialog_panels.db_storage_location_widgets import StorageLocationsPanelWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_add_functions import add_storage_location_to_db

class AddStorageLocationsDialog(QDialog):
    # Signal to trigger update
    db_updated = Signal()

    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Add Storage Locations to Database")

        # Initialise the AddStorageLocationsDialog layout and its margins (left, top, right, bottom)
        add_storage_locations_dialog_layout = QVBoxLayout()
        add_storage_locations_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the add storage locations dialog layout
        add_storage_locations_dialog_layout.addWidget(FormHeaderWidget("Add a New Storage Location to the Database:"))

        # Add stretch
        add_storage_locations_dialog_layout.addStretch()

        # Add the storage location panel widget to the add storage locations dialog layout
        self.storage_location_form = StorageLocationsPanelWidget()
        add_storage_locations_dialog_layout.addWidget(self.storage_location_form, alignment=Qt.AlignCenter)

        # Add spacing
        add_storage_locations_dialog_layout.addSpacing(10)

        # Add a proceed button
        add_storage_locations_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        add_storage_locations_dialog_layout.addStretch()

        # Add the universal footer widget to the add storage locations dialog layout
        controller.close_all_windows.connect(self.close)
        add_storage_locations_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(add_storage_locations_dialog_layout)
        

    def btn_proceed(self):
        field_values = []
        complete_flag = True

        for field in self.storage_location_form.findChildren(FormLabelTextWidgetWide):
            if field.txt.text() == "":
                # If field is empty
                complete_flag = False
            else:
                # Otherwise add the field value to the list
                field_values.append(field.txt.text())

        if complete_flag:
            # Add the new storage location to the database
            dialog_close = add_storage_location_to_db(field_values)

            # Emit the signal to trigger the update in the welcome window
            self.db_updated.emit()

            # Close the dialog
            if dialog_close:
                self.close()
        else:
            # If any field is empty, show an error message
            msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
            msg_dialog.exec_()
