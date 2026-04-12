import psycopg2
import csv
from config import params

def execute_query(query, vals=None, fetch=False):
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(query, vals)
            if fetch: return cur.fetchall()
            conn.commit()

def import_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            execute_query("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", row)
    print("CSV imported.")

def add_contact(fname, lname, phone):
    execute_query("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (fname, lname, phone))
    print("Contact added.")

def update_contact(name, new_phone):
    execute_query("UPDATE phonebook SET phone_number = %s WHERE first_name = %s", (new_phone, name))
    print("Contact updated.")

def get_contacts(filter_val):
    results = execute_query("SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone_number LIKE %s", (f'%{filter_val}%', f'%{filter_val}%'), True)
    for r in results: print(r)

def delete_contact(name):
    execute_query("DELETE FROM phonebook WHERE first_name = %s", (name,))
    print("Contact deleted.")