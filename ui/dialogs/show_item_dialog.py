from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from ui.custom_widgets.general.form_widgets import FormLabelComboWidgetWide, FormLabelLinkButton, FormLabelTextWidget, FormLabelTextWidgetExtraWide, FormLabelTextWidgetWide
from ui.custom_widgets.general.header_widgets import FormHeaderWidget
from ui.custom_widgets.general.footer_widgets import FormFooterWidget
from ui.custom_widgets.general.button_widgets import MainMenuButton
from ui.custom_widgets.window_dialog_panels.db_item_widgets import ItemsPanelWidget, ItemsChemicalDisplayPanelWidget, FormLabelCheckBox, PictogramWidget
from core.control_functions import controller
from core.db_get_functions import get_item_info_by_id, get_supplier_info_by_id, get_storage_location_info_by_id

class ShowItemDialog(QDialog):
    def __init__(self, item_id=None):
        super().__init__()

        # Set the window size and title
        self.resize(400, 400)
        self.setWindowTitle("Show Item Information")

        # Initialise the ShowItemDialog layout and its margins (left, top, right, bottom)
        show_item_dialog_layout = QVBoxLayout()
        show_item_dialog_layout.setContentsMargins(20, 20, 20, 20)

        # Add the header widget to the show item dialog layout
        show_item_dialog_layout.addWidget(FormHeaderWidget("Show Item Information"))

        # Add stretch
        show_item_dialog_layout.addStretch()

        # Add the items panel widget to the show item dialog layout
        self.item_form = ItemsPanelWidget()
        show_item_dialog_layout.addWidget(self.item_form, alignment=Qt.AlignCenter)

        # Add spacing
        show_item_dialog_layout.addSpacing(10)

        # Add the chemical section widget to the show item dialog layout
        self.chemical_section = ItemsChemicalDisplayPanelWidget("", "")
        show_item_dialog_layout.addWidget(self.chemical_section)
        self.chemical_section.hide()

        # Add stretch
        show_item_dialog_layout.addStretch()

        # Add the universal footer widget to the show item dialog layout
        controller.close_all_windows.connect(self.close)
        show_item_dialog_layout.addWidget(FormFooterWidget())

        # Set the main layout for the window
        self.setLayout(show_item_dialog_layout)

        # Populate the form with the item information if an item ID is provided
        if item_id is not None:
            self.populate_form(item_id)
        

    def populate_form(self, item_id):
        item_info = get_item_info_by_id(item_id)

        info_idx = [1, 3, 4, 5, 6, 8, 9, 13]
        for idx, field in enumerate(self.item_form.findChildren(FormLabelTextWidgetWide)):
            if idx == 4:
                field.txt.setText(str(item_info[info_idx[idx]]))
            elif idx == 5:
                field.txt.setText(str(item_info[info_idx[idx]]))
            else:
                field.txt.setText(item_info[info_idx[idx]])

        info_idx = [2, 7, 12]
        for idx, field in enumerate(self.item_form.findChildren(FormLabelComboWidgetWide)):
            if idx == 0:
                supplier = get_supplier_info_by_id(item_info[info_idx[idx]])
                field.cmb.setCurrentText(supplier[1])
            elif idx == 1:
                storage_location = get_storage_location_info_by_id(item_info[info_idx[idx]])
                field.cmb.setCurrentText(storage_location[1])
            else:
                field.cmb.setCurrentText(item_info[info_idx[idx]])

        info_idx = 10
        field = self.item_form.findChildren(FormLabelCheckBox)[0]
        field.chb.setChecked(item_info[info_idx])

        # If the item is a chemical, show the chemical section and populate the chemical information
        if item_info[12] == "Hazardous Chemical":
            self.chemical_section.show()
            self.chemical_flag_1 = True

            info_idx = [14]
            for idx, field in enumerate(self.chemical_section.findChildren(FormLabelTextWidgetExtraWide)):
                field.txt.setText(item_info[info_idx[idx]])

            info_idx = [15, 16]
            for idx, field in enumerate(self.chemical_section.findChildren(FormLabelLinkButton)):
                field.btn.setText(item_info[info_idx[idx]])

            info_idx = [17, 18, 19, 20, 21, 22, 23, 24, 25]
            for idx, field in enumerate(self.chemical_section.findChildren(PictogramWidget)):
                field.chb.setChecked(item_info[info_idx[idx]])
        else:
            self.chemical_section.hide()
