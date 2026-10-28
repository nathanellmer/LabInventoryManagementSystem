from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.form_widgets import FormLabelTextWidget

# Panel widget for the grant codes based database information
class GrantCodesPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Set a mandatory field indicator
        mandatory_field_indicator = '<span style="color: red;">*</span>'

        # Add a form label/line edit widget for the new grant code
        self.grant_code = FormLabelTextWidget("Grant Code" + mandatory_field_indicator + ":")
        form_panel_layout.addLayout(self.grant_code)

        # Add a form label/line edit widget for the owner
        self.owner = FormLabelTextWidget("Owner" + mandatory_field_indicator + ":")
        form_panel_layout.addLayout(self.owner)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)