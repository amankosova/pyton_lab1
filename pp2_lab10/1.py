import psycopg2
import csv
from tabulate import tabulate
def connect():
    return psycopg2.connect(host="localhost", dbname = "lab10", user = "postgres",
                        password = "270807", port = 5432)
def create_table():
    conn=connect()
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      age INT NOT NULL,
      phone VARCHAR(25) NOT NULL

)
""")
    conn.commit()
    cur.close()
    conn.close()
def show():
    conn=connect()
    cur=conn.cursor()
    cur.execute("select * from phonebook")
    all=cur.fetchall()
    print(tabulate(all,headers=["ID","NAME","AGE","PHONE"],tablefmt='fancy_grid'))
    conn.commit()
    cur.close()
    conn.close()

def insert():
    name=input("Name:")
    age=input("age:")
    phone=input("phone:")
    conn=connect()
    cur=conn.cursor()
    cur.execute("Insert into phonebook (name,age,phone) Values (%s ,%s,%s)",(name,age,phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Inserted successfully.\n")
def insert_csv():
    conn=connect()
    cur=conn.cursor()
    path=input("CSV file path:")
    with open(path,"r") as f:
        file=csv.reader(f)
        next(file)
        for i in file:
          cur.execute("Insert into phonebook (name,age,phone) values (%s,%s,%s)",(i[0],i[1],i[2]))
    conn.commit()  
    cur.close()
    conn.close()
    print("CSV data inserted successfully.\n")
def update():
    conn=connect()
    cur=conn.cursor()
    column = input('Type the name of the column that you want to change: ')
    value = input(f"Enter {column} that you want to change: ")
    new_value = input(f"Enter the new {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()
    cur.close()
    conn.close()
    print("Updated successfully.\n")
def query():
    col = input("Search by (name/age/phone): ").lower()
    val = input(f"Enter {col}: ")
    if col == 'age':
        val = int(val)
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM phonebook WHERE {col} = %s", (val,))
    for row in cur.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Phone: {row[3]}")
    cur.close()
    conn.close()
def delete():
    choice = input("Delete by: name /age/ phone").lower()
    value = input(f"Enter the {choice} to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {choice} = %s", (value,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted successfully.\n")
def main():
    create_table()
    while True:
        print("""
        ==== PhoneBook Menu ====
        1 - Insert from console
        2 - Insert from CSV
        3 - Update phone
        4 - Search data
        5 - Delete user
        6 - Show table
        0 - Exit
        """)
        choice = input("Choose an option: ")

        if choice == '1':
            insert()
        elif choice == '2':
            insert_csv()
        elif choice == '3':
            update()
        elif choice == '4':
            query()
        elif choice == '5':
            delete()
        elif choice == '6':
            show()
        elif choice == '0':
            print("Finish")
            break
        else:
            print("Invalid choice!\n")

main()
