# This file contains functions for validating and converting data from CSV files when adding items to the database.

# Take a dictionary and convert the values
def validate_csv_data_item(old_item):
    new_item = {}
    for key, value in old_item.items():
        new_item[key] = convert_value_item(value, key)

    return new_item

# Convert an item dictionary
def convert_value_item(value, key):
        # Create a schema dictionary
        schema = {
            "ItemName": str,
            "ItemSupplier": str,
            "ItemRef": str,
            "ItemDescription": str,
            "ItemSize": str,
            "ItemQuantity": int,
            "ItemStorageLocation": str,
            "ItemUnitCost": float,
            "ItemWebsite": str,
            "ItemReorderFlag": bool,
            "ItemOriginator": str,
            "ItemCategory": str,
            "ItemNotes": str,
            "ItemQuartzyRef": str,
            "ItemPrepurchase": str,
            "ItemMSDS": str,
            "ItemGHS1": bool,
            "ItemGHS2": bool,
            "ItemGHS3": bool,
            "ItemGHS4": bool,
            "ItemGHS5": bool,
            "ItemGHS6": bool,
            "ItemGHS7": bool,
            "ItemGHS8": bool,
            "ItemGHS9": bool,
        }

        # Convert the value to the appropriate data type based on the schema
        if schema[key] == int:
            return int(value)
        elif schema[key] == float:
            return float(value)
        elif schema[key] == bool:
            if value.lower() in ["true", "1", "yes"]:
                return True
            elif value.lower() in ["false", "0", "no"]:
                return False
        else:
            return value
    