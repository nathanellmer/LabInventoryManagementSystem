from PySide6.QtCore import QObject, Signal

class AppController(QObject):
    close_all_windows = Signal()
    logged_in_user = None
    item_id = None

controller = AppController()


class DBInfo():
    # Database information and paths
    SCHEMA_PATH = "database/schema.sql"
    CONFIG_PATH = "config.txt"

    with open(CONFIG_PATH, 'r') as f:
        db_path = f.read().strip()

    DB_PATH = db_path.split('"')[1]

db_info = DBInfo()