from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.custom_widgets.general.form_widgets import FormLabelTextWidgetWide

# Panel widget for the storage locations based database information
class StorageLocationsPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set form layout
        form_panel_layout = QVBoxLayout()

        # Add a form label/line edit widget for the new storage location
        self.storage_location = FormLabelTextWidgetWide("Storage Location:")
        form_panel_layout.addLayout(self.storage_location)

        # Set the main layout for the widget
        self.setLayout(form_panel_layout)