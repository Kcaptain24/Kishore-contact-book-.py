class ContactBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contact details

    # Function to add a new contact
    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print(f"Contact with the name {name} already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact {name} added successfully!")

    # Function to view all contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

    # Function to search for a contact by name or phone number
    def search_contact(self, search_value):
        for name, info in self.contacts.items():
            if name == search_value or info['phone'] == search_value:
                print(f"Contact Found: Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
                return
        print("Contact not found.")

    # Function to update a contact
    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact {name} updated successfully!")
        else:
            print(f"No contact found with the name {name}.")

    # Function to delete a contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"No contact found with the name {name}.")


# User Interface Simulation
def user_interface():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_value = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_value)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            address = input("Enter new address (or press Enter to skip): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None, address if address else None)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the User Interface
if __name__ == "__main__":
    user_interface()