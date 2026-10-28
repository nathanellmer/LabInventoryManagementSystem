from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QSizePolicy, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from core.utility_functions import resource_path
from core.control_functions import controller
from ui.custom_widgets.general.button_widgets import NavbarMenuButton
from ui.custom_widgets.general.footer_widgets import SULogoLabel
from ui.custom_widgets.general.header_widgets import LabLogoLabel, TitleLabel
from ui.custom_widgets.general.label_widgets import InfoLabel
from datetime import datetime

# Panel widget for the use database menu
class Navbar(QWidget):
    # Setup signal for menu selection
    page_selection = Signal()
    
    def __init__(self):
        super().__init__()

        # Set the layout for the panel
        navbar_layout = QVBoxLayout()
        navbar_layout.setContentsMargins(0, 25, 0, 0)

        # Connect button clicks to the signal
        def select_search_page():
            controller.active_page = 1
            self.page_selection.emit()
            
        def select_database_page():
            controller.active_page = 2
            self.page_selection.emit()

        def select_shopping_page():
            controller.active_page = 3
            self.page_selection.emit()

        def select_forms_page():
            controller.active_page = 4
            self.page_selection.emit()

        # Create buttons
        navbar_btns = [
            NavbarMenuButton("Search", select_search_page),
            NavbarMenuButton("Database", select_database_page),
            NavbarMenuButton("Shopping", select_shopping_page),
            NavbarMenuButton("Forms", select_forms_page)
        ]

        # Add buttons to the layout
        for btn in navbar_btns:
            # btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            navbar_layout.addWidget(btn)
            navbar_layout.addSpacing(20)

        # Set the layout for the panel
        self.setLayout(navbar_layout)

        # Add stretch
        navbar_layout.addStretch()

        # Setup a layout for the logos
        logo_layout = QVBoxLayout()

        # Add the lab logo
        logo_layout.addWidget(LabLogoLabel(), alignment=Qt.AlignmentFlag.AlignHCenter)

        # Add spacing
        logo_layout.addSpacing(10)

        # Add the university logo
        logo_layout.addWidget(SULogoLabel(), alignment=Qt.AlignmentFlag.AlignHCenter)

        # Add the logo layout to the main layout
        navbar_layout.addLayout(logo_layout)

        
        

        


# Logo label widget for the application
class LIMSLogoLabel(QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QPixmap(resource_path("assets/lims_icon_new.png"))
        self.setPixmap(pixmap.scaledToWidth(50, Qt.SmoothTransformation))
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(50)


class StatusBar(QWidget):
    def __init__(self):
        super().__init__()

        # Set the layout for the status bar
        status_bar_layout = QGridLayout()
        status_bar_layout.setContentsMargins(0, 0, 0, 0)
        status_bar_layout.setSpacing(0)

        # Add the logo to the status bar
        status_bar_layout.addWidget(LIMSLogoLabel(), 0, 0, alignment=Qt.AlignLeft)

        # Add a date
        self.lbl_date = InfoLabel(datetime.now().strftime("%A, %d %B %Y"))
        status_bar_layout.addWidget(self.lbl_date, 0, 1, alignment=Qt.AlignLeft)

        # Create a label to display the page title
        self.lbl_page_title = TitleLabel("Page Title")
        status_bar_layout.addWidget(self.lbl_page_title, 0, 2, alignment=Qt.AlignCenter)

        # Create a label to display the status message
        self.lbl_username = InfoLabel("Username")
        status_bar_layout.addWidget(self.lbl_username, 0, 3, alignment=Qt.AlignRight)

        # Set the column widths for the status bar layout
        status_bar_layout.setColumnStretch(0, 1) 
        status_bar_layout.setColumnStretch(1, 3)  
        status_bar_layout.setColumnStretch(2, 3) 
        status_bar_layout.setColumnStretch(3, 3)
        # Set the layout for the status bar
        self.setLayout(status_bar_layout)
        