import sqlite3
from core.control_functions import db_info
from core.setup_functions import get_db_connection
from ui.dialogs.msg_dialog import MsgDialog

# Update user information in the database using user_id
def update_user_in_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    user_id, user_name, user_email, user_office = field_values

    # Execute sql command and catch any integrity errors (e.g. if the user already exists in the database)
    try:
        cursor.execute("UPDATE Users SET UserName = ?, UserEmail = ?, UserOffice = ? WHERE UserID = ?", (user_name, user_email, user_office, user_id))
        conn.commit()

        # Show a message dialog to confirm the user has been added
        msg_dialog = MsgDialog("User Updated", f"{user_name} has been updated in the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error Updating User", f"Either {user_name} or {user_email} already exists.", "OK")
        msg_dialog.exec_()
        dialog_close = False
    
    conn.commit()

    # Close the connection
    conn.close()

    return dialog_close


# Update supplier information in the database using supplier_id
def update_supplier_in_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    supplier_id, supplier_name, supplier_website, supplier_address_L1, supplier_address_L2, supplier_postcode, supplier_phone, supplier_email = field_values

    # Execute sql command and catch any integrity errors (e.g. if the supplier already exists in the database)
    try:
        cursor.execute("UPDATE Suppliers SET SupplierName = ?, SupplierWebsite = ?, SupplierAddressL1 = ?, SupplierAddressL2 = ?, SupplierPostcode = ?, SupplierPhone = ?, SupplierEmail = ? WHERE SupplierID = ?", (supplier_name, supplier_website, supplier_address_L1, supplier_address_L2, supplier_postcode, supplier_phone, supplier_email, supplier_id))
        conn.commit()

        # Show a message dialog to confirm the supplier has been added
        msg_dialog = MsgDialog("Supplier Updated", f"{supplier_name} has been updated in the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error Updating Supplier", f"The supplier '{supplier_name}' already exists.", "OK")
        msg_dialog.exec_()
        dialog_close = False
    
    conn.commit()

    # Close the connection
    conn.close()

    return dialog_close


# Update grant code information in the database using grant_code_id
def update_grant_code_in_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    grant_code_id, grant_code_name, grant_code_owner = field_values

    # Execute sql command and catch any integrity errors (e.g. if the grant code already exists in the database)
    try:
        cursor.execute("UPDATE GrantCodes SET GrantCodeName = ?, GrantCodeOwner = ? WHERE GrantCodeID = ?", (grant_code_name, grant_code_owner, grant_code_id))
        conn.commit()

        # Show a message dialog to confirm the grant code has been added
        msg_dialog = MsgDialog("Grant Code Updated", f"{grant_code_owner}'s grant code has been updated in the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error Updating Grant Code", f"The grant code '{grant_code_name}' already exists.", "OK")
        msg_dialog.exec_()
        dialog_close = False
    
    conn.commit()

    # Close the connection
    conn.close()

    return dialog_close


# Update storage location information in the database using location_id
def update_storage_location_in_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    location_id, location_name = field_values

    # Execute sql command and catch any integrity errors (e.g. if the storage location already exists in the database)
    try:
        cursor.execute("UPDATE StorageLocations SET LocationName = ? WHERE LocationID = ?", (location_name, location_id))
        conn.commit()

        # Show a message dialog to confirm the storage location has been updated
        msg_dialog = MsgDialog("Storage Location Updated", f"{location_name} has been updated in the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error Updating Storage Location", f"The storage location '{location_name}' already exists.", "OK")
        msg_dialog.exec_()
        dialog_close = False
    
    conn.commit()

    # Close the connection
    conn.close()

    return dialog_close
