from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidget
from ui.custom_widgets.window_dialog_panels.db_grant_code_widgets import GrantCodesPanelWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_grant_code_info_by_grant_code_name, get_grant_code_info_by_grant_code_owner
from core.db_update_functions import update_user_in_db

class UpdateGrantCodesDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Update Grant Code in Database")

        # Initialise the UpdateGrantCodesDialog layout and its margins (left, top, right, bottom)
        upd_grant_code_dialog_layout = QVBoxLayout()
        upd_grant_code_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the update grant code dialog layout
        upd_grant_code_dialog_layout.addWidget(FormHeaderWidget("Update Grant Code Information:"))

        # Add stretch
        upd_grant_code_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a grant code:", "Grant Code / Owner:", self.btn_search)
        upd_grant_code_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        upd_grant_code_dialog_layout.addStretch()

        # Add the grant code panel widget to the update grant code dialog layout
        self.grant_code_form = GrantCodesPanelWidget()
        upd_grant_code_dialog_layout.addWidget(self.grant_code_form, alignment=Qt.AlignCenter)

        # Add spacing
        upd_grant_code_dialog_layout.addSpacing(10)

        # Add a proceed button
        upd_grant_code_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        upd_grant_code_dialog_layout.addStretch()

        # Add the universal footer widget to the update grant code dialog layout
        controller.close_all_windows.connect(self.close)
        upd_grant_code_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(upd_grant_code_dialog_layout)
        

    def btn_search(self):
        # Gather the data from the form
        field_values = []

        for field in self.search_panel.findChildren(FormLabelTextWidget):
            field_values.append(field.txt.text())

        # Search the database for the grant code by code
        grant_codes_by_name = get_grant_code_info_by_grant_code_name(field_values[0])
        print(grant_codes_by_name)

        # Search the database for the grant code by owner
        grant_codes_by_owner = get_grant_code_info_by_grant_code_owner(field_values[0])
        print(grant_codes_by_owner)

        # # Populate the user form with the retrieved information
        # if user_info:
        #     self.user_id = user_info[0] 
            
        #     for idx, field in enumerate(self.user_form.findChildren(FormLabelTextWidget)):
        #         field.txt.setText(user_info[idx + 1])

        #     if controller.logged_in_user == user_info[1]:
        #         self.current_user = True
        #     else:
        #         self.current_user = False


    def btn_proceed(self):
    #     field_values = [self.user_id]
        complete_flag = True

    #     for field in self.user_form.findChildren(FormLabelTextWidget):
    #         if field.txt.text() == "":
    #             # If field is empty
    #             complete_flag = False
    #         else:
    #             # Otherwise add the field value to the list
    #             field_values.append(field.txt.text())

    #     if complete_flag:
    #         # Add the new user to the database
    #         dialog_close = update_user_in_db(field_values)

    #         # Close the dialog
    #         if dialog_close:
    #             if self.current_user:
    #                 controller.logged_in_user = field_values[1]

    #             self.close()
    #     else:
    #         # If any field is empty, show an error message
    #         msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
    #         msg_dialog.exec_()
