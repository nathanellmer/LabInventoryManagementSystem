import sqlite3
import os
import re

from core.control_functions import db_info
from core.utility_functions import resource_path
from ui.styles.load_themes import THEMES

# Setup of stylesheets
def replace_url(match):
    relative_img_path = match.group(1).strip('"\'')

    # Convert to absolute path
    abs_img_path = resource_path(relative_img_path)
    # Use forward slashes for QSS (Qt requires /)
    return f'url("{abs_img_path.replace(os.sep, "/")}")'


def load_stylesheets(files):
    theme = THEMES.get(db_info.COLOUR_SCHEME)

    styles = []

    for file in files:
        with open(resource_path(file)) as f:
            qss = f.read() % theme
            qss = re.sub(r'url\((.*?)\)', replace_url, qss)
            styles.append(qss)

    return "\n".join(styles)


def load_all_stylesheets(app):
    app.setStyleSheet(load_stylesheets(["ui/styles/main_component_styles.qss", 
                                        "ui/styles/form_component_styles.qss", 
                                        "ui/styles/msg_component_styles.qss"]))


# Database setup functions
def init_database(db_path=db_info.DB_PATH, schema_path=db_info.SCHEMA_PATH):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read the SQL schema from the file
    with open(schema_path, 'r') as f:
        schema_sql = f.read()

    # Execute the SQL schema to create tables
    cursor.executescript(schema_sql)

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def get_db_connection(db_path):
    if not os.path.exists(db_path):
        init_database()

    conn = sqlite3.connect(db_path)
    conn.execute('PRAGMA foreign_keys = ON;')

    return conn