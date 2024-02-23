class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"{name}: {details['phone']}")

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details['phone']:
                results.append((name, details))
        return results

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

# Example usage
contact_manager = ContactManager()

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        contact_manager.add_contact(name, phone, email, address)

    elif choice == '2':
        contact_manager.view_contact_list()

    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        results = contact_manager.search_contact(query)
        if results:
            print("\nSearch Results:")
            for name, details in results:
                print(f"{name}: {details['phone']}")
        else:
            print("No matching contacts found.")

    elif choice == '4':
        name = input("Enter contact name to update: ")
        new_phone = input("Enter new phone number (press Enter to skip): ")
        new_email = input("Enter new email address (press Enter to skip): ")
        new_address = input("Enter new address (press Enter to skip): ")
        contact_manager.update_contact(name, new_phone, new_email, new_address)

    elif choice == '5':
        name = input("Enter contact name to delete: ")
        contact_manager.delete_contact(name)

    elif choice == '6':
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")