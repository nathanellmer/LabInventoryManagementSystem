from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from core.setup_functions import load_all_stylesheets
from core.utility_functions import resource_path
from ui.windows.welcome_window import WelcomeWindow

app = QApplication([])
app.setWindowIcon(QIcon(resource_path("assets/lims_icon.ico")))

load_all_stylesheets(app)

window = WelcomeWindow()
window.show()

app.exec()