from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidget, FormLabelTextWidgetWide
from ui.custom_widgets.window_dialog_panels.db_storage_location_widgets import StorageLocationsPanelWidget
from ui.dialogs.choice_selection_dialog import ChoiceSelectionDialogOne
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_storage_location_info_by_name
from core.db_delete_functions import delete_storage_location_from_db

class DeleteStorageLocationsDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(500, 400)
        self.setWindowTitle("Delete Storage Location from Database")

        # Initialise the DeleteStorageLocationsDialog layout and its margins (left, top, right, bottom)
        del_storage_location_dialog_layout = QVBoxLayout()
        del_storage_location_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the delete storage location dialog layout
        del_storage_location_dialog_layout.addWidget(FormHeaderWidget("Delete Storage Location Information:"))

        # Add stretch
        del_storage_location_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a storage location:", "Storage Location:", self.btn_search)
        del_storage_location_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        del_storage_location_dialog_layout.addStretch()

        # Add the storage location panel widget to the delete storage location dialog layout
        self.storage_locations_form = StorageLocationsPanelWidget()
        del_storage_location_dialog_layout.addWidget(self.storage_locations_form, alignment=Qt.AlignCenter)

        # Add spacing
        del_storage_location_dialog_layout.addSpacing(10)

        # Add a proceed button
        del_storage_location_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        del_storage_location_dialog_layout.addStretch()

        # Add the universal footer widget to the delete storage location dialog layout
        controller.close_all_windows.connect(self.close)
        del_storage_location_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(del_storage_location_dialog_layout)
        

    def btn_search(self):
        # Gather the data from the form
        field_values = []

        for field in self.search_panel.findChildren(FormLabelTextWidget):
            field_values.append(field.txt.text())

        # Search the database for the storage location by name
        storage_locations = get_storage_location_info_by_name(field_values[0])

        if len(storage_locations) == 1:
            selected_storage_location = storage_locations[0]
            self.location_id = selected_storage_location[0] 
        else:
            choice_selection_dialog = ChoiceSelectionDialogOne("Multiple Storage Locations Found", "Multiple storage locations were found matching your search. Please select one:", "Storage Locations:", [location[1] for location in storage_locations])
            if choice_selection_dialog.exec() == QDialog.Accepted:
                selected_idx = choice_selection_dialog.selected_idx
                selected_storage_location = storage_locations[selected_idx]
                self.location_id = selected_storage_location[0] 
            
        for idx, field in enumerate(self.storage_locations_form.findChildren(FormLabelTextWidgetWide)):
            field.txt.setText(selected_storage_location[idx + 1])


    def btn_proceed(self):
        # Gather the data from the form
        location_id = self.location_id

        # Delete the storage location from the database
        delete_storage_location_from_db(location_id)
        self.close()
