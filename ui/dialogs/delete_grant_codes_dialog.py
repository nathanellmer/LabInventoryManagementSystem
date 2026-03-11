from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidget
from ui.custom_widgets.window_dialog_panels.db_grant_code_widgets import GrantCodesPanelWidget
from ui.dialogs.choice_selection_dialog import ChoiceSelectionDialogTwo
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_grant_code_info_by_grant_code_name, get_grant_code_info_by_grant_code_owner
from core.db_delete_functions import delete_grant_code_from_db


class DeleteGrantCodesDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(500, 400)
        self.setWindowTitle("Delete Grant Code from Database")

        # Initialise the DeleteGrantCodesDialog layout and its margins (left, top, right, bottom)
        del_grant_code_dialog_layout = QVBoxLayout()
        del_grant_code_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the delete grant code dialog layout
        del_grant_code_dialog_layout.addWidget(FormHeaderWidget("Delete Grant Code Information:"))

        # Add stretch
        del_grant_code_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a grant code:", "Grant Code / Owner:", self.btn_search)
        del_grant_code_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        del_grant_code_dialog_layout.addStretch()

        # Add the grant code panel widget to the delete grant code dialog layout
        self.grant_code_form = GrantCodesPanelWidget()
        del_grant_code_dialog_layout.addWidget(self.grant_code_form, alignment=Qt.AlignCenter)

        # Add spacing
        del_grant_code_dialog_layout.addSpacing(10)

        # Add a proceed button
        del_grant_code_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        del_grant_code_dialog_layout.addStretch()

        # Add the universal footer widget to the delete grant code dialog layout
        controller.close_all_windows.connect(self.close)
        del_grant_code_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(del_grant_code_dialog_layout)
        

    def btn_search(self):
        # Gather the data from the form
        field_values = []

        for field in self.search_panel.findChildren(FormLabelTextWidget):
            field_values.append(field.txt.text())

        # Search the database for the grant code by code
        grant_codes_by_name = get_grant_code_info_by_grant_code_name(field_values[0])

        # Search the database for the grant code by owner
        grant_codes_by_owner = get_grant_code_info_by_grant_code_owner(field_values[0])

        choice_selection_dialog = ChoiceSelectionDialogTwo("Multiple Grant Codes Found", "Multiple grant codes were found matching your search. Please select one:", "Grant Codes by Name:", "Grant Codes by Owner:", [grant_code[1] for grant_code in grant_codes_by_name], [grant_code[1] for grant_code in grant_codes_by_owner])
        if choice_selection_dialog.exec() == QDialog.Accepted:
            selected_optn = choice_selection_dialog.selected_option
            selected_idx = choice_selection_dialog.selected_idx

            if selected_optn == 1:
                selected_grant_code = grant_codes_by_name[selected_idx]
            else:
                selected_grant_code = grant_codes_by_owner[selected_idx]

            self.grant_code_id = selected_grant_code[0] 
            
            for idx, field in enumerate(self.grant_code_form.findChildren(FormLabelTextWidget)):
                field.txt.setText(selected_grant_code[idx + 1])


    def btn_proceed(self):
        # Gather the data from the form
        grant_code_id = self.grant_code_id

        # Delete the grant code from the database
        delete_grant_code_from_db(grant_code_id)
        self.close()
