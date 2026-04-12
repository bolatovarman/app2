from db_manager import *

def main():
    import_csv('contacts.csv')
    add_contact('Aman', 'Berikov', '87071112233')
    update_contact('', '')
    get_contacts('')
    delete_contact('')

if __name__ == "__main__":
    main()