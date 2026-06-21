from PySide6.QtWidgets import QDialog, QHBoxLayout, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormLabelCheckBox, FormLabelComboWidgetWide, FormLabelTextWidgetWide, FormLabelTextWidgetExtraWide, FormSearchPanelWidget, FormLabelTextWidget
from ui.custom_widgets.window_dialog_panels.db_item_widgets import ItemsPanelWidget, ItemsChemicalPanelWidget, PictogramWidget
from ui.dialogs.choice_selection_dialog import ChoiceSelectionDialogFour
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_item_info_by_product_code, get_item_info_by_supplier, get_item_info_by_description, get_item_info_by_name, get_supplier_info_by_id, get_storage_location_info_by_id, get_user_info_by_username, get_supplier_info_by_name, get_storage_location_info_by_name
from core.db_update_functions import update_item_in_db

class UpdateItemDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(1250, 600)
        self.setWindowTitle("Update Item in Database")
        self.setMaximumHeight(600)

        # Initialise the UpdateItemDialog layout and its margins (left, top, right, bottom)
        upd_item_dialog_layout = QVBoxLayout()
        upd_item_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the update item dialog layout
        upd_item_dialog_layout.addWidget(FormHeaderWidget("Update Item Information:"))

        # Add stretch
        upd_item_dialog_layout.addStretch()

        # Add a search panel
        horiz_layout = QHBoxLayout()
        horiz_layout.addStretch()
        self.search_panel = FormSearchPanelWidget("Search for an item:", "Name or other information:", self.btn_search)
        horiz_layout.addWidget(self.search_panel)
        horiz_layout.addStretch()
        upd_item_dialog_layout.addLayout(horiz_layout)

        # Add stretch
        upd_item_dialog_layout.addStretch()

        # Add the items panel widget to the update item dialog layout
        self.item_form = ItemsPanelWidget()
        upd_item_dialog_layout.addWidget(self.item_form, alignment=Qt.AlignCenter)

        # Add spacing
        upd_item_dialog_layout.addSpacing(10)

        # Add the chemical section widget to the update item dialog layout
        self.chemical_flag_1 = False
        self.chemical_flag_2 = False
        self.chemical_section = ItemsChemicalPanelWidget()
        upd_item_dialog_layout.addWidget(self.chemical_section)
        self.chemical_section.hide()

        # Add a proceed button
        upd_item_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        upd_item_dialog_layout.addStretch()

        # Add the universal footer widget to the update item dialog layout
        controller.close_all_windows.connect(self.close)
        upd_item_dialog_layout.addWidget(FormFooterWidget())

        # Create a container widget for the scroll area and set its layout
        container = QWidget()
        container.setLayout(upd_item_dialog_layout)

        # Create a scroll area and set the container widget as its widget
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(container)

        # Set the main layout for the window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        

    def btn_search(self):
        # Gather the data from the form
        field_values = []

        for field in self.search_panel.findChildren(FormLabelTextWidget):
            field_values.append(field.txt.text())

        # Search the database for the item by name
        items_by_name = get_item_info_by_name(field_values[0])

        # Search the database for the item by supplier
        items_by_supplier = get_item_info_by_supplier(field_values[0])

        # Search the database for the item by product code
        items_by_ref = get_item_info_by_product_code(field_values[0])

        # Search the database for the item by description
        items_by_description = get_item_info_by_description(field_values[0])

        choice_selection_dialog = ChoiceSelectionDialogFour("Multiple Items Found", "Multiple items were found matching your search. Please select one:", "Items by Name:", "Items by Supplier:", "Items by Product Code:", "Items by Description:", [item[1] for item in items_by_name], [item[1] for item in items_by_supplier], [item[1] for item in items_by_ref], [item[1] for item in items_by_description])
        if choice_selection_dialog.exec() == QDialog.Accepted:
            selected_optn = choice_selection_dialog.selected_option
            selected_idx = choice_selection_dialog.selected_idx

            if selected_optn == 1:
                selected_item = items_by_name[selected_idx]
            elif selected_optn == 2:
                selected_item = items_by_supplier[selected_idx]
            elif selected_optn == 3:
                selected_item = items_by_ref[selected_idx]
            elif selected_optn == 4:
                selected_item = items_by_description[selected_idx]

            self.item_id = selected_item[0]

            info_idx = [1, 3, 4, 5, 6, 8, 9, 13]
            for idx, field in enumerate(self.item_form.findChildren(FormLabelTextWidgetWide)):
                if idx == 4:
                    field.txt.setText(str(selected_item[info_idx[idx]]))
                elif idx == 5:
                    field.txt.setText(str(selected_item[info_idx[idx]]))
                else:
                    field.txt.setText(selected_item[info_idx[idx]])

            info_idx = [2, 7, 12]
            for idx, field in enumerate(self.item_form.findChildren(FormLabelComboWidgetWide)):
                if idx == 0:
                    supplier = get_supplier_info_by_id(selected_item[info_idx[idx]])
                    field.cmb.setCurrentText(supplier[1])
                elif idx == 1:
                    storage_location = get_storage_location_info_by_id(selected_item[info_idx[idx]])
                    field.cmb.setCurrentText(storage_location[1])
                else:
                    field.cmb.setCurrentText(selected_item[info_idx[idx]])

            info_idx = 10
            field = self.item_form.findChildren(FormLabelCheckBox)[0]
            field.chb.setChecked(selected_item[info_idx])

            self.originator_id = selected_item[11]

            # If the item is a chemical, show the chemical section and populate the chemical information
            if selected_item[12] == "Hazardous Chemical":
                self.chemical_section.show()
                self.chemical_flag_1 = True

                info_idx = [14]
                for idx, field in enumerate(self.chemical_section.findChildren(FormLabelTextWidgetExtraWide)):
                    field.txt.setText(selected_item[info_idx[idx]])

                info_idx = [15, 16]
                for idx, field in enumerate(self.chemical_section.findChildren(FormLabelTextWidget)):
                    field.txt.setText(selected_item[info_idx[idx]])

                info_idx = [17, 18, 19, 20, 21, 22, 23, 24, 25]
                for idx, field in enumerate(self.chemical_section.findChildren(PictogramWidget)):
                    field.chb.setChecked(selected_item[info_idx[idx]])
            else:
                self.chemical_section.hide()


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

        # Check if the chemical section needs to be filled in and show/hide the chemical section accordingly
        self.check_chemical()

        if self.chemical_flag_2:
            self.chemical_section.show()
        else:
            self.chemical_section.hide()

        if self.chemical_flag_1 == self.chemical_flag_2:

            # Gather the text data from the form
            for idx, field in enumerate(self.item_form.findChildren(FormLabelTextWidgetWide)):
                if field.txt.text() == "":
                    if compulsory_fields[idx]:
                        # If field is empty
                        complete_flag = False
                    else:
                        # If field is empty but not compulsory, add an empty string to the list
                        field_values_txt.append("")
                    
                else:
                    # Otherwise add the field value to the list
                    field_values_txt.append(field.txt.text())

            # Gather the dropdown data from the form
            for idx, field in enumerate(self.item_form.findChildren(FormLabelComboWidgetWide)):
                if field.cmb.currentText() == compulsory_dropdowns[idx]:
                    # If field is empty
                    complete_flag = False
                    
                else:
                    # Otherwise add the field value to the list
                    field_values_cmb.append(field.cmb.currentText())

            # Gather the checkbox data from the form
            for field in self.item_form.findChildren(FormLabelCheckBox):
                field_values_chb.append(field.chb.isChecked())

            # Gather the chemical section data from the form if the chemical section is visible
            if self.chemical_flag_1:
                for field in self.chemical_section.findChildren(FormLabelTextWidgetExtraWide):
                    if field.txt.text() == "":
                        # If field is empty
                        complete_flag = False
                        
                    else:
                        # Otherwise add the field value to the list
                        field_values_chem_txt.append(field.txt.text())

                for field in self.chemical_section.findChildren(FormLabelTextWidget):
                    if field.txt.text() == "":
                        # If field is empty
                        complete_flag = False
                        
                    else:
                        # Otherwise add the field value to the list
                        field_values_chem_txt.append(field.txt.text())

                for field in self.chemical_section.findChildren(PictogramWidget):
                    field_values_hazards.append(field.chb.isChecked())

            else:
                # If the chemical section is not visible, add empty values for the chemical text fields and hazard checkboxes
                field_values_chem_txt = [""] * 3
                field_values_hazards = [False] * 9

            if complete_flag:
                # Add the new item to the database
                item_id = self.item_id
                user_id = self.originator_id
                supplier_info = get_supplier_info_by_name(field_values_cmb[0])
                storage_location_info = get_storage_location_info_by_name(field_values_cmb[1])
                dialog_close = update_item_in_db(item_id, field_values_txt, field_values_cmb, field_values_chb, field_values_chem_txt, field_values_hazards, user_id, supplier_info[0], storage_location_info[0][0])

                # Close the dialog
                if dialog_close:
                    self.close()
            else:
                # If any field is empty, show an error message
                msg_dialog = MsgDialog("Input Error", "Please fill in all fields.", "OK")
                msg_dialog.exec_()

        else:
            self.chemical_flag_1 = self.chemical_flag_2


    def check_chemical(self):
        if self.item_form.item_category.cmb.currentText() == "Hazardous Chemical":
            self.chemical_flag_2 = True
        else:
            self.chemical_flag_2 = False
