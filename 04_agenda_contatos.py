contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def view_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found.")

# Example usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
view_contacts()
delete_contact("Alice")
view_contacts()
