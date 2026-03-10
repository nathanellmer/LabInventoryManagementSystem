from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidget
from ui.custom_widgets.window_dialog_panels.db_user_widgets import UserPanelWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_user_info_by_username
from core.db_update_functions import update_user_in_db

class UpdateUserDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Initialise variables for user_id
        self.user_id = None
        self.current_user = None

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Update User in Database")

        # Initialise the UpdateUserDialog layout and its margins (left, top, right, bottom)
        upd_user_dialog_layout = QVBoxLayout()
        upd_user_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the update user dialog layout
        upd_user_dialog_layout.addWidget(FormHeaderWidget("Update User Information:"))

        # Add stretch
        upd_user_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a user:", "Username:", self.btn_search)
        upd_user_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        upd_user_dialog_layout.addStretch()

        # Add the user panel widget to the update user dialog layout
        self.user_form = UserPanelWidget()
        upd_user_dialog_layout.addWidget(self.user_form, alignment=Qt.AlignCenter)

        # Add spacing
        upd_user_dialog_layout.addSpacing(10)

        # Add a proceed button
        upd_user_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        upd_user_dialog_layout.addStretch()

        # Add the universal footer widget to the update user dialog layout
        controller.close_all_windows.connect(self.close)
        upd_user_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(upd_user_dialog_layout)
        

    def btn_search(self):
        # Gather the data from the form
        username = self.search_panel.search_txt.txt.text()

        # Search the database for the user
        user_info = get_user_info_by_username(username)

        # Populate the user form with the retrieved information
        if user_info:
            self.user_id = user_info[0] 
            
            for idx, field in enumerate(self.user_form.findChildren(FormLabelTextWidget)):
                field.txt.setText(user_info[idx + 1])

            if controller.logged_in_user == user_info[1]:
                self.current_user = True
            else:
                self.current_user = False


    def btn_proceed(self):
        field_values = [self.user_id]
        complete_flag = True

        for field in self.user_form.findChildren(FormLabelTextWidget):
            if field.txt.text() == "":
                # If field is empty
                complete_flag = False
            else:
                # Otherwise add the field value to the list
                field_values.append(field.txt.text())

        if complete_flag:
            # Add the new user to the database
            dialog_close = update_user_in_db(field_values)

            # Close the dialog
            if dialog_close:
                if self.current_user:
                    controller.logged_in_user = field_values[1]

                self.close()
        else:
            # If any field is empty, show an error message
            msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
            msg_dialog.exec_()
