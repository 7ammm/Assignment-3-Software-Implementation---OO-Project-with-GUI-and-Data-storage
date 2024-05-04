import pickle
import tkinter as tk

class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # Initialize venue attributes
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Static method to save venue data to a pickle file
    @staticmethod
    def save_venue(entries):
        # Create a Venue object using the data from entries
        venue = Venue(
            entries['Venue ID'].get(),
            entries['Name'].get(),
            entries['Address'].get(),
            entries['Contact'].get(),
            entries['Min Guests'].get(),
            entries['Max Guests'].get()
        )

        try:
            # Open the pickle file in append binary mode and dump the venue object
            with open("venue_file.pkl", "ab") as file:
                pickle.dump(venue.__dict__, file)
                return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to read venue data from the pickle file
    @staticmethod
    def read_venues():
        venues = []  # Initialize an empty list to store venue data
        try:
            # Open the pickle file in read binary mode
            with open("venue_file.pkl", "rb") as file:
                while True:
                    try:
                        venue_data = pickle.load(file)  # Load venue data from the file
                        venues.append(venue_data)  # Append venue data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
        return venues  # Return the list of venue data

    # Static method to delete a venue from the pickle file based on venue ID
    @staticmethod
    def delete_venue(venue_id):
        try:
            venues = []  # Initialize an empty list to store updated venue data
            # Read existing venues from file
            with open("venue_file.pkl", "rb") as file:
                while True:
                    try:
                        venue = pickle.load(file)  # Load venue data from the file
                        if venue['venue_id'] != venue_id:
                            venues.append(venue)  # Append venue data to the list if ID doesn't match
                    except EOFError:
                        break  # Exit loop when end of file is reached

            # Write back the venues excluding the one to be deleted
            with open("venue_file.pkl", "wb") as file:
                for venue in venues:
                    pickle.dump(venue, file)  # Write updated venue data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to check if a venue with the given ID exists
    @staticmethod
    def venue_exists(venue_id):
        venues = Venue.read_venues()  # Read venue data from the pickle file
        for venue in venues:
            if venue.get('venue_id') == venue_id:
                return True  # Return True if venue with given ID exists
        return False  # Return False if venue with given ID doesn't exist

    # Static method to get venue data based on venue ID
    @staticmethod
    def get_venue(venue_id):
        venues = Venue.read_venues()  # Read venue data from the pickle file
        for venue in venues:
            if venue['venue_id'] == venue_id:
                return venue  # Return venue data if found
        return None  # Return None if venue with given ID doesn't exist

    # Static method to modify venue data based on venue ID and new data
    @staticmethod
    def modify_venue(venue_id, new_data):
        try:
            venues = []  # Initialize an empty list to store updated venue data
            with open("venue_file.pkl", "rb") as file:
                while True:
                    try:
                        venue = pickle.load(file)  # Load venue data from the file
                        if venue['venue_id'] == venue_id:
                            venue.update(new_data)  # Update venue data with new data
                        venues.append(venue)  # Append venue data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("venue_file.pkl", "wb") as file:
                for venue in venues:
                    pickle.dump(venue, file)  # Write updated venue data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure
