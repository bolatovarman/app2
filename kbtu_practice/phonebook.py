import psycopg2
import csv
from config import db_params

def get_connection():
    return psycopg2.connect(**db_params)

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id SERIAL PRIMARY KEY, 
                    name TEXT, 
                    phone TEXT UNIQUE
                );
            """)
            conn.commit()

def import_from_csv(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            with get_connection() as conn:
                with conn.cursor() as cur:
                    for row in reader:
                        cur.execute(
                            "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                            (row['name'], row['phone'])
                        )
                    conn.commit()
        print("CSV data imported successfully.")
    except Exception as e:
        print(f"CSV Error: {e}")

def add_contact(name, phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING", (name, phone))
            conn.commit()

def update_contact(old_name, new_phone):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE contacts SET phone = %s WHERE name = %s", (new_phone, old_name))
            conn.commit()
            print(f"Contact {old_name} updated.")

def delete_contact(identifier):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM contacts WHERE name = %s OR phone = %s", (identifier, identifier))
            conn.commit()
            print(f"Contact {identifier} deleted.")

def search_contacts(pattern):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s", ('%' + pattern + '%', pattern + '%'))
            rows = cur.fetchall()
            for row in rows:
                print(row)