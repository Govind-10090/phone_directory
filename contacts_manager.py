# contacts_manager.py

class ContactsManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, details):
        """Add a new contact."""
        self.contacts[name] = details
        print(f"Contact '{name}' added.")

    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, new_details):
        """Update contact information."""
        if name in self.contacts:
            self.contacts[name] = new_details
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            return f"{name}: {self.contacts[name]}"
        else:
            return f"Contact '{name}' not found."

    def display_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"{name}: {details}")

# Example usage
if __name__ == "__main__":
    manager = ContactsManager()
    
    while True:
        print("\nOptions: add, delete, update, search, display, exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            name = input("Enter contact name: ")
            details = input("Enter contact details (e.g., phone number): ")
            manager.add_contact(name, details)

        elif command == "delete":
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)

        elif command == "update":
            name = input("Enter contact name to update: ")
            new_details = input("Enter new details: ")
            manager.update_contact(name, new_details)

        elif command == "search":
            name = input("Enter contact name to search: ")
            print(manager.search_contact(name))

        elif command == "display":
            manager.display_contacts()

        elif command == "exit":
            print("Exiting the contact manager.")
            break

        else:
            print("Invalid command. Please try again.")

# contacts_manager.py