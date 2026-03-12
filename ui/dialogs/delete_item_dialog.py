from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.general.form_widgets import FormLabelCheckBox, FormLabelComboWidgetWide, FormLabelTextWidgetWide, FormSearchPanelWidget, FormLabelTextWidget
from ui.custom_widgets.window_dialog_panels.db_item_widgets import ItemsPanelWidget, ItemsChemicalPanelWidget, PictogramWidget
from ui.dialogs.choice_selection_dialog import ChoiceSelectionDialogFour
from ui.dialogs.msg_dialog import MsgDialog
from core.control_functions import controller
from core.db_get_functions import get_item_info_by_product_code, get_item_info_by_supplier, get_item_info_by_description, get_item_info_by_name, get_supplier_info_by_id, get_storage_location_info_by_id, get_user_info_by_username, get_supplier_info_by_name, get_storage_location_info_by_name
from core.db_delete_functions import delete_item_from_db

class DeleteItemDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.resize(500, 400)
        self.setWindowTitle("Delete Item from Database")

        # Initialise the DeleteItemDialog layout and its margins (left, top, right, bottom)
        del_item_dialog_layout = QVBoxLayout()
        del_item_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the delete item dialog layout
        del_item_dialog_layout.addWidget(FormHeaderWidget("Delete Item Information:"))

        # Add stretch
        del_item_dialog_layout.addStretch()

        # Add a search panel
        horiz_layout = QHBoxLayout()
        horiz_layout.addStretch()
        self.search_panel = FormSearchPanelWidget("Search for an item:", "Name or other information:", self.btn_search)
        horiz_layout.addWidget(self.search_panel)
        horiz_layout.addStretch()
        del_item_dialog_layout.addLayout(horiz_layout)

        # Add stretch
        del_item_dialog_layout.addStretch()

        # Add the items panel widget to the delete item dialog layout
        self.item_form = ItemsPanelWidget()
        del_item_dialog_layout.addWidget(self.item_form, alignment=Qt.AlignCenter)

        # Add spacing
        del_item_dialog_layout.addSpacing(10)

        # Add the chemical section widget to the delete item dialog layout
        self.chemical_flag_1 = False
        self.chemical_flag_2 = False
        self.chemical_section = ItemsChemicalPanelWidget()
        del_item_dialog_layout.addWidget(self.chemical_section)
        self.chemical_section.hide()

        # Add a proceed button
        del_item_dialog_layout.addWidget(MainMenuButton("Proceed", self.btn_proceed), alignment=Qt.AlignCenter)

        # Add stretch
        del_item_dialog_layout.addStretch()

        # Add the universal footer widget to the delete item dialog layout
        controller.close_all_windows.connect(self.close)
        del_item_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(del_item_dialog_layout)
        

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
                for idx, field in enumerate(self.chemical_section.findChildren(FormLabelTextWidget)):
                    field.txt.setText(selected_item[info_idx[idx]])

                info_idx = [15, 16, 17, 18, 19, 20, 21, 22, 23]
                for idx, field in enumerate(self.chemical_section.findChildren(PictogramWidget)):
                    field.chb.setChecked(selected_item[info_idx[idx]])
            else:
                self.chemical_section.hide()


    def btn_proceed(self):
        # Gather the data from the form
        item_id = self.item_id
        
        # Delete the storage location from the database
        delete_item_from_db(item_id)
        self.close()


    def check_chemical(self):
        if self.item_form.item_category.cmb.currentText() == "Hazardous Chemical":
            self.chemical_flag_2 = True
        else:
            self.chemical_flag_2 = False
