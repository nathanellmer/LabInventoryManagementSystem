from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormSearchPanelWidget, FormLabelTextWidget
from ui.custom_widgets.window_dialog_panels.db_user_widgets import UserPanelWidget
from core.control_functions import controller
from core.db_get_functions import get_user_info_by_username
from core.db_delete_functions import delete_user_from_db
from ui.dialogs.msg_dialog import MsgDialog

class DeleteUserDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Initialise variables for user_id
        self.user_id = None
        self.current_user = None

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Delete User from Database")

        # Initialise the DeleteUserDialog layout and its margins (left, top, right, bottom)
        del_user_dialog_layout = QVBoxLayout()
        del_user_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the delete user dialog layout
        del_user_dialog_layout.addWidget(FormHeaderWidget("Delete User Information:"))

        # Add stretch
        del_user_dialog_layout.addStretch()

        # Add a search panel
        self.search_panel = FormSearchPanelWidget("Search for a user:", "Username:", self.btn_search)
        del_user_dialog_layout.addWidget(self.search_panel)

        # Add stretch
        del_user_dialog_layout.addStretch()

        # Add the user panel widget to the delete user dialog layout
        self.user_form = UserPanelWidget()
        del_user_dialog_layout.addWidget(self.user_form, alignment=Qt.AlignCenter)

        # Add spacing
        del_user_dialog_layout.addSpacing(10)

        # Add a proceed button
        del_user_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        del_user_dialog_layout.addStretch()

        # Add the universal footer widget to the delete user dialog layout
        controller.close_all_windows.connect(self.close)
        del_user_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(del_user_dialog_layout)
        

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
        # Gather the data from the form
        user_id = self.user_id

        # Check if the user to be deleted is the currently logged in user
        if self.current_user:
            msg_dialog = MsgDialog("Error Deleting User", f"Cannot delete the currently logged-in user.", "OK")
            msg_dialog.exec()
        else:
            # Delete the user from the database
            delete_user_from_db(user_id)
            self.close()
