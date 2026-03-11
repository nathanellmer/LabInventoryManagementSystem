from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.custom_widgets.general.form_widgets import FormLabelTextWidget
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.window_dialog_panels.db_item_widgets import ItemsPanelWidget, ItemsChemicalPanelWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_add_functions import add_user_to_db

class AddItemDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Add Item to Database")

        # Initialise the AddItemDialog layout and its margins (left, top, right, bottom)
        add_item_dialog_layout = QVBoxLayout()
        add_item_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the add item dialog layout
        add_item_dialog_layout.addWidget(FormHeaderWidget("Add a New Item to the Database:"))

        # Add stretch
        add_item_dialog_layout.addStretch()

        # Add the user panel widget to the add item dialog layout
        self.item_form = ItemsPanelWidget()
        add_item_dialog_layout.addWidget(self.item_form, alignment=Qt.AlignCenter)

        # Add spacing
        add_item_dialog_layout.addSpacing(10)

        # Add a proceed button
        add_item_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add the pictogram widget to the add item dialog layout
        self.chemical_flag = False
        self.chemical_section = ItemsChemicalPanelWidget()
        add_item_dialog_layout.addWidget(self.chemical_section)
        self.chemical_section.hide()

        # Add stretch
        add_item_dialog_layout.addStretch()

        # Add the universal footer widget to the add item dialog layout
        controller.close_all_windows.connect(self.close)
        add_item_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(add_item_dialog_layout)
        

    def btn_proceed(self):
        field_values = []
        complete_flag = True

        self.check_chemical()

        if self.chemical_flag:
            self.chemical_section.show()
        else:
            self.chemical_section.hide()

        # for field in self.user_form.findChildren(FormLabelTextWidget):
        #     if field.txt.text() == "":
        #         # If field is empty
        #         complete_flag = False
        #     else:
        #         # Otherwise add the field value to the list
        #         field_values.append(field.txt.text())

        # if complete_flag:
        #     # Add the new user to the database
        #     dialog_close = add_user_to_db(field_values)

        #     # Emit the signal to trigger the update in the welcome window
        #     self.db_updated.emit()

        #     # Close the dialog
        #     if dialog_close:
        #         self.close()
        # else:
        #     # If any field is empty, show an error message
        #     msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
        #     msg_dialog.exec_()


    def check_chemical(self):
        if self.item_form.item_category.cmb.currentText() == "Hazardous Chemical":
            self.chemical_flag = True
        else:
            self.chemical_flag = False

    
