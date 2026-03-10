from PySide6.QtWidgets import QApplication
from core.setup_functions import load_all_stylesheets
from ui.windows.welcome_window import WelcomeWindow

app = QApplication([])

load_all_stylesheets(app)

window = WelcomeWindow()
window.show()

app.exec()