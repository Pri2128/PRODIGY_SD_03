import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    def edit_contact(self, index, name=None, phone=None, email=None):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            print("Contact edited successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)
        print("Contacts saved to file successfully!")

    def load_contacts_from_file(self, filename):
        with open(filename, 'r') as file:
            self.contacts = json.load(file)
        print("Contacts loaded from file successfully!")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            index = int(input("Enter index of contact to edit: "))
            name = input("Enter new name (leave blank to keep existing): ")
            phone = input("Enter new phone number (leave blank to keep existing): ")
            email = input("Enter new email address (leave blank to keep existing): ")
            contact_manager.edit_contact(index, name, phone, email)
        elif choice == '4':
            index = int(input("Enter index of contact to delete: "))
            contact_manager.delete_contact(index)
        elif choice == '5':
            filename = input("Enter filename to save contacts to: ")
            contact_manager.save_contacts_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load contacts from: ")
            contact_manager.load_contacts_from_file(filename)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
