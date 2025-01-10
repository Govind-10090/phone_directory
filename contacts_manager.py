import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class ContactsManager:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def add_contact(self, name, details):
        """Add a new contact."""
        self.contacts[name] = details
        self.save_contacts()
        return f"Contact '{name}' added."

    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return f"Contact '{name}' deleted."
        else:
            return f"Contact '{name}' not found."

    def update_contact(self, name, new_details):
        """Update contact information."""
        if name in self.contacts:
            self.contacts[name] = new_details
            self.save_contacts()
            return f"Contact '{name}' updated."
        else:
            return f"Contact '{name}' not found."

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            return {name: self.contacts[name]}
        else:
            return f"Contact '{name}' not found."

    def display_contacts(self):
        """Display all contacts."""
        return [{"name": name, "details": details} for name, details in self.contacts.items()]

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file)

    def load_contacts(self):
        """Load contacts from a JSON file."""
        try:
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}
        except json.JSONDecodeError:
            self.contacts = {}

manager = ContactsManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data['name']
    phone_number = data['phone_number']
    address = data['address']
    message = manager.add_contact(name, {'phone_number': phone_number, 'address': address})
    return jsonify({'message': message})

@app.route('/search_contact/<name>', methods=['GET'])
def search_contact(name):
    result = manager.search_contact(name)
    return jsonify({'message': result})

@app.route('/display_contacts', methods=['GET'])
def display_contacts():
    contacts = manager.display_contacts()
    return jsonify(contacts)

if __name__ == "__main__":
    app.run(debug=True)
