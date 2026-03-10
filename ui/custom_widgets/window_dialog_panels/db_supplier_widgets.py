from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.form_widgets import FormLabelTextWidgetWide

# Panel widget for the supplier based database information
class SupplierPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a form label/line edit widget for the new supplier name
        self.name = FormLabelTextWidgetWide("Name:")
        form_panel_layout.addLayout(self.name)

        # Add a form label/line edit widget for the website
        self.website = FormLabelTextWidgetWide("Website:")
        form_panel_layout.addLayout(self.website)

        # Add a form label/line edit widget for the address
        self.address_L1 = FormLabelTextWidgetWide("Address:")
        form_panel_layout.addLayout(self.address_L1)
        self.address_L2 = FormLabelTextWidgetWide("")
        form_panel_layout.addLayout(self.address_L2)

        # Add a form label/line edit widget for the postcode
        self.postcode = FormLabelTextWidgetWide("Postcode:")
        form_panel_layout.addLayout(self.postcode)

        # Add a form label/line edit widget for the Phone number
        self.phone = FormLabelTextWidgetWide("Phone:")
        form_panel_layout.addLayout(self.phone)

        # Add a form label/line edit widget for the email
        self.email = FormLabelTextWidgetWide("Email:")
        form_panel_layout.addLayout(self.email)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)