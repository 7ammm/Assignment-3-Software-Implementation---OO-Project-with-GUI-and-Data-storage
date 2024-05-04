import pickle
import tkinter as tk

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    # Method to save client data to a pickle file
    def save_client(entries):
        # Create a Client object using the data from entries
        client = Client(
            entries['Client ID'].get(),
            entries['Name'].get(),
            entries['Address'].get(),
            entries['Contact Details'].get(),
            entries['Budget'].get()
        )

        try:
            # Open the pickle file in append binary mode and dump the client object
            with open("client_file.pkl", "ab") as file:
                pickle.dump(client.__dict__, file)  # Save the client object's dictionary representation
                return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to read client data from the pickle file
    @staticmethod
    def read_clients():
        clients = []  # Initialize an empty list to store client data
        try:
            # Open the pickle file in read binary mode
            with open("client_file.pkl", "rb") as file:
                while True:
                    try:
                        client_data = pickle.load(file)  # Load client data from the file
                        clients.append(client_data)  # Append client data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
        return clients  # Return the list of client data

    # Static method to delete a client from the pickle file based on client ID
    @staticmethod
    def delete_client(client_id):
        try:
            clients = []  # Initialize an empty list to store updated client data
            with open("client_file.pkl", "rb") as file:
                while True:
                    try:
                        client = pickle.load(file)  # Load client data from the file
                        if client['client_id'] != client_id:
                            clients.append(client)  # Append client data to the list if ID doesn't match
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("client_file.pkl", "wb") as file:
                for client in clients:
                    pickle.dump(client, file)  # Write updated client data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure

    # Static method to check if a client with the given ID exists
    @staticmethod
    def client_exists(client_id):
        clients = Client.read_clients()  # Read client data from the pickle file
        for client in clients:
            if client.get('client_id') == client_id:
                return True  # Return True if client with given ID exists
        return False  # Return False if client with given ID doesn't exist

    # Static method to get client data based on client ID
    @staticmethod
    def get_client(client_id):
        clients = Client.read_clients()  # Read client data from the pickle file
        for client in clients:
            if client['client_id'] == client_id:
                return client  # Return client data if found
        return None  # Return None if client with given ID doesn't exist

    # Static method to modify client data based on client ID and new data
    @staticmethod
    def modify_client(client_id, new_data):
        try:
            clients = []  # Initialize an empty list to store updated client data
            with open("client_file.pkl", "rb") as file:
                while True:
                    try:
                        client = pickle.load(file)  # Load client data from the file
                        if client['client_id'] == client_id:
                            client.update(new_data)  # Update client data with new data
                        clients.append(client)  # Append client data to the list
                    except EOFError:
                        break  # Exit loop when end of file is reached

            with open("client_file.pkl", "wb") as file:
                for client in clients:
                    pickle.dump(client, file)  # Write updated client data back to the file
            return True  # Return True if successful
        except Exception as e:
            print("Error:", str(e))  # Print error message if an exception occurs
            return False  # Return False indicating failure
