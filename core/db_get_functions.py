from core.control_functions import db_info
from core.setup_functions import get_db_connection
from ui.dialogs.msg_dialog import MsgDialog

# Get all the usernames from the database and return them as a list
def get_all_usernames():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    user_names = cursor.execute("SELECT UserName FROM Users").fetchall()

    # Close the connection
    conn.close()

    return [user[0] for user in user_names]


# Get all the supplier names from the database and return them as a list
def get_all_suppliers():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    supplier_names = cursor.execute("SELECT SupplierName FROM Suppliers").fetchall()

    # Close the connection
    conn.close()

    return [supplier[0] for supplier in supplier_names]


# Get all the storage location names from the database and return them as a list
def get_all_storage_locations():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    location_names = cursor.execute("SELECT LocationName FROM StorageLocations").fetchall()

    # Close the connection
    conn.close()

    return [location[0] for location in location_names]


# Get all user information from the database using username
def get_user_info_by_username(username):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    user_info = cursor.execute("SELECT * FROM Users WHERE UserName = ?", (username,)).fetchone()

    # If empty result, check a partial match
    if user_info is None:
        user_info = cursor.execute("SELECT * FROM Users WHERE UserName LIKE ?", (f"%{username}%",)).fetchone()

    # Close the connection
    conn.close()

    # Check if empty result
    if user_info is None:
        msg_dialog = MsgDialog("User Not Found", f"User '{username}' not found in the database.", "OK")
        msg_dialog.exec()

    return user_info


# Get all supplier information from the database using supplier name
def get_supplier_info_by_name(supplier_name):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    supplier_info = cursor.execute("SELECT * FROM Suppliers WHERE SupplierName = ?", (supplier_name,)).fetchone()

    # If empty result, check a partial match
    if supplier_info is None:
        supplier_info = cursor.execute("SELECT * FROM Suppliers WHERE SupplierName LIKE ?", (f"%{supplier_name}%",)).fetchone()

    # Close the connection
    conn.close()

    # Check if empty result
    if supplier_info is None:
        msg_dialog = MsgDialog("Supplier Not Found", f"Supplier '{supplier_name}' not found in the database.", "OK")
        msg_dialog.exec()

    return supplier_info


# Get all grant code information from the database using grant code name
def get_grant_code_info_by_grant_code_name(grant_code_name):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    grant_code_info = cursor.execute("SELECT * FROM GrantCodes WHERE GrantCodeName = ?", (grant_code_name,)).fetchall()

    # If empty result, check a partial match
    if len(grant_code_info) == 0:
        grant_code_info = cursor.execute("SELECT * FROM GrantCodes WHERE GrantCodeName LIKE ?", (f"%{grant_code_name}%",)).fetchall()

    # Close the connection
    conn.close()

    return grant_code_info


# Get all grant code information from the database using grant code owner
def get_grant_code_info_by_grant_code_owner(grant_code_owner):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    grant_code_info = cursor.execute("SELECT * FROM GrantCodes WHERE GrantCodeOwner = ?", (grant_code_owner,)).fetchall()

    # If empty result, check a partial match
    if len(grant_code_info) == 0:
        grant_code_info = cursor.execute("SELECT * FROM GrantCodes WHERE GrantCodeOwner LIKE ?", (f"%{grant_code_owner}%",)).fetchall()

    # Close the connection
    conn.close()

    return grant_code_info


# Get all storage location information from the database using location name
def get_storage_location_info_by_name(location_name):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    storage_location_info = cursor.execute("SELECT * FROM StorageLocations WHERE LocationName = ?", (location_name,)).fetchall()

    # If empty result, check a partial match
    if len(storage_location_info) == 0:
        storage_location_info = cursor.execute("SELECT * FROM StorageLocations WHERE LocationName LIKE ?", (f"%{location_name}%",)).fetchall()

    # Close the connection
    conn.close()

    return storage_location_info
