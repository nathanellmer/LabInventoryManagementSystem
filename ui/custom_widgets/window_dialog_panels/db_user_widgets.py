from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.form_widgets import FormLabelTextWidget

# Panel widget for the user based database information
class UserPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a form label/line edit widget for the new username
        self.username = FormLabelTextWidget("Username:")
        form_panel_layout.addLayout(self.username)

        # Add a form label/line edit widget for the email
        self.email = FormLabelTextWidget("Email:")
        form_panel_layout.addLayout(self.email)

        # Add a form label/line edit widget for the office location
        self.office_location = FormLabelTextWidget("Office Location:")
        form_panel_layout.addLayout(self.office_location)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)