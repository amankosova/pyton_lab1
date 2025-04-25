import psycopg2
import csv

def connect():
    return psycopg2.connect(
        database="lab10", user="postgres", password="270807", host="localhost", port="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            phone VARCHAR(25) NOT NULL UNIQUE

        )
    ''')
    conn.commit()
    conn.close()
def insert_or_update_user(name, age, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO phonebook (name, age, phone)
        VALUES (%s, %s, %s)
        ON CONFLICT(phone) DO UPDATE SET
            name = EXCLUDED.name,
            age = EXCLUDED.age
    ''', (name, age, phone))
    conn.commit()
    conn.close()

def insert_csv():
    conn=connect()
    cur=conn.cursor()
    path= r"C:\Users\zenbo\OneDrive\Рабочий стол\pp2\contacts.csv"

    with open(path,"r") as f:
        file=csv.reader(f)
        next(file)
        for i in file:
            # Егер телефон нөмірі дерекқорда болмаса, қосамыз
            cur.execute('''
                INSERT INTO phonebook (name, age, phone)
                VALUES (%s, %s, %s)
                ON CONFLICT(phone) DO NOTHING 
            ''', (i[0], i[1], i[2]))
    conn.commit()  
    cur.close()
    conn.close()
    print("CSV data inserted successfully.\n")

def search_users(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR phone ILIKE %s
    ''', ('%' + pattern + '%', '%' + pattern + '%'))
    rows = cur.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Phone: {row[3]}")
    else:
        print("No users found matching the pattern.")

def get_users_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM phonebook
        LIMIT %s OFFSET %s
    ''', (limit, offset))
    rows = cur.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Phone: {row[3]}")
    else:
        print("No more users to display.")
    
def insert_many_users(user_list):
    conn = connect()
    cur = conn.cursor()
    valid_users = []
    for i in user_list:
            valid_users.append(i)
    for username,age, phone in valid_users:
            cur.execute("CALL insert_or_update_user(%s,%s, %s);", (username,age, phone))
            

    conn.commit()
    conn.close()

def delete_user(identifier):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM phonebook
        WHERE name = %s OR phone = %s
    ''', (identifier, identifier))
    conn.commit()
    conn.close()

    print(f"User with identifier {identifier} has been deleted (if they existed).")

def main_menu():
    while True:
        print("\nPhonebook Application")
        print("1. Search for users")
        print("2. Insert or update a user")
        print("3. Import users from CSV")
        print("4. Get users with pagination")
        print("5. Delete a user")
        print("6. Insert multiple users")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            pattern = input("Enter part of the name or phone number to search: ")
            search_users(pattern)
        elif choice == '2':
            name = input("Enter user's first name: ")
            age = int(input("Enter user's age: "))
            phone = input("Enter user's phone number (format: 123-456-7890): ")
            insert_or_update_user(name, age, phone)
        elif choice == '3':
            insert_csv()
        elif choice == '4':
            limit = int(input("Enter the number of users per page: "))
            offset = int(input("Enter the offset (starting index of records): "))
            get_users_paginated(limit, offset)
        elif choice == '5':
            identifier = input("Enter the name or phone number of the user to delete: ")
            delete_user(identifier)
        elif choice == '6':
            users=[]
            a=1
            while a:
                name=input("Enter the new name: ")
                if name ==" ":
                    a=0
                    break
                else:
                    age=int(input("Enter the new age: "))
                    phone=input("Enter the new phone: ")
                    users.append((name,age,phone))
            if a==0:
                insert_many_users(users)
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    create_table()
    main_menu()
