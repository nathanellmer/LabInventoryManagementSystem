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


# Get all supplier information from the database using supplier id
def get_supplier_info_by_id(supplier_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    supplier_info = cursor.execute("SELECT * FROM Suppliers WHERE SupplierID = ?", (supplier_id,)).fetchone()

    # Close the connection
    conn.close()

    # Check if empty result
    if supplier_info is None:
        msg_dialog = MsgDialog("Supplier Not Found", f"Supplier '{supplier_id}' not found in the database.", "OK")
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


# Get all grant code information from the database using grant code id
def get_grant_code_info_by_id(grant_code_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    grant_code_info = cursor.execute("SELECT * FROM GrantCodes WHERE GrantCodeID = ?", (grant_code_id,)).fetchone()

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


# Get all storage location information from the database using location id
def get_storage_location_info_by_id(location_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    storage_location_info = cursor.execute("SELECT * FROM StorageLocations WHERE LocationID = ?", (location_id,)).fetchone()

    # Close the connection
    conn.close()

    return storage_location_info


# Get all item information from the database using item name
def get_item_info_by_name(item_name):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    item_info = cursor.execute("SELECT * FROM Items WHERE ItemName = ?", (item_name,)).fetchall()

    # If empty result, check a partial match
    if len(item_info) == 0:
        item_info = cursor.execute("SELECT * FROM Items WHERE ItemName LIKE ?", (f"%{item_name}%",)).fetchall()

    # Close the connection
    conn.close()

    return item_info


# Get all item information from the database using item product code
def get_item_info_by_product_code(item_product_code):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    item_info = cursor.execute("SELECT * FROM Items WHERE ItemRef = ?", (item_product_code,)).fetchall()

    # If empty result, check a partial match
    if len(item_info) == 0:
        item_info = cursor.execute("SELECT * FROM Items WHERE ItemRef LIKE ?", (f"%{item_product_code}%",)).fetchall()

    # Close the connection
    conn.close()

    return item_info


# Get all item information from the database using item description
def get_item_info_by_description(item_description):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    item_info = cursor.execute("SELECT * FROM Items WHERE ItemDescription = ?", (item_description,)).fetchall()

    # If empty result, check a partial match
    if len(item_info) == 0:
        item_info = cursor.execute("SELECT * FROM Items WHERE ItemDescription LIKE ?", (f"%{item_description}%",)).fetchall()

    # Close the connection
    conn.close()

    return item_info


# Get all item information from the database using item supplier
def get_item_info_by_supplier(item_supplier):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    supplier_info = cursor.execute("SELECT * FROM Suppliers WHERE SupplierName = ?", (item_supplier,)).fetchall()

    # If empty result, check a partial match
    if len(supplier_info) == 0:
        supplier_info = cursor.execute("SELECT * FROM Suppliers WHERE SupplierName LIKE ?", (f"%{item_supplier}%",)).fetchall()

    # If there is supplier info then identify matching items
    item_info = []
    if len(supplier_info) > 0:
        for supplier in supplier_info:
            items = cursor.execute("SELECT * FROM Items WHERE ItemSupplier = ?", (supplier[0],)).fetchall()
            item_info.extend(items)

    # Close the connection
    conn.close()

    return item_info


# Get all item information from the database using the reorder flag
def get_items_info_by_reorder_flag():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    reorder_items = cursor.execute("SELECT * FROM Items WHERE ItemReorderFlag = 1").fetchall()

    # Close the connection
    conn.close()

    return reorder_items


# Get all item information from the database using item id
def get_item_info_by_id(item_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command
    item_info = cursor.execute("SELECT * FROM Items WHERE ItemID = ?", (item_id,)).fetchone()

    # Close the connection
    conn.close()

    return item_info


# Get all the field names for the items table in the database and return them as a list
def get_items_db_fieldnames():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get the field names for the items table
    cursor.execute("PRAGMA table_info(Items)")
    fieldnames = [field[1] for field in cursor.fetchall()]

    # Close the connection
    conn.close()

    return fieldnames[1:len(fieldnames)+1]


# Get all items information from the database
def get_all_items_info():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get all items information
    items_info = cursor.execute("SELECT * FROM Items").fetchall()

    # Close the connection
    conn.close()

    return items_info


# Get all the field names for the suppliers table in the database and return them as a list
def get_suppliers_db_fieldnames():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get the field names for the suppliers table
    cursor.execute("PRAGMA table_info(Suppliers)")
    fieldnames = [field[1] for field in cursor.fetchall()]

    # Close the connection
    conn.close()

    return fieldnames[1:len(fieldnames)+1]


# Get all suppliers information from the database
def get_all_suppliers_info():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get all suppliers information
    suppliers_info = cursor.execute("SELECT * FROM Suppliers").fetchall()

    # Close the connection
    conn.close()

    return suppliers_info


# Get all the field names for the users table in the database and return them as a list
def get_users_db_fieldnames():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get the field names for the users table
    cursor.execute("PRAGMA table_info(Users)")
    fieldnames = [field[1] for field in cursor.fetchall()]

    # Close the connection
    conn.close()

    return fieldnames[1:len(fieldnames)+1]


# Get all users information from the database
def get_all_users_info():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get all users information
    users_info = cursor.execute("SELECT * FROM Users").fetchall()

    # Close the connection
    conn.close()

    return users_info


# Get all the field names for the grant codes table in the database and return them as a list
def get_grant_codes_db_fieldnames():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get the field names for the grant codes table
    cursor.execute("PRAGMA table_info(GrantCodes)")
    fieldnames = [field[1] for field in cursor.fetchall()]

    # Close the connection
    conn.close()

    return fieldnames[1:len(fieldnames)+1]


# Get all grant_codes information from the database
def get_all_grant_codes_info():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get all grant codes information
    grant_codes_info = cursor.execute("SELECT * FROM GrantCodes").fetchall()

    # Close the connection
    conn.close()

    return grant_codes_info


# Get all the field names for the locations table in the database and return them as a list
def get_locations_db_fieldnames():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get the field names for the locations table
    cursor.execute("PRAGMA table_info(StorageLocations)")
    fieldnames = [field[1] for field in cursor.fetchall()]

    # Close the connection
    conn.close()

    return fieldnames[1:len(fieldnames)+1]


# Get all locations information from the database
def get_all_locations_info():
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command to get all locations information
    locations_info = cursor.execute("SELECT * FROM StorageLocations").fetchall()

    # Close the connection
    conn.close()

    return locations_info
