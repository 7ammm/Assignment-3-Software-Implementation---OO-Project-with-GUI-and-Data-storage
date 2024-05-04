import pickle
import tkinter as tk

class Supplier:
    def __init__(self, supplier_id, name, address, contact, service_provided, min_guests, max_guests):
        # Initialize supplier attributes
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact = contact
        self.service_provided = service_provided
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Static method to save supplier data to a pickle file
    @staticmethod
    def save_supplier(entries):
        # Create a Supplier object using the data from entries
        supplier = Supplier(
            entries['Supplier ID'].get(),
            entries['Name'].get(),
            entries['Address'].get(),
            entries['Contact'].get(),
            entries['Service Provided'].get(),
            entries['Min Guests'].get(),
            entries['Max Guests'].get()
        )
        try:
            # Open the pickle file in append binary mode and dump the supplier object
            with open("supplier_file.pkl", "ab") as file:
                pickle.dump(supplier.__dict__, file)
                return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to read supplier data from the pickle file
    @staticmethod
    def read_suppliers():
        suppliers = []  # Initialize an empty list to store supplier data
        try:
            # Open the pickle file in read binary mode
            with open("supplier_file.pkl", "rb") as file:
                while True:
                    try:
                        supplier_data = pickle.load(file)  # Load supplier data from the file
                        suppliers.append(supplier_data)  # Append supplier data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
        return suppliers  # Return the list of supplier data

    # Static method to delete a supplier from the pickle file based on supplier ID
    @staticmethod
    def delete_supplier(supplier_id):
        try:
            suppliers = []  # Initialize an empty list to store updated supplier data
            # Read existing suppliers from file
            with open("supplier_file.pkl", "rb") as file:
                while True:
                    try:
                        supplier = pickle.load(file)  # Load supplier data from the file
                        if supplier['supplier_id'] != supplier_id:
                            suppliers.append(supplier)  # Append supplier data to the list if ID doesn't match
                    except EOFError:
                        break  # Exit loop when end of file is reached

            # Write back the suppliers excluding the one to be deleted
            with open("supplier_file.pkl", "wb") as file:
                for supplier in suppliers:
                    pickle.dump(supplier, file)  # Write updated supplier data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to check if a supplier with the given ID exists
    @staticmethod
    def supplier_exists(supplier_id):
        suppliers = Supplier.read_suppliers()  # Read supplier data from the pickle file
        for supplier in suppliers:
            if supplier.get('supplier_id') == supplier_id:
                return True  # Return True if supplier with given ID exists
        return False  # Return False if supplier with given ID doesn't exist

    # Static method to get supplier data based on supplier ID
    @staticmethod
    def get_supplier(supplier_id):
        suppliers = Supplier.read_suppliers()  # Read supplier data from the pickle file
        for supplier in suppliers:
            if supplier['supplier_id'] == supplier_id:
                return supplier  # Return supplier data if found
        return None  # Return None if supplier with given ID doesn't exist

    # Static method to modify supplier data based on supplier ID and new data
    @staticmethod
    def modify_supplier(supplier_id, new_data):
        try:
            suppliers = []  # Initialize an empty list to store updated supplier data
            with open("supplier_file.pkl", "rb") as file:
                while True:
                    try:
                        supplier = pickle.load(file)  # Load supplier data from the file
                        if supplier['supplier_id'] == supplier_id:
                            supplier.update(new_data)  # Update supplier data with new data
                        suppliers.append(supplier)  # Append supplier data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("supplier_file.pkl", "wb") as file:
                for supplier in suppliers:
                    pickle.dump(supplier, file)  # Write updated supplier data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure
