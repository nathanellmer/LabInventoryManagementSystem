from core.control_functions import db_info
from core.setup_functions import get_db_connection
from ui.dialogs.msg_dialog import MsgDialog

# Delete user information in the database using user_id
def delete_user_from_db(user_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command and catch any integrity errors (e.g. if the user already exists in the database)
    cursor.execute("DELETE FROM Users WHERE UserID = ?", (user_id,))
    conn.commit()

    # Show a message dialog to confirm the user has been deleted
    msg_dialog = MsgDialog("User Deleted", "User has been deleted from the database.", "OK")
    msg_dialog.exec()
    
    conn.commit()

    # Close the connection
    conn.close()


# Delete supplier information in the database using supplier_id
def delete_supplier_from_db(supplier_id):
    # Setup connection
    conn = get_db_connection(db_info.DB_PATH)
    cursor = conn.cursor()

    # Execute sql command and catch any integrity errors (e.g. if the supplier already exists in the database)
    cursor.execute("DELETE FROM Suppliers WHERE SupplierID = ?", (supplier_id,))
    conn.commit()

    # Show a message dialog to confirm the supplier has been deleted
    msg_dialog = MsgDialog("Supplier Deleted", "Supplier has been deleted from the database.", "OK")
    msg_dialog.exec()
    
    conn.commit()

    # Close the connection
    conn.close()
