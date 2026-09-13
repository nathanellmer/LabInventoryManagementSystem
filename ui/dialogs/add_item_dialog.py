from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.custom_widgets.general.form_widgets import FormLabelComboWidgetWide, FormLabelTextWidget, FormLabelTextWidgetExtraWide, FormLabelTextWidgetWide
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.window_dialog_panels.db_item_widgets import HazardousItemsChemicalPanelWidget, ItemsPanelWidget, ItemsChemicalPanelWidget, FormLabelCheckBox, NonHazardousItemsChemicalPanelWidget, PictogramWidget
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_add_functions import add_item_to_db
from core.db_get_functions import get_user_info_by_username, get_supplier_info_by_name, get_storage_location_info_by_name


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

        # Add the items panel widget to the add item dialog layout
        self.item_form = ItemsPanelWidget()
        add_item_dialog_layout.addWidget(self.item_form, alignment=Qt.AlignCenter)

        # Add spacing
        add_item_dialog_layout.addSpacing(10)

        # Add the chemical section widget to the add item dialog layout
        self.non_hazardous_chemical_section = NonHazardousItemsChemicalPanelWidget()
        add_item_dialog_layout.addWidget(self.non_hazardous_chemical_section)
        self.non_hazardous_chemical_section.hide()
        self.chemical_flag = False

        # Add spacing
        add_item_dialog_layout.addSpacing(10)

        # Add the chemical section widget to the add item dialog layout
        self.hazardous_chemical_section = HazardousItemsChemicalPanelWidget()
        add_item_dialog_layout.addWidget(self.hazardous_chemical_section)
        self.hazardous_chemical_section.hide()
        self.item_form.item_category.cmb.currentTextChanged.connect(self.toggle_chemical_section)

        # Add a proceed button
        add_item_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        add_item_dialog_layout.addStretch()

        # Add the universal footer widget to the add item dialog layout
        controller.close_all_windows.connect(self.close)
        add_item_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(add_item_dialog_layout)


    def toggle_chemical_section(self):
        if self.item_form.item_category.cmb.currentText() == "Hazardous Chemical":
            self.hazardous_chemical_section.show()
            self.non_hazardous_chemical_section.show()
            self.chemical_flag = True
        elif self.item_form.item_category.cmb.currentText() == "Non-hazardous Chemical":
            self.hazardous_chemical_section.hide()
            self.non_hazardous_chemical_section.show()
            self.chemical_flag = True
        else:
            self.hazardous_chemical_section.hide()
            self.non_hazardous_chemical_section.hide()
            self.chemical_flag = False
        

    def btn_proceed(self):
        # Initialise lists to store the field values and a flag to check if all fields are complete
        field_values_txt = []
        field_values_cmb = []
        field_values_chb = []
        field_values_chem_txt = []
        field_values_hazards = []
        complete_flag = True
        compulsory_fields = [True, True, True, True, True, False, True, False]
        compulsory_dropdowns = ["Select Supplier...", "Select Storage Location...", "Select Category..."]

        # Gather the text data from the form
        for idx, field in enumerate(self.item_form.findChildren(FormLabelTextWidgetWide)):
            field_values_txt.append(field.txt.text())

        # Gather the dropdown data from the form
        for idx, field in enumerate(self.item_form.findChildren(FormLabelComboWidgetWide)):
            field_values_cmb.append(field.cmb.currentText())

        # Gather the checkbox data from the form
        for field in self.item_form.findChildren(FormLabelCheckBox):
            field_values_chb.append(field.chb.isChecked())

        # Gather chemical data
        if self.chemical_flag:
            for field in self.hazardous_chemical_section.findChildren(FormLabelTextWidgetExtraWide):
                field_values_chem_txt.append(field.txt.text())

            for field in self.non_hazardous_chemical_section.findChildren(FormLabelTextWidget):
                field_values_chem_txt.append(field.txt.text())
            
            for field in self.hazardous_chemical_section.findChildren(PictogramWidget):
                field_values_hazards.append(field.chb.isChecked())
        else:
            field_values_chem_txt = [""] * 3
            field_values_hazards = [False] * 9


        # Add the new item to the database
        user_name = controller.logged_in_user
        user_info = get_user_info_by_username(user_name)
        supplier_info = get_supplier_info_by_name(field_values_cmb[0])
        storage_location_info = get_storage_location_info_by_name(field_values_cmb[1])
        dialog_close = add_item_to_db(field_values_txt, field_values_cmb, field_values_chb, field_values_chem_txt, field_values_hazards, user_info[0], supplier_info[0], storage_location_info[0][0])

        # Close the dialog
        if dialog_close:
            self.close()
