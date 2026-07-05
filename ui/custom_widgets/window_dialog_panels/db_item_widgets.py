from PySide6.QtWidgets import QCheckBox, QHBoxLayout, QWidget, QGridLayout, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from ui.custom_widgets.general.form_widgets import FormLabelHyperlinkButton, FormLabelTextWidget, FormLabelTextWidgetWide, FormLabelTextWidgetExtraWide, FormLabelComboWidgetWide, FormLabelLinkButton, FormLabelCheckBox
from ui.dialogs.add_supplier_dialog import AddSupplierDialog
from ui.dialogs.add_storage_locations_dialog import AddStorageLocationsDialog
from core.db_get_functions import get_all_suppliers, get_all_storage_locations
from core.utility_functions import resource_path
from core.control_functions import db_info
import os

# Panel widget for the items based database information
class ItemsPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QGridLayout()

        # Add a form label/line edit widget for the new item name
        self.item_name = FormLabelTextWidgetWide("Name:")
        form_panel_layout.addLayout(self.item_name, 0, 0)

        # Add a form label/line edit widget for the new item supplier
        self.item_supplier = FormLabelComboWidgetWide("Supplier:")
        self.load_suppliers()
        form_panel_layout.addLayout(self.item_supplier, 1, 0)

        # Add a link button widget for missing supplier information
        self.btn_missing_supplier = FormLabelLinkButton("I cannot find the supplier...", self.open_add_supplier_dialog)
        form_panel_layout.addLayout(self.btn_missing_supplier, 2, 0, alignment=Qt.AlignLeft)

        # Add a form label/line edit widget for the new item product number
        self.item_product_number = FormLabelTextWidgetWide("Product Number:")
        form_panel_layout.addLayout(self.item_product_number, 3, 0)

        # Add a form label/line edit widget for the new item description
        self.item_description = FormLabelTextWidgetWide("Description:")
        form_panel_layout.addLayout(self.item_description, 4, 0)

        # Add a form label/line edit widget for the new item size
        self.item_size = FormLabelTextWidgetWide("Size/Volume:")
        form_panel_layout.addLayout(self.item_size, 5, 0)

        # Add a form label/line edit widget for the new item quantity
        self.item_quantity = FormLabelTextWidgetWide("Quantity:")
        form_panel_layout.addLayout(self.item_quantity, 6, 0)

        # Add a form label/line edit widget for the new item unit cost
        self.item_unit_cost = FormLabelTextWidgetWide("Unit Cost:")
        form_panel_layout.addLayout(self.item_unit_cost, 0, 1)

        # Add a form label/line edit widget for the new item storage location
        self.item_storage_location = FormLabelComboWidgetWide("Storage Location:")
        self.load_storage_locations()
        form_panel_layout.addLayout(self.item_storage_location, 1, 1)

        # Add a link button widget for missing storage location
        self.btn_missing_storage_location = FormLabelLinkButton("I cannot find the storage location...", self.open_add_storage_location_dialog)
        form_panel_layout.addLayout(self.btn_missing_storage_location, 2, 1, alignment=Qt.AlignLeft)

        # Add a form label/line edit widget for the new item website
        self.item_website = FormLabelTextWidgetWide("Website:")
        form_panel_layout.addLayout(self.item_website, 3, 1)

        # Add a checkbox widget for the new item reorder flag
        self.item_reorder_flag = FormLabelCheckBox("Reorder Flag:")
        form_panel_layout.addLayout(self.item_reorder_flag, 4, 1, alignment=Qt.AlignLeft)

        # Add item category 
        self.item_category = FormLabelComboWidgetWide("Category:")
        self.item_category.cmb.addItems(["Select Category...", "Consumable", "Equipment", "Non-hazardous Chemical", "Hazardous Chemical"])
        form_panel_layout.addLayout(self.item_category, 5, 1)

        # Add item notes
        self.item_notes = FormLabelTextWidgetWide("Notes:")
        form_panel_layout.addLayout(self.item_notes, 6, 1)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)


    def load_suppliers(self):
        # Clear suppliers from the dropdown
        self.item_supplier.cmb.clear()

        # Get the list of suppliers from the database and add them to the dropdown
        suppliers = get_all_suppliers()
        suppliers.insert(0, "Select Supplier...")
        self.item_supplier.cmb.addItems(suppliers)

    def load_storage_locations(self):
        # Clear storage locations from the dropdown
        self.item_storage_location.cmb.clear()

        # Get the list of storage locations from the database and add them to the dropdown
        locations = get_all_storage_locations()
        locations.insert(0, "Select Storage Location...")
        self.item_storage_location.cmb.addItems(locations)


    def open_add_supplier_dialog(self):
        add_supplier_dialog = AddSupplierDialog()
        add_supplier_dialog.exec()
        self.load_suppliers()


    def open_add_storage_location_dialog(self):
        add_storage_location_dialog = AddStorageLocationsDialog()
        add_storage_location_dialog.exec()
        self.load_storage_locations()


# READ ONLY Panel widget for the items based database information
class ReadOnlyItemsPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QGridLayout()

        # Add a form label/line edit widget for the new item name
        self.item_name = FormLabelTextWidgetWide("Name:", read_only=True)
        form_panel_layout.addLayout(self.item_name, 0, 0)

        # Add a form label/line edit widget for the new item supplier
        self.item_supplier = FormLabelTextWidgetWide("Supplier:", read_only=True)
        form_panel_layout.addLayout(self.item_supplier, 1, 0)

        # Add a form label/line edit widget for the new item product number
        self.item_product_number = FormLabelTextWidgetWide("Product Number:", read_only=True)
        form_panel_layout.addLayout(self.item_product_number, 2, 0)

        # Add a form label/line edit widget for the new item description
        self.item_description = FormLabelTextWidgetWide("Description:", read_only=True)
        form_panel_layout.addLayout(self.item_description, 3, 0)

        # Add a form label/line edit widget for the new item size
        self.item_size = FormLabelTextWidgetWide("Size/Volume:", read_only=True)
        form_panel_layout.addLayout(self.item_size, 4, 0)

        # Add a form label/line edit widget for the new item quantity
        self.item_quantity = FormLabelTextWidgetWide("Quantity:", read_only=True)
        form_panel_layout.addLayout(self.item_quantity, 5, 0)

        # Add a form label/line edit widget for the new item unit cost
        self.item_unit_cost = FormLabelTextWidgetWide("Unit Cost:", read_only=True)
        form_panel_layout.addLayout(self.item_unit_cost, 0, 1)

        # Add a form label/line edit widget for the new item storage location
        self.item_storage_location = FormLabelTextWidgetWide("Storage Location:", read_only=True)
        form_panel_layout.addLayout(self.item_storage_location, 1, 1)

        # Add a form label/line edit widget for the new item website
        self.item_website = FormLabelHyperlinkButton("hyperlink", "Website:")
        form_panel_layout.addLayout(self.item_website, 2, 1)

        # Add a checkbox widget for the new item reorder flag
        self.item_reorder_flag = FormLabelCheckBox("Reorder Flag:")
        form_panel_layout.addLayout(self.item_reorder_flag, 3, 1, alignment=Qt.AlignLeft)

        # Add item category 
        self.item_category = FormLabelTextWidgetWide("Category:", read_only=True)
        form_panel_layout.addLayout(self.item_category, 4, 1)

        # Add item notes
        self.item_notes = FormLabelTextWidgetWide("Notes:", read_only=True)
        form_panel_layout.addLayout(self.item_notes, 5, 1)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)


# Pictogram widget
class PictogramWidget(QWidget):
    def __init__(self, pictogram_path:str):
        super().__init__()
        # Set the layout for the widget
        pictogram_layout = QVBoxLayout()

        # Add the pictogram image to the widget
        pixmap = QPixmap(pictogram_path)
        transform = QTransform().rotate(315)
        scaled_pixmap = pixmap.scaledToWidth(65, Qt.SmoothTransformation)
        rotated_pixmap = scaled_pixmap.transformed(transform, Qt.SmoothTransformation)
        lbl = QLabel()
        lbl.setPixmap(rotated_pixmap)
        lbl.setAlignment(Qt.AlignCenter)

        # Add the label to the layout
        pictogram_layout.addWidget(lbl)

        # Add a checkbox for the pictogram
        self.chb = QCheckBox()

        # Add the checkbox to the layout
        pictogram_layout.addWidget(self.chb, alignment=Qt.AlignCenter)

        # Set the main layout for the widget
        self.setLayout(pictogram_layout)


# Editable panel widget for the chemical aspect of items based database information
class ItemsChemicalPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a form label/line edit widget for the new item quartzy reference
        central_layout = QHBoxLayout()
        central_layout.addStretch()
        self.item_quartzy_ref = FormLabelTextWidgetExtraWide("Quartzy Reference:")
        central_layout.addLayout(self.item_quartzy_ref)
        central_layout.addStretch()
        form_panel_layout.addLayout(central_layout)

        # Add spacing
        form_panel_layout.addSpacing(10)

        # Add a form label/line edit widget for the new item file names
        central_layout = QHBoxLayout()
        central_layout.addStretch()
        self.item_prepurchase = FormLabelTextWidget("Pre-purchase Filename:")
        central_layout.addLayout(self.item_prepurchase)
        central_layout.addSpacing(20)
        self.item_msds = FormLabelTextWidget("MSDS Filename:")
        central_layout.addLayout(self.item_msds)
        central_layout.addStretch()
        form_panel_layout.addLayout(central_layout)

        # Add spacing
        form_panel_layout.addSpacing(10)

        # Add a label for the pictogram section
        lbl_pictogram_section = QLabel("Select the appropriate GHS pictograms for the item:")
        lbl_pictogram_section.setProperty("role", "std_form_lbl")
        form_panel_layout.addWidget(lbl_pictogram_section, alignment=Qt.AlignCenter)

        # Add pictograms 
        pictograms_layout = QHBoxLayout()
        self.GHS01_pictogram = PictogramWidget(resource_path("assets/ghs_01_explosive.tif"))
        self.GHS02_pictogram = PictogramWidget(resource_path("assets/ghs_02_flammable.tif"))
        self.GHS03_pictogram = PictogramWidget(resource_path("assets/ghs_03_oxidiser.tif"))
        self.GHS04_pictogram = PictogramWidget(resource_path("assets/ghs_04_compressed.tif"))
        self.GHS05_pictogram = PictogramWidget(resource_path("assets/ghs_05_corrosion.tif"))
        self.GHS06_pictogram = PictogramWidget(resource_path("assets/ghs_06_toxic.tif"))
        self.GHS07_pictogram = PictogramWidget(resource_path("assets/ghs_07_irritant.tif"))
        self.GHS08_pictogram = PictogramWidget(resource_path("assets/ghs_08_health.tif"))
        self.GHS09_pictogram = PictogramWidget(resource_path("assets/ghs_09_environment.tif"))
        pictograms_layout.addWidget(self.GHS01_pictogram)
        pictograms_layout.addWidget(self.GHS02_pictogram)
        pictograms_layout.addWidget(self.GHS03_pictogram)
        pictograms_layout.addWidget(self.GHS04_pictogram)
        pictograms_layout.addWidget(self.GHS05_pictogram)
        pictograms_layout.addWidget(self.GHS06_pictogram)
        pictograms_layout.addWidget(self.GHS07_pictogram)
        pictograms_layout.addWidget(self.GHS08_pictogram)
        pictograms_layout.addWidget(self.GHS09_pictogram)

        form_panel_layout.addLayout(pictograms_layout)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)


# Show panel widget for the chemical aspect of items based database information
class ItemsChemicalDisplayPanelWidget(QWidget):
    def __init__(self, prepurchase_filename:str, msds_filename:str):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a form label/line edit widget for the new item quartzy reference
        central_layout = QHBoxLayout()
        central_layout.addStretch()
        self.item_quartzy_ref = FormLabelTextWidgetExtraWide("Quartzy Reference:")
        central_layout.addLayout(self.item_quartzy_ref)
        central_layout.addStretch()
        form_panel_layout.addLayout(central_layout)

        # Add spacing
        form_panel_layout.addSpacing(10)

        # Add a form label/line edit widget for the new item file names
        central_layout = QHBoxLayout()
        central_layout.addStretch()
        self.item_prepurchase = FormLabelLinkButton(prepurchase_filename, self.open_prepurchase_file)
        central_layout.addLayout(self.item_prepurchase)
        central_layout.addSpacing(20)
        self.item_msds = FormLabelLinkButton(msds_filename, self.open_msds_file)
        central_layout.addLayout(self.item_msds)
        central_layout.addStretch()
        form_panel_layout.addLayout(central_layout)

        # Add spacing
        form_panel_layout.addSpacing(10)

        # Add a label for the pictogram section
        lbl_pictogram_section = QLabel("Select the appropriate GHS pictograms for the item:")
        lbl_pictogram_section.setProperty("role", "std_form_lbl")
        form_panel_layout.addWidget(lbl_pictogram_section, alignment=Qt.AlignCenter)

        # Add pictograms 
        pictograms_layout = QHBoxLayout()
        self.GHS01_pictogram = PictogramWidget(resource_path("assets/ghs_01_explosive.tif"))
        self.GHS02_pictogram = PictogramWidget(resource_path("assets/ghs_02_flammable.tif"))
        self.GHS03_pictogram = PictogramWidget(resource_path("assets/ghs_03_oxidiser.tif"))
        self.GHS04_pictogram = PictogramWidget(resource_path("assets/ghs_04_compressed.tif"))
        self.GHS05_pictogram = PictogramWidget(resource_path("assets/ghs_05_corrosion.tif"))
        self.GHS06_pictogram = PictogramWidget(resource_path("assets/ghs_06_toxic.tif"))
        self.GHS07_pictogram = PictogramWidget(resource_path("assets/ghs_07_irritant.tif"))
        self.GHS08_pictogram = PictogramWidget(resource_path("assets/ghs_08_health.tif"))
        self.GHS09_pictogram = PictogramWidget(resource_path("assets/ghs_09_environment.tif"))
        pictograms_layout.addWidget(self.GHS01_pictogram)
        pictograms_layout.addWidget(self.GHS02_pictogram)
        pictograms_layout.addWidget(self.GHS03_pictogram)
        pictograms_layout.addWidget(self.GHS04_pictogram)
        pictograms_layout.addWidget(self.GHS05_pictogram)
        pictograms_layout.addWidget(self.GHS06_pictogram)
        pictograms_layout.addWidget(self.GHS07_pictogram)
        pictograms_layout.addWidget(self.GHS08_pictogram)
        pictograms_layout.addWidget(self.GHS09_pictogram)

        form_panel_layout.addLayout(pictograms_layout)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)

    
    def open_prepurchase_file(self):
        filename = self.item_prepurchase.btn.text()
        filepath = db_info.PREPURCHASE_PATH + filename
        os.startfile(filepath)


    def open_msds_file(self):
        filename = self.item_msds.btn.text()
        filepath = db_info.MSDS_PATH + filename
        os.startfile(filepath)