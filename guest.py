import pickle
import tkinter as tk

class Guest:
    def __init__(self, guest_id, name, address, contact):
        # Initialize guest attributes
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact = contact

    # Static method to save guest data to a pickle file
    @staticmethod
    def save_guest(entries):
        # Create a Guest object using the data from entries
        guest = Guest(
            entries['Guest ID'].get(),
            entries['Name'].get(),
            entries['Address'].get(),
            entries['Contact'].get()
        )
        try:
            # Open the pickle file in append binary mode and dump the guest object
            with open("guest_file.pkl", "ab") as file:
                pickle.dump(guest.__dict__, file)
                return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to read guest data from the pickle file
    @staticmethod
    def read_guests():
        guests = []  # Initialize an empty list to store guest data
        try:
            # Open the pickle file in read binary mode
            with open("guest_file.pkl", "rb") as file:
                while True:
                    try:
                        guest_data = pickle.load(file)  # Load guest data from the file
                        guests.append(guest_data)  # Append guest data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
        return guests  # Return the list of guest data

    # Static method to delete a guest from the pickle file based on guest ID
    @staticmethod
    def delete_guest(guest_id):
        try:
            guests = []  # Initialize an empty list to store updated guest data
            # Read existing guests from file
            with open("guest_file.pkl", "rb") as file:
                while True:
                    try:
                        guest = pickle.load(file)  # Load guest data from the file
                        if guest['guest_id'] != guest_id:
                            guests.append(guest)  # Append guest data to the list if ID doesn't match
                    except EOFError:
                        break  # Exit loop when end of file is reached

            # Write back the guests excluding the one to be deleted
            with open("guest_file.pkl", "wb") as file:
                for guest in guests:
                    pickle.dump(guest, file)  # Write updated guest data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to check if a guest with the given ID exists
    @staticmethod
    def guest_exists(guest_id):
        guests = Guest.read_guests()  # Read guest data from the pickle file
        for guest in guests:
            if guest.get('guest_id') == guest_id:
                return True  # Return True if guest with given ID exists
        return False  # Return False if guest with given ID doesn't exist

    # Static method to get guest data based on guest ID
    @staticmethod
    def get_guest(guest_id):
        guests = Guest.read_guests()  # Read guest data from the pickle file
        for guest in guests:
            if guest['guest_id'] == guest_id:
                return guest  # Return guest data if found
        return None  # Return None if guest with given ID doesn't exist

    # Static method to modify guest data based on guest ID and new data
    @staticmethod
    def modify_guest(guest_id, new_data):
        try:
            guests = []  # Initialize an empty list to store updated guest data
            with open("guest_file.pkl", "rb") as file:
                while True:
                    try:
                        guest = pickle.load(file)  # Load guest data from the file
                        if guest['guest_id'] == guest_id:
                            guest.update(new_data)  # Update guest data with new data
                        guests.append(guest)  # Append guest data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("guest_file.pkl", "wb") as file:
                for guest in guests:
                    pickle.dump(guest, file)  # Write updated guest data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure
