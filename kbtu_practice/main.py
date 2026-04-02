import phonebook

def main():
    phonebook.create_table()
    
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Import from CSV")
        print("2. Add new contact")
        print("3. Update contact phone")
        print("4. Search contact")
        print("5. Delete contact")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            phonebook.import_from_csv('contacts.csv')
        elif choice == '2':
            n = input("Enter name: ")
            p = input("Enter phone: ")
            phonebook.add_contact(n, p)
            print("Added!")
        elif choice == '3':
            n = input("Enter name to update: ")
            p = input("Enter new phone: ")
            phonebook.update_contact(n, p)
        elif choice == '4':
            s = input("Enter name or phone prefix to search: ")
            phonebook.search_contacts(s)
        elif choice == '5':
            d = input("Enter name or phone to delete: ")
            phonebook.delete_contact(d)
        elif choice == '0':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()