import json

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class ContactsManager:
    def __init__(self):
        self.contacts = {}
        self.contacts_file = 'contacts.json'
        self.load_contacts()


    def add_contact(self, name, details):
        """Add a new contact."""
        if not name or not isinstance(name, str):
            return "Error: Name must be a non-empty string"
        if not details or not isinstance(details, dict):
            return "Error: Details must contain phone_number and address"

        if name in self.contacts:
            return f"Error: Contact '{name}' already exists"
            
        self.contacts[name] = details
        self.save_contacts()
        return f"Contact '{name}' added successfully."


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
            with open(self.contacts_file, 'r') as file:
                data = file.read()
                if not data.strip():  # Check if file is empty
                    self.contacts = {}
                else:
                    self.contacts = json.loads(data)
                    if not isinstance(self.contacts, dict):
                        raise ValueError("Invalid contacts format")
        except FileNotFoundError:
            self.contacts = {}
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error loading contacts: {str(e)}")
            self.contacts = {}



manager = ContactsManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        name = data.get('name')
        phone_number = data.get('phone_number')
        address = data.get('address')
        
        if not all([name, phone_number, address]):
            return jsonify({'error': 'Missing required fields'}), 400
            
        message = manager.add_contact(name, {'phone_number': phone_number, 'address': address})
        if message.startswith('Error:'):
            return jsonify({'error': message}), 400
            
        return jsonify({'message': message}), 201
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/delete_contact/<name>', methods=['DELETE'])
def delete_contact(name):
    message = manager.delete_contact(name)
    return jsonify({'message': message})

@app.route('/update_contact/<name>', methods=['PUT'])
def update_contact(name):
    data = request.get_json()
    new_details = {'phone_number': data['phone_number'], 'address': data['address']}
    message = manager.update_contact(name, new_details)
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
