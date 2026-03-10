from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

# Info label widget
class InfoLabel(QLabel):
    def __init__(self, lbl_text: str):
        super().__init__()
        self.setText(lbl_text)
        self.setProperty("role", "universal_info_line_lbl")
        self.setAlignment(Qt.AlignCenter)
