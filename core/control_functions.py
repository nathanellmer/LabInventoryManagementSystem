import os
import sys

from PySide6.QtCore import QObject, Signal
from core.utility_functions import resource_path

class AppController(QObject):
    close_all_windows = Signal()
    logged_in_user = None
    item_id = None

controller = AppController()


class DBInfo():
    # Database information and paths
    SCHEMA_PATH = resource_path("database/schema.sql")
    CONFIG_PATH = resource_path("config.txt")

    if getattr(sys, 'frozen', False):
        # Running as compiled exe
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        base_dir = os.path.abspath(".")

    config_path = os.path.join(base_dir, "config.txt")

    with open(config_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    DB_PATH = lines[0].split('"')[1]
    PREPURCHASE_PATH = lines[1].split('"')[1]
    MSDS_PATH = lines[2].split('"')[1]
    SAVE_PATH = lines[3].split('"')[1]
    COLOUR_SCHEME = lines[4].split('"')[1]

db_info = DBInfo()