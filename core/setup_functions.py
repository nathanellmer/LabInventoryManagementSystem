import sqlite3
import os

from core.control_functions import db_info

# Setup of stylesheets
def load_stylesheets(files):
    styles = []

    for file in files:
        with open(file) as f:
            styles.append(f.read())

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