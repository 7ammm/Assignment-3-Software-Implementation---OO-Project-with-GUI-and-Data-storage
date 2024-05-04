import pickle

class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers_company, invoice):
        # Initialize event attributes
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers_company = suppliers_company
        self.invoice = invoice

    # Static method to save event data to a pickle file
    @staticmethod
    def save_event(entries):
        # Create an Event object using the data from entries
        event = Event(
            entries['Event ID'].get(),
            entries['Event Type'].get(),
            entries['Theme'].get(),
            entries['Date'].get(),
            entries['Time'].get(),
            entries['Duration'].get(),
            entries['Venue Address'].get(),
            entries['Client ID'].get(),
            entries['Guest List'].get(),
            entries['Suppliers Company'].get(),
            entries['Invoice'].get()
        )
        try:
            # Open the pickle file in append binary mode and dump the event object
            with open("event_file.pkl", "ab") as file:
                pickle.dump(event.__dict__, file)
                return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to read event data from the pickle file
    @staticmethod
    def read_events():
        events = []  # Initialize an empty list to store event data
        try:
            # Open the pickle file in read binary mode
            with open("event_file.pkl", "rb") as file:
                while True:
                    try:
                        event_data = pickle.load(file)  # Load event data from the file
                        events.append(event_data)  # Append event data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
        return events  # Return the list of event data

    # Static method to delete an event from the pickle file based on event ID
    @staticmethod
    def delete_event(event_id):
        try:
            events = []  # Initialize an empty list to store updated event data
            # Read existing events from file
            with open("event_file.pkl", "rb") as file:
                while True:
                    try:
                        event = pickle.load(file)  # Load event data from the file
                        if event['event_id'] != event_id:
                            events.append(event)  # Append event data to the list if ID doesn't match
                    except EOFError:
                        break  # Exit loop when end of file is reached

            # Write back the events excluding the one to be deleted
            with open("event_file.pkl", "wb") as file:
                for event in events:
                    pickle.dump(event, file)  # Write updated event data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to check if an event with the given ID exists
    @staticmethod
    def event_exists(event_id):
        events = Event.read_events()  # Read event data from the pickle file
        for event in events:
            if event.get('event_id') == event_id:
                return True  # Return True if event with given ID exists
        return False  # Return False if event with given ID doesn't exist

    # Static method to get event data based on event ID
    @staticmethod
    def get_event(event_id):
        events = Event.read_events()  # Read event data from the pickle file
        for event in events:
            if event['event_id'] == event_id:
                return event  # Return event data if found
        return None  # Return None if event with given ID doesn't exist

    # Static method to modify event data based on event ID and new data
    @staticmethod
    def modify_event(event_id, new_data):
        try:
            events = []  # Initialize an empty list to store updated event data
            with open("event_file.pkl", "rb") as file:
                while True:
                    try:
                        event = pickle.load(file)  # Load event data from the file
                        if event['event_id'] == event_id:
                            event.update(new_data)  # Update event data with new data
                        events.append(event)  # Append event data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("event_file.pkl", "wb") as file:
                for event in events:
                    pickle.dump(event, file)  # Write updated event data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure
