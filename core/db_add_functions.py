import sqlite3
from core.control_functions import db_info
from core.setup_functions import get_db_connection
from ui.dialogs.msg_dialog import MsgDialog

# Add a new user to the database
def add_user_to_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    user_name, user_email, user_office = field_values

    # Execute sql command and catch any integrity errors (e.g. if the user already exists in the database)
    try:
        cursor.execute("INSERT INTO Users (UserName, UserEmail, UserOffice) VALUES (?, ?, ?)", (user_name, user_email, user_office))
        conn.commit()

        # Show a message dialog to confirm the user has been added
        msg_dialog = MsgDialog("User Added", f"{user_name} has been added to the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error", f"Either {user_name} or {user_email} already exists.", "OK")
        msg_dialog.exec_()
        dialog_close = False

    # Close the connection
    conn.close()

    return dialog_close


# Add a new supplier to the database
def add_supplier_to_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    supplier_name, supplier_website, supplier_address_L1, supplier_address_L2, supplier_postcode, supplier_phone, supplier_email = field_values

    # Execute sql command and catch any integrity errors (e.g. if the supplier already exists in the database)
    try:
        cursor.execute("INSERT INTO Suppliers (SupplierName, SupplierWebsite, SupplierAddressL1, SupplierAddressL2, SupplierPostcode, SupplierPhone, SupplierEmail) VALUES (?, ?, ?, ?, ?, ?, ?)", (supplier_name, supplier_website, supplier_address_L1, supplier_address_L2, supplier_postcode, supplier_phone, supplier_email))
        conn.commit()

        # Show a message dialog to confirm the supplier has been added
        msg_dialog = MsgDialog("Supplier Added", f"{supplier_name} has been added to the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error", f"{supplier_name} already exists in the database.", "OK")
        msg_dialog.exec_()
        dialog_close = False

    # Close the connection
    conn.close()

    return dialog_close


# Add a new grant code to the database
def add_grant_code_to_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    grant_code_name, grant_code_owner = field_values

    # Execute sql command and catch any integrity errors (e.g. if the grant code already exists in the database)
    try:
        cursor.execute("INSERT INTO GrantCodes (GrantCodeName, GrantCodeOwner) VALUES (?, ?)", (grant_code_name, grant_code_owner))
        conn.commit()

        # Show a message dialog to confirm the grant code has been added
        msg_dialog = MsgDialog("Grant Code Added", f"{grant_code_owner}'s grant code has been added to the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error", f"The grant code '{grant_code_name}' already exists in the database.", "OK")
        msg_dialog.exec_()
        dialog_close = False

    # Close the connection
    conn.close()

    return dialog_close


# Add a new storage location to the database
def add_storage_location_to_db(field_values):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    storage_location_name = field_values[0]

    # Execute sql command and catch any integrity errors (e.g. if the storage location already exists in the database)
    try:
        cursor.execute("INSERT INTO StorageLocations (LocationName) VALUES (?)", (storage_location_name,))
        conn.commit()

        # Show a message dialog to confirm the storage location has been added
        msg_dialog = MsgDialog("Storage Location Added", f"{storage_location_name} has been added to the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error", f"The storage location '{storage_location_name}' already exists in the database.", "OK")
        msg_dialog.exec_()
        dialog_close = False

    # Close the connection
    conn.close()

    return dialog_close


# Add a new item to the database
def add_item_to_db(field_values_txt, field_values_cmb, field_values_chb, field_values_quartzy, field_values_hazards, user_id, supplier_id, storage_location_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Unpack the field values
    item_name, item_prod_no, item_description, item_size, item_quantity, item_cost, item_website, item_notes = field_values_txt
    item_supplier, item_location, item_category = field_values_cmb
    item_reorder = field_values_chb[0]
    item_quartzy = field_values_quartzy[0]
    ghs_01, ghs_02, ghs_03, ghs_04, ghs_05, ghs_06, ghs_07, ghs_08, ghs_09 = field_values_hazards

    # Execute sql command and catch any integrity errors (e.g. if the storage location already exists in the database)
    try:
        cursor.execute("INSERT INTO Items (ItemName, ItemSupplier, ItemRef, ItemDescription, ItemSize, ItemQuantity, ItemStorageLocation, ItemUnitCost, ItemWebsite, ItemReorderFlag, ItemOriginator, ItemCategory, ItemNotes, ItemQuartzyRef, ItemGHS1, ItemGHS2, ItemGHS3, ItemGHS4, ItemGHS5, ItemGHS6, ItemGHS7, ItemGHS8, ItemGHS9) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (item_name, supplier_id, item_prod_no, item_description, item_size, item_quantity, storage_location_id, item_cost, item_website, item_reorder, user_id, item_category, item_notes, item_quartzy, ghs_01, ghs_02, ghs_03, ghs_04, ghs_05, ghs_06, ghs_07, ghs_08, ghs_09))
        conn.commit()

        # Show a message dialog to confirm the item has been added
        msg_dialog = MsgDialog("Item Added", f"{item_name} has been added to the database.", "OK")
        msg_dialog.exec()
        dialog_close = True

    except sqlite3.IntegrityError as e:
        msg_dialog = MsgDialog("Error", f"The item '{item_name}' product number already exists in the database.", "OK")
        msg_dialog.exec_()
        dialog_close = False

    # Close the connection
    conn.close()

    return dialog_close
