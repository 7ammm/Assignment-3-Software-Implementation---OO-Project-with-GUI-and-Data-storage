import tkinter as tk
from tkinter import messagebox
from employee import Employee
from client import Client
from guest import Guest
from supplier import Supplier
from venue import Venue
from event import Event
import tkinter.scrolledtext as scrolledtext

def login_screen(root):
    def login():
        password = entry_password.get()
        if password == company_password:
            root.destroy()  # Close login window
            # Call main application window
            main_application()
        else:
            messagebox.showerror("Error", "Incorrect password! Please try again.")

    root.title("Management System")
    root.geometry("520x300")
    root.configure(bg="#FFFDD0")  # Set background color

    # Set company password
    company_password = "event123"  # Set your desired password here

    # Create widgets
    label_heading = tk.Label(root, text="Your Event, Our Passion: Let's Make It Unforgettable!", font=("Helvetica", 16), bg="#FFFDD0", fg="black")
    label_heading.pack(pady=10)

    label_password = tk.Label(root, text="Enter Password:", font=("Helvetica", 12), bg="#FFFDD0", fg="black")
    label_password.pack()

    entry_password = tk.Entry(root, show="*", font=("Helvetica", 12))
    entry_password.pack(pady=5)

    btn_login = tk.Button(root, text="Login", command=login, font=("Helvetica", 12), bg="#DAA06D", fg="black")
    btn_login.pack(pady=10)

def main_application():

    def open_employee_menu():
        employee_menu = tk.Toplevel(root)
        employee_menu.title("Employee Menu")
        employee_menu.geometry("400x300")
        employee_menu.configure(bg="#FFFDD0")  # Set background color

        btn_add_employee = tk.Button(employee_menu, text="Add Employee", command=lambda: add_employee(root), font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_add_employee.pack(pady=10)

        btn_modify_employee = tk.Button(employee_menu, text="Modify Employee", command=modify_employee, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_modify_employee.pack(pady=10)

        btn_delete_employee = tk.Button(employee_menu, text="Delete Employee", command=delete_employee, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_delete_employee.pack(pady=10)

        btn_display_employee = tk.Button(employee_menu, text="Display Employee", command=display_employee, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_display_employee.pack(pady=10)

    def open_client_menu():
        client_menu = tk.Toplevel(root)
        client_menu.title("Client Menu")
        client_menu.geometry("400x300")
        client_menu.configure(bg="#FFFDD0")  # Set background color

        btn_add_client = tk.Button(client_menu, text="Add Client", command=lambda: add_client(root), font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_add_client.pack(pady=10)

        btn_modify_client = tk.Button(client_menu, text="Modify Client", command=modify_client, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_modify_client.pack(pady=10)

        btn_delete_client = tk.Button(client_menu, text="Delete Client", command=delete_client, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_delete_client.pack(pady=10)

        btn_display_client = tk.Button(client_menu, text="Display Client", command=display_client, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_display_client.pack(pady=10)

    def open_guest_menu():
        guest_menu = tk.Toplevel(root)
        guest_menu.title("Guest Menu")
        guest_menu.geometry("400x300")
        guest_menu.configure(bg="#FFFDD0")  # Set background color

        btn_add_guest = tk.Button(guest_menu, text="Add Guest", command=lambda: add_guest(root), font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_add_guest.pack(pady=10)

        btn_modify_guest = tk.Button(guest_menu, text="Modify Guest", command=modify_guest, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_modify_guest.pack(pady=10)

        btn_delete_guest = tk.Button(guest_menu, text="Delete Guest", command=delete_guest, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_delete_guest.pack(pady=10)

        btn_display_guest = tk.Button(guest_menu, text="Display Guest", command=display_guest, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_display_guest.pack(pady=10)

    def open_supplier_menu():
        supplier_menu = tk.Toplevel(root)
        supplier_menu.title("Supplier Menu")
        supplier_menu.geometry("400x300")
        supplier_menu.configure(bg="#FFFDD0")  # Set background color

        btn_add_supplier = tk.Button(supplier_menu, text="Add Supplier", command=lambda: add_supplier(root), font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_add_supplier.pack(pady=10)

        btn_modify_supplier = tk.Button(supplier_menu, text="Modify Supplier", command=modify_supplier, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_modify_supplier.pack(pady=10)

        btn_delete_supplier = tk.Button(supplier_menu, text="Delete Supplier", command=delete_supplier, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_delete_supplier.pack(pady=10)

        btn_display_supplier = tk.Button(supplier_menu, text="Display Supplier", command=display_supplier, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_display_supplier.pack(pady=10)

    def open_venue_menu():
        venue_menu = tk.Toplevel(root)
        venue_menu.title("Venue Menu")
        venue_menu.geometry("400x300")
        venue_menu.configure(bg="#FFFDD0")  # Set background color

        btn_add_venue = tk.Button(venue_menu, text="Add Venue", command=lambda: add_venue(root), font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_add_venue.pack(pady=10)

        btn_modify_venue = tk.Button(venue_menu, text="Modify Venue", command=modify_venue, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_modify_venue.pack(pady=10)

        btn_delete_venue = tk.Button(venue_menu, text="Delete Venue", command=delete_venue, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_delete_venue.pack(pady=10)

        btn_display_venue = tk.Button(venue_menu, text="Display Venue", command=display_venue, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_display_venue.pack(pady=10)

    def open_event_menu():
        event_menu = tk.Toplevel(root)
        event_menu.title("Event Menu")
        event_menu.geometry("400x300")
        event_menu.configure(bg="#FFFDD0")  # Set background color

        btn_add_event = tk.Button(event_menu, text="Add Event", command=lambda: add_event(root), font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_add_event.pack(pady=10)

        btn_modify_event = tk.Button(event_menu, text="Modify Event", command=modify_event, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_modify_event.pack(pady=10)

        btn_delete_event = tk.Button(event_menu, text="Delete Event", command=delete_event, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_delete_event.pack(pady=10)

        btn_display_event = tk.Button(event_menu, text="Display Event", command=display_event, font=("Helvetica", 12), bg="#DAA06D", fg="black", width=15)
        btn_display_event.pack(pady=10)

    def add_client(root):
        add_screen = tk.Toplevel(root)
        add_screen.title("Add Client")
        add_screen.geometry("400x400")
        add_screen.configure(bg="#FFFDD0")

        labels = ["Client ID", "Name", "Address", "Contact Details", "Budget"]
        entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(add_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(add_screen, font=("Helvetica", 12))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[label_text] = entry

        btn_save = tk.Button(add_screen, text="Save", command=lambda: save_client(entries), font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save.grid(row=i+1, columnspan=2, pady=10)

    def save_client(entries):
        client_id = entries['Client ID'].get()
        name = entries['Name'].get()

        # Validate Client ID (numeric) and Name (alphabetic)
        if not client_id.isdigit():
            messagebox.showerror("Error", "Client ID must be a number.")
            return False

        if not name.isalpha():
            messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return False

        # If validation passes, proceed to save the client
        if Client.save_client(entries):
            messagebox.showinfo("Success", "Client added successfully!")
            return True
        else:
            messagebox.showerror("Error", "Failed to add client.")
            return False

    def modify_client():
        def display_client_data():
            client_id = entry_client_id.get()
            client_data = Client.get_client(client_id)
            if client_data:
                for key, entry in entry_fields.items():
                    lowercase_key = key.lower().replace(" ", "_")
                    if lowercase_key in client_data:
                        entry.delete(0, tk.END)
                        entry.insert(0, client_data[lowercase_key])
                    else:
                        entry.delete(0, tk.END)
                        entry.insert(0, "")
            else:
                messagebox.showerror("Error", "Client data not found.")

        def save_changes():
            client_id = entry_client_id.get()
            client_data = Client.get_client(client_id)
            if client_data:
                new_data = {key.lower().replace(" ", "_"): entry.get() for key, entry in entry_fields.items()}
                if Client.modify_client(client_id, new_data):
                    messagebox.showinfo("Success", "Client information updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update client information.")
            else:
                messagebox.showerror("Error", "Client data not found.")

        modify_screen = tk.Toplevel()
        modify_screen.title("Modify Client")
        modify_screen.geometry("600x400")
        modify_screen.configure(bg="#FFFDD0")

        label_client_id = tk.Label(modify_screen, text="Enter Client ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_client_id.grid(row=0, column=0, padx=10, pady=5)

        entry_client_id = tk.Entry(modify_screen, font=("Helvetica", 12))
        entry_client_id.grid(row=0, column=1, padx=10, pady=5)

        btn_display_client = tk.Button(modify_screen, text="Display Client", command=display_client_data, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display_client.grid(row=0, column=2, padx=10, pady=5)

        entry_fields = {}
        labels = ["Client ID", "Name", "Address", "Contact Details", "Budget"]
        for i, label_text in enumerate(labels):
            label = tk.Label(modify_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i+1, column=0, padx=10, pady=5)

            entry = tk.Entry(modify_screen, font=("Helvetica", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entry_fields[label_text] = entry

        btn_save_changes = tk.Button(modify_screen, text="Save Changes", command=save_changes, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save_changes.grid(row=len(labels)+2, columnspan=2, pady=10)

    def delete_client():
        def confirm_delete():
            client_id = entry_client_id.get()
            if Client.client_exists(client_id):  # Check if client ID exists
                if Client.delete_client(client_id):
                    messagebox.showinfo("Success", "Client deleted successfully!")
                else:
                    messagebox.showerror("Error", "Failed to delete client.")
            else:
                messagebox.showerror("Error", f"Client with ID {client_id} not found.")
            delete_screen.destroy()

        delete_screen = tk.Toplevel()
        delete_screen.title("Delete Client")
        delete_screen.geometry("300x150")
        delete_screen.configure(bg="#FFFDD0")

        label_client_id = tk.Label(delete_screen, text="Enter Client ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_client_id.pack(pady=5)

        entry_client_id = tk.Entry(delete_screen, font=("Helvetica", 12))
        entry_client_id.pack(pady=5)

        btn_confirm_delete = tk.Button(delete_screen, text="Confirm Delete", command=confirm_delete, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_confirm_delete.pack(pady=5)

    def display_client():
        # Create a new window for entering client ID
        display_screen = tk.Toplevel()
        display_screen.title("Display Client")
        display_screen.geometry("350x300")
        display_screen.configure(bg="#FFFDD0")

        # Function to display client details
        def show_client_details():
            # Get the client ID from the entry widget
            client_id = entry_client_id.get()

            # Read client details
            clients = Client.read_clients()
            found = False
            for client in clients:
                if client['client_id'] == client_id:
                    found = True
                    break

            if found:
                # Clear previous display
                for widget in display_screen.winfo_children():
                    widget.destroy()

                # Display client details
                details = "\n".join([f"{key}: {value}" for key, value in client.items()])
                text_area = scrolledtext.ScrolledText(display_screen, wrap=tk.WORD, width=50, height=20)
                text_area.insert(tk.INSERT, details)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Client not found!")

        # Label and entry for client ID
        label_client_id = tk.Label(display_screen, text="Enter Client ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_client_id.pack(pady=5)

        entry_client_id = tk.Entry(display_screen, font=("Helvetica", 12))
        entry_client_id.pack(pady=5)

        # Button to display client details
        btn_display = tk.Button(display_screen, text="Display", command=show_client_details, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display.pack(pady=5)

    def add_employee(root):
        add_screen = tk.Toplevel(root)
        add_screen.title("Add Employee")
        add_screen.geometry("400x450")
        add_screen.configure(bg="#FFFDD0")

        labels = ["Name", "Employee ID", "Department", "Job Title", "Basic Salary", "Age", "Date of Birth", "Passport Details", "Manager ID"]
        entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(add_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(add_screen, font=("Helvetica", 12))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[label_text] = entry

        btn_save = tk.Button(add_screen, text="Save", command=lambda: save(entries), font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save.grid(row=i+1, columnspan=2, pady=10)

    def save(entries):
        employee_id = entries['Employee ID'].get()
        name = entries['Name'].get()

        # Validate Employee ID (numeric) and Name (alphabetic)
        if not employee_id.isdigit():
            messagebox.showerror("Error", "Employee ID must be a number.")
            return False

        if not name.isalpha():
            messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return False

        # If validation passes, proceed to save the employee
        if Employee.save_employee(entries):
            messagebox.showinfo("Success", "Employee added successfully!")
            return True
        else:
            messagebox.showerror("Error", "Failed to add employee.")
            return False

    def modify_employee():
        def display_employee_data():
            employee_id = entry_employee_id.get()
            employee_data = Employee.get_employee(employee_id)
            if employee_data:
                for key, entry in entry_fields.items():
                    lowercase_key = key.lower().replace(" ", "_")
                    if lowercase_key in employee_data:
                        entry.delete(0, tk.END)
                        entry.insert(0, employee_data[lowercase_key])
                    else:
                        entry.delete(0, tk.END)
                        entry.insert(0, "")
            else:
                messagebox.showerror("Error", "Employee data not found.")

        def save_changes():
            employee_id = entry_employee_id.get()
            employee_data = Employee.get_employee(employee_id)
            if employee_data:
                new_data = {key.lower().replace(" ", "_"): entry.get() for key, entry in entry_fields.items()}
                if Employee.modify_employee(employee_id, new_data):
                    messagebox.showinfo("Success", "Employee information updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update employee information.")
            else:
                messagebox.showerror("Error", "Employee data not found.")

        modify_screen = tk.Toplevel()
        modify_screen.title("Modify Employee")
        modify_screen.geometry("600x400")
        modify_screen.configure(bg="#FFFDD0")

        label_employee_id = tk.Label(modify_screen, text="Enter Employee ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_employee_id.grid(row=0, column=0, padx=10, pady=5)

        entry_employee_id = tk.Entry(modify_screen, font=("Helvetica", 12))
        entry_employee_id.grid(row=0, column=1, padx=10, pady=5)

        btn_display_employee = tk.Button(modify_screen, text="Display Employee", command=display_employee_data, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display_employee.grid(row=0, column=2, padx=10, pady=5)

        entry_fields = {}
        labels = ["Name", "Employee ID", "Department", "Job Title", "Basic Salary", "Age", "Date of Birth", "Passport Details", "Manager ID"]
        for i, label_text in enumerate(labels):
            label = tk.Label(modify_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i+1, column=0, padx=10, pady=5)

            entry = tk.Entry(modify_screen, font=("Helvetica", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entry_fields[label_text] = entry

        btn_save_changes = tk.Button(modify_screen, text="Save Changes", command=save_changes, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save_changes.grid(row=len(labels)+2, columnspan=2, pady=10)

    def delete_employee():
        def confirm_delete():
            employee_id = entry_employee_id.get()
            if Employee.employee_exists(employee_id):  # Check if employee ID exists
                if Employee.delete_employee(employee_id):
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                else:
                    messagebox.showerror("Error", "Failed to delete employee.")
            else:
                messagebox.showerror("Error", f"Employee with ID {employee_id} not found.")
            delete_screen.destroy()

        delete_screen = tk.Toplevel()
        delete_screen.title("Delete Employee")
        delete_screen.geometry("300x150")
        delete_screen.configure(bg="#FFFDD0")

        label_employee_id = tk.Label(delete_screen, text="Enter Employee ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_employee_id.pack(pady=5)

        entry_employee_id = tk.Entry(delete_screen, font=("Helvetica", 12))
        entry_employee_id.pack(pady=5)

        btn_confirm_delete = tk.Button(delete_screen, text="Confirm Delete", command=confirm_delete, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_confirm_delete.pack(pady=5)

    def display_employee():
        # Create a new window for entering employee ID
        display_screen = tk.Toplevel()
        display_screen.title("Display Employee")
        display_screen.geometry("350x300")
        display_screen.configure(bg="#FFFDD0")

        # Function to display employee details
        def show_employee_details():
            # Get the employee ID from the entry widget
            employee_id = entry_employee_id.get()

            # Read employee details
            employees = Employee.read_employees()
            found = False
            for employee in employees:
                if employee['employee_id'] == employee_id:
                    found = True
                    break

            if found:
                # Clear previous display
                for widget in display_screen.winfo_children():
                    widget.destroy()

                # Display employee details
                details = "\n".join([f"{key}: {value}" for key, value in employee.items()])
                text_area = scrolledtext.ScrolledText(display_screen, wrap=tk.WORD, width=50, height=20)
                text_area.insert(tk.INSERT, details)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Employee not found!")

        # Label and entry for employee ID
        label_employee_id = tk.Label(display_screen, text="Enter Employee ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_employee_id.pack(pady=5)

        entry_employee_id = tk.Entry(display_screen, font=("Helvetica", 12))
        entry_employee_id.pack(pady=5)

        # Button to display employee details
        btn_display = tk.Button(display_screen, text="Display", command=show_employee_details, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display.pack(pady=5)

    def add_guest(root):
        add_screen = tk.Toplevel(root)
        add_screen.title("Add Guest")
        add_screen.geometry("400x400")
        add_screen.configure(bg="#FFFDD0")

        labels = ["Guest ID", "Name", "Address", "Contact"]
        entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(add_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(add_screen, font=("Helvetica", 12))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[label_text] = entry

        btn_save = tk.Button(add_screen, text="Save", command=lambda: save_guest(entries), font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save.grid(row=i+1, columnspan=2, pady=10)

    def save_guest(entries):
        guest_id = entries['Guest ID'].get()
        name = entries['Name'].get()

        # Validate Guest ID (numeric) and Name (alphabetic)
        if not guest_id.isdigit():
            messagebox.showerror("Error", "Guest ID must be a number.")
            return False

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return False

        # If validation passes, proceed to save the guest
        if Guest.save_guest(entries):
            messagebox.showinfo("Success", "Guest added successfully!")
            return True
        else:
            messagebox.showerror("Error", "Failed to add guest.")
            return False

    def modify_guest():
        def display_guest_data():
            guest_id = entry_guest_id.get()
            guest_data = Guest.get_guest(guest_id)
            if guest_data:
                for key, entry in entry_fields.items():
                    lowercase_key = key.lower().replace(" ", "_")
                    if lowercase_key in guest_data:
                        entry.delete(0, tk.END)
                        entry.insert(0, guest_data[lowercase_key])
                    else:
                        entry.delete(0, tk.END)
                        entry.insert(0, "")
            else:
                messagebox.showerror("Error", "Guest data not found.")

        def save_changes():
            guest_id = entry_guest_id.get()
            guest_data = Guest.get_guest(guest_id)
            if guest_data:
                new_data = {key.lower().replace(" ", "_"): entry.get() for key, entry in entry_fields.items()}
                if Guest.modify_guest(guest_id, new_data):
                    messagebox.showinfo("Success", "Guest information updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update guest information.")
            else:
                messagebox.showerror("Error", "Guest data not found.")

        modify_screen = tk.Toplevel()
        modify_screen.title("Modify Guest")
        modify_screen.geometry("600x400")
        modify_screen.configure(bg="#FFFDD0")

        label_guest_id = tk.Label(modify_screen, text="Enter Guest ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_guest_id.grid(row=0, column=0, padx=10, pady=5)

        entry_guest_id = tk.Entry(modify_screen, font=("Helvetica", 12))
        entry_guest_id.grid(row=0, column=1, padx=10, pady=5)

        btn_display_guest = tk.Button(modify_screen, text="Display Guest", command=display_guest_data, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display_guest.grid(row=0, column=2, padx=10, pady=5)

        entry_fields = {}
        labels = ["Guest ID", "Name", "Address", "Contact"]
        for i, label_text in enumerate(labels):
            label = tk.Label(modify_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i+1, column=0, padx=10, pady=5)

            entry = tk.Entry(modify_screen, font=("Helvetica", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entry_fields[label_text] = entry

        btn_save_changes = tk.Button(modify_screen, text="Save Changes", command=save_changes, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save_changes.grid(row=len(labels)+2, columnspan=2, pady=10)

    def delete_guest():
        def confirm_delete():
            guest_id = entry_guest_id.get()
            if Guest.guest_exists(guest_id):  # Check if guest ID exists
                if Guest.delete_guest(guest_id):
                    messagebox.showinfo("Success", "Guest deleted successfully!")
                else:
                    messagebox.showerror("Error", "Failed to delete guest.")
            else:
                messagebox.showerror("Error", f"Guest with ID {guest_id} not found.")
            delete_screen.destroy()

        delete_screen = tk.Toplevel()
        delete_screen.title("Delete Guest")
        delete_screen.geometry("300x150")
        delete_screen.configure(bg="#FFFDD0")

        label_guest_id = tk.Label(delete_screen, text="Enter Guest ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_guest_id.pack(pady=5)

        entry_guest_id = tk.Entry(delete_screen, font=("Helvetica", 12))
        entry_guest_id.pack(pady=5)

        btn_confirm_delete = tk.Button(delete_screen, text="Confirm Delete", command=confirm_delete, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_confirm_delete.pack(pady=5)

    def display_guest():
        # Create a new window for entering guest ID
        display_screen = tk.Toplevel()
        display_screen.title("Display Guest")
        display_screen.geometry("350x300")
        display_screen.configure(bg="#FFFDD0")

        # Function to display guest details
        def show_guest_details():
            # Get the guest ID from the entry widget
            guest_id = entry_guest_id.get()

            # Read guest details
            guests = Guest.read_guests()
            found = False
            for guest in guests:
                if guest['guest_id'] == guest_id:
                    found = True
                    break

            if found:
                # Clear previous display
                for widget in display_screen.winfo_children():
                    widget.destroy()

                # Display guest details
                details = "\n".join([f"{key}: {value}" for key, value in guest.items()])
                text_area = scrolledtext.ScrolledText(display_screen, wrap=tk.WORD, width=50, height=20)
                text_area.insert(tk.INSERT, details)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Guest not found!")

        # Label and entry for guest ID
        label_guest_id = tk.Label(display_screen, text="Enter Guest ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_guest_id.pack(pady=5)

        entry_guest_id = tk.Entry(display_screen, font=("Helvetica", 12))
        entry_guest_id.pack(pady=5)

        # Button to display guest details
        btn_display = tk.Button(display_screen, text="Display", command=show_guest_details, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display.pack(pady=5)


    def add_supplier(root):
        add_screen = tk.Toplevel(root)
        add_screen.title("Add Supplier")
        add_screen.geometry("400x400")
        add_screen.configure(bg="#FFFDD0")

        labels = ["Supplier ID", "Name", "Address", "Contact", "Service Provided", "Min Guests", "Max Guests"]
        entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(add_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(add_screen, font=("Helvetica", 12))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[label_text] = entry

        btn_save = tk.Button(add_screen, text="Save", command=lambda: save_supplier(entries), font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save.grid(row=i+1, columnspan=2, pady=10)

    def save_supplier(entries):
        supplier_id = entries['Supplier ID'].get()
        name = entries['Name'].get()

        # Validate Supplier ID (numeric) and Name (alphabetic)
        if not supplier_id.isdigit():
            messagebox.showerror("Error", "Supplier ID must be a number.")
            return False

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return False

        # If validation passes, proceed to save the supplier
        if Supplier.save_supplier(entries):
            messagebox.showinfo("Success", "Supplier added successfully!")
            return True
        else:
            messagebox.showerror("Error", "Failed to add supplier.")
            return False

    def modify_supplier():
        def display_supplier_data():
            supplier_id = entry_supplier_id.get()
            supplier_data = Supplier.get_supplier(supplier_id)
            if supplier_data:
                for key, entry in entry_fields.items():
                    lowercase_key = key.lower().replace(" ", "_")
                    if lowercase_key in supplier_data:
                        entry.delete(0, tk.END)
                        entry.insert(0, supplier_data[lowercase_key])
                    else:
                        entry.delete(0, tk.END)
                        entry.insert(0, "")
            else:
                messagebox.showerror("Error", "Supplier data not found.")

        def save_changes():
            supplier_id = entry_supplier_id.get()
            supplier_data = Supplier.get_supplier(supplier_id)
            if supplier_data:
                new_data = {key.lower().replace(" ", "_"): entry.get() for key, entry in entry_fields.items()}
                if Supplier.modify_supplier(supplier_id, new_data):
                    messagebox.showinfo("Success", "Supplier information updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update supplier information.")
            else:
                messagebox.showerror("Error", "Supplier data not found.")

        modify_screen = tk.Toplevel()
        modify_screen.title("Modify Supplier")
        modify_screen.geometry("600x400")
        modify_screen.configure(bg="#FFFDD0")

        label_supplier_id = tk.Label(modify_screen, text="Enter Supplier ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_supplier_id.grid(row=0, column=0, padx=10, pady=5)

        entry_supplier_id = tk.Entry(modify_screen, font=("Helvetica", 12))
        entry_supplier_id.grid(row=0, column=1, padx=10, pady=5)

        btn_display_supplier = tk.Button(modify_screen, text="Display Supplier", command=display_supplier_data, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display_supplier.grid(row=0, column=2, padx=10, pady=5)

        entry_fields = {}
        labels = ["Supplier ID", "Name", "Address", "Contact", "Service Provided", "Min Guests", "Max Guests"]
        for i, label_text in enumerate(labels):
            label = tk.Label(modify_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i+1, column=0, padx=10, pady=5)

            entry = tk.Entry(modify_screen, font=("Helvetica", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entry_fields[label_text] = entry

        btn_save_changes = tk.Button(modify_screen, text="Save Changes", command=save_changes, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save_changes.grid(row=len(labels)+2, columnspan=2, pady=10)

    def delete_supplier():
        def confirm_delete():
            supplier_id = entry_supplier_id.get()
            if Supplier.supplier_exists(supplier_id):  # Check if supplier ID exists
                if Supplier.delete_supplier(supplier_id):
                    messagebox.showinfo("Success", "Supplier deleted successfully!")
                else:
                    messagebox.showerror("Error", "Failed to delete supplier.")
            else:
                messagebox.showerror("Error", f"Supplier with ID {supplier_id} not found.")
            delete_screen.destroy()

        delete_screen = tk.Toplevel()
        delete_screen.title("Delete Supplier")
        delete_screen.geometry("300x150")
        delete_screen.configure(bg="#FFFDD0")

        label_supplier_id = tk.Label(delete_screen, text="Enter Supplier ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_supplier_id.pack(pady=5)

        entry_supplier_id = tk.Entry(delete_screen, font=("Helvetica", 12))
        entry_supplier_id.pack(pady=5)

        btn_confirm_delete = tk.Button(delete_screen, text="Confirm Delete", command=confirm_delete, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_confirm_delete.pack(pady=5)

    def display_supplier():
        # Create a new window for entering supplier ID
        display_screen = tk.Toplevel()
        display_screen.title("Display Supplier")
        display_screen.geometry("350x300")
        display_screen.configure(bg="#FFFDD0")

        # Function to display supplier details
        def show_supplier_details():
            # Get the supplier ID from the entry widget
            supplier_id = entry_supplier_id.get()

            # Read supplier details
            suppliers = Supplier.read_suppliers()
            found = False
            for supplier in suppliers:
                if supplier['supplier_id'] == supplier_id:
                    found = True
                    break

            if found:
                # Clear previous display
                for widget in display_screen.winfo_children():
                    widget.destroy()

                # Display supplier details
                details = "\n".join([f"{key}: {value}" for key, value in supplier.items()])
                text_area = scrolledtext.ScrolledText(display_screen, wrap=tk.WORD, width=50, height=20)
                text_area.insert(tk.INSERT, details)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Supplier not found!")

        # Label and entry for supplier ID
        label_supplier_id = tk.Label(display_screen, text="Enter Supplier ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_supplier_id.pack(pady=5)

        entry_supplier_id = tk.Entry(display_screen, font=("Helvetica", 12))
        entry_supplier_id.pack(pady=5)

        # Button to display supplier details
        btn_display = tk.Button(display_screen, text="Display", command=show_supplier_details, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display.pack(pady=5)


    def add_venue(root):
        add_screen = tk.Toplevel(root)
        add_screen.title("Add Venue")
        add_screen.geometry("400x400")
        add_screen.configure(bg="#FFFDD0")

        labels = ["Venue ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"]
        entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(add_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(add_screen, font=("Helvetica", 12))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[label_text] = entry

        btn_save = tk.Button(add_screen, text="Save", command=lambda: save_venue(entries), font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save.grid(row=i+1, columnspan=2, pady=10)

    def save_venue(entries):
        venue_id = entries['Venue ID'].get()
        name = entries['Name'].get()

        # Validate Venue ID (numeric) and Name (alphabetic)
        if not venue_id.isdigit():
            messagebox.showerror("Error", "Venue ID must be a number.")
            return False

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return False

        # If validation passes, proceed to save the venue
        if Venue.save_venue(entries):
            messagebox.showinfo("Success", "Venue added successfully!")
            return True
        else:
            messagebox.showerror("Error", "Failed to add venue.")
            return False

    def modify_venue():
        def display_venue_data():
            venue_id = entry_venue_id.get()
            venue_data = Venue.get_venue(venue_id)
            if venue_data:
                for key, entry in entry_fields.items():
                    lowercase_key = key.lower().replace(" ", "_")
                    if lowercase_key in venue_data:
                        entry.delete(0, tk.END)
                        entry.insert(0, venue_data[lowercase_key])
                    else:
                        entry.delete(0, tk.END)
                        entry.insert(0, "")
            else:
                messagebox.showerror("Error", "Venue data not found.")

        def save_changes():
            venue_id = entry_venue_id.get()
            venue_data = Venue.get_venue(venue_id)
            if venue_data:
                new_data = {key.lower().replace(" ", "_"): entry.get() for key, entry in entry_fields.items()}
                if Venue.modify_venue(venue_id, new_data):
                    messagebox.showinfo("Success", "Venue information updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update venue information.")
            else:
                messagebox.showerror("Error", "Venue data not found.")

        modify_screen = tk.Toplevel()
        modify_screen.title("Modify Venue")
        modify_screen.geometry("600x400")
        modify_screen.configure(bg="#FFFDD0")

        label_venue_id = tk.Label(modify_screen, text="Enter Venue ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_venue_id.grid(row=0, column=0, padx=10, pady=5)

        entry_venue_id = tk.Entry(modify_screen, font=("Helvetica", 12))
        entry_venue_id.grid(row=0, column=1, padx=10, pady=5)

        btn_display_venue = tk.Button(modify_screen, text="Display Venue", command=display_venue_data, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display_venue.grid(row=0, column=2, padx=10, pady=5)

        entry_fields = {}
        labels = ["Venue ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"]
        for i, label_text in enumerate(labels):
            label = tk.Label(modify_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i+1, column=0, padx=10, pady=5)

            entry = tk.Entry(modify_screen, font=("Helvetica", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entry_fields[label_text] = entry

        btn_save_changes = tk.Button(modify_screen, text="Save Changes", command=save_changes, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save_changes.grid(row=len(labels)+2, columnspan=2, pady=10)

    def delete_venue():
        def confirm_delete():
            venue_id = entry_venue_id.get()
            if Venue.venue_exists(venue_id):  # Check if venue ID exists
                if Venue.delete_venue(venue_id):
                    messagebox.showinfo("Success", "Venue deleted successfully!")
                else:
                    messagebox.showerror("Error", "Failed to delete venue.")
            else:
                messagebox.showerror("Error", f"Venue with ID {venue_id} not found.")
            delete_screen.destroy()

        delete_screen = tk.Toplevel()
        delete_screen.title("Delete Venue")
        delete_screen.geometry("300x150")
        delete_screen.configure(bg="#FFFDD0")

        label_venue_id = tk.Label(delete_screen, text="Enter Venue ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_venue_id.pack(pady=5)

        entry_venue_id = tk.Entry(delete_screen, font=("Helvetica", 12))
        entry_venue_id.pack(pady=5)

        btn_confirm_delete = tk.Button(delete_screen, text="Confirm Delete", command=confirm_delete, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_confirm_delete.pack(pady=5)

    def display_venue():
        # Create a new window for entering venue ID
        display_screen = tk.Toplevel()
        display_screen.title("Display Venue")
        display_screen.geometry("350x300")
        display_screen.configure(bg="#FFFDD0")

        # Function to display venue details
        def show_venue_details():
            # Get the venue ID from the entry widget
            venue_id = entry_venue_id.get()

            # Read venue details
            venues = Venue.read_venues()
            found = False
            for venue in venues:
                if venue['venue_id'] == venue_id:
                    found = True
                    break

            if found:
                # Clear previous display
                for widget in display_screen.winfo_children():
                    widget.destroy()

                # Display venue details
                details = "\n".join([f"{key}: {value}" for key, value in venue.items()])
                text_area = scrolledtext.ScrolledText(display_screen, wrap=tk.WORD, width=50, height=20)
                text_area.insert(tk.INSERT, details)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Venue not found!")

        # Label and entry for venue ID
        label_venue_id = tk.Label(display_screen, text="Enter Venue ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_venue_id.pack(pady=5)

        entry_venue_id = tk.Entry(display_screen, font=("Helvetica", 12))
        entry_venue_id.pack(pady=5)

        # Button to display venue details
        btn_display = tk.Button(display_screen, text="Display", command=show_venue_details, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display.pack(pady=5)

    def add_event(root):
        add_screen = tk.Toplevel(root)
        add_screen.title("Add Event")
        add_screen.geometry("600x600")
        add_screen.configure(bg="#FFFDD0")

        labels = ["Event ID", "Event Type", "Theme", "Date", "Time", "Duration", "Venue Address", "Client ID", "Guest List", "Suppliers Company", "Invoice"]
        entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(add_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i, column=0, padx=10, pady=10, sticky="w")

            entry = tk.Entry(add_screen, font=("Helvetica", 12))
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries[label_text] = entry

        btn_save = tk.Button(add_screen, text="Save", command=lambda: save_event(entries), font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save.grid(row=i+1, columnspan=2, pady=10)

    def save_event(entries):
        event_id = entries['Event ID'].get()
        event_type = entries['Event Type'].get()

        # Validate Event ID (numeric) and Event Type (alphabetic)
        if not event_id.isdigit():
            messagebox.showerror("Error", "Event ID must be a number.")
            return False

        if not event_type.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Event Type must contain only alphabetic characters.")
            return False

        # If validation passes, proceed to save the event
        if Event.save_event(entries):
            messagebox.showinfo("Success", "Event added successfully!")
            return True
        else:
            messagebox.showerror("Error", "Failed to add event.")
            return False

    def modify_event():
        def display_event_data():
            event_id = entry_event_id.get()
            event_data = Event.get_event(event_id)
            if event_data:
                for key, entry in entry_fields.items():
                    lowercase_key = key.lower().replace(" ", "_")
                    if lowercase_key in event_data:
                        entry.delete(0, tk.END)
                        entry.insert(0, event_data[lowercase_key])
                    else:
                        entry.delete(0, tk.END)
                        entry.insert(0, "")
            else:
                messagebox.showerror("Error", "Event data not found.")

        def save_changes():
            event_id = entry_event_id.get()
            event_data = Event.get_event(event_id)
            if event_data:
                new_data = {key.lower().replace(" ", "_"): entry.get() for key, entry in entry_fields.items()}
                if Event.modify_event(event_id, new_data):
                    messagebox.showinfo("Success", "Event information updated successfully!")
                else:
                    messagebox.showerror("Error", "Failed to update event information.")
            else:
                messagebox.showerror("Error", "Event data not found.")

        modify_screen = tk.Toplevel()
        modify_screen.title("Modify Event")
        modify_screen.geometry("800x600")
        modify_screen.configure(bg="#FFFDD0")

        label_event_id = tk.Label(modify_screen, text="Enter Event ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_event_id.grid(row=0, column=0, padx=10, pady=5)

        entry_event_id = tk.Entry(modify_screen, font=("Helvetica", 12))
        entry_event_id.grid(row=0, column=1, padx=10, pady=5)

        btn_display_event = tk.Button(modify_screen, text="Display Event", command=display_event_data, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display_event.grid(row=0, column=2, padx=10, pady=5)

        entry_fields = {}
        labels = ["Event ID", "Event Type", "Theme", "Date", "Time", "Duration", "Venue Address", "Client ID", "Guest List", "Suppliers Company", "Invoice"]
        for i, label_text in enumerate(labels):
            label = tk.Label(modify_screen, text=label_text + ":", font=("Helvetica", 12), bg="#FFFDD0")
            label.grid(row=i+1, column=0, padx=10, pady=5)

            entry = tk.Entry(modify_screen, font=("Helvetica", 12))
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entry_fields[label_text] = entry

        btn_save_changes = tk.Button(modify_screen, text="Save Changes", command=save_changes, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_save_changes.grid(row=len(labels)+2, columnspan=2, pady=10)

    def delete_event():
        def confirm_delete():
            event_id = entry_event_id.get()
            if Event.event_exists(event_id):  # Check if event ID exists
                if Event.delete_event(event_id):
                    messagebox.showinfo("Success", "Event deleted successfully!")
                else:
                    messagebox.showerror("Error", "Failed to delete event.")
            else:
                messagebox.showerror("Error", f"Event with ID {event_id} not found.")
            delete_screen.destroy()

        delete_screen = tk.Toplevel()
        delete_screen.title("Delete Event")
        delete_screen.geometry("300x150")
        delete_screen.configure(bg="#FFFDD0")

        label_event_id = tk.Label(delete_screen, text="Enter Event ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_event_id.pack(pady=5)

        entry_event_id = tk.Entry(delete_screen, font=("Helvetica", 12))
        entry_event_id.pack(pady=5)

        btn_confirm_delete = tk.Button(delete_screen, text="Confirm Delete", command=confirm_delete, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_confirm_delete.pack(pady=5)

    def display_event():
        # Create a new window for entering event ID
        display_screen = tk.Toplevel()
        display_screen.title("Display Event")
        display_screen.geometry("350x300")
        display_screen.configure(bg="#FFFDD0")

        # Function to display event details
        def show_event_details():
            # Get the event ID from the entry widget
            event_id = entry_event_id.get()

            # Read event details
            events = Event.read_events()
            found = False
            for event in events:
                if event['event_id'] == event_id:
                    found = True
                    break

            if found:
                # Clear previous display
                for widget in display_screen.winfo_children():
                    widget.destroy()

                # Display event details
                details = "\n".join([f"{key}: {value}" for key, value in event.items()])
                text_area = scrolledtext.ScrolledText(display_screen, wrap=tk.WORD, width=50, height=20)
                text_area.insert(tk.INSERT, details)
                text_area.pack(expand=True, fill="both", padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Event not found!")

        # Label and entry for event ID
        label_event_id = tk.Label(display_screen, text="Enter Event ID:", font=("Helvetica", 12), bg="#FFFDD0")
        label_event_id.pack(pady=5)

        entry_event_id = tk.Entry(display_screen, font=("Helvetica", 12))
        entry_event_id.pack(pady=5)

        # Button to display event details
        btn_display = tk.Button(display_screen, text="Display", command=show_event_details, font=("Helvetica", 12), bg="#DAA06D", fg="black")
        btn_display.pack(pady=5)

    root = tk.Tk()
    root.title("Management System")
    root.geometry("800x600")
    root.configure(bg="#FFFDD0")  # Set background color

    # Create buttons for different options
    btn_employee = tk.Button(root, text="Employee", command=open_employee_menu, font=("Helvetica", 14), bg="#DAA06D", fg="black", width=15)
    btn_employee.pack(pady=20)

    btn_client = tk.Button(root, text="Client", command=open_client_menu, font=("Helvetica", 14), bg="#DAA06D", fg="black", width=15)
    btn_client.pack(pady=20)

    btn_guest = tk.Button(root, text="Guest", command=open_guest_menu, font=("Helvetica", 14), bg="#DAA06D", fg="black", width=15)
    btn_guest.pack(pady=20)

    btn_supplier = tk.Button(root, text="Supplier", command=open_supplier_menu, font=("Helvetica", 14), bg="#DAA06D", fg="black", width=15)
    btn_supplier.pack(pady=20)

    btn_venue = tk.Button(root, text="Venue", command=open_venue_menu, font=("Helvetica", 14), bg="#DAA06D", fg="black", width=15)
    btn_venue.pack(pady=20)

    btn_event = tk.Button(root, text="Event", command=open_event_menu, font=("Helvetica", 14), bg="#DAA06D", fg="black", width=15)
    btn_event.pack(pady=20)

    root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    login_screen(root)
    root.mainloop()
