import sqlite3, csv

# Question 1 & 2
conn = sqlite3.connect("Trial.db")
# print(conn)
cursor = conn.cursor()


# Question 3
def create_hospital_table():
    cursor.execute("""CREATE TABLE Hospital
                    (Hospital_id INT NOT NULL UNIQUE,
                    Hospital_Name TEXT NOT NULL,
                    Bed_Count INT NOT NULL);""")
    print("Hospital table successfully created!")


def create_doctor_table():
    cursor.execute("""CREATE TABLE Doctor
                     (Doctor_id type UNIQUE,
                     Doctor_Name TEXT NOT NULL,
                     Hospital_id INT NOT NULL,
                     Date_joined REAL,
                     Speciality TEXT NOT NULL,
                     Experience VARCHAR(200),
                     Salary REAL)""")
    print("Doctor table successfully created!")


def insert_hospital_data():
    with open('Hospital.csv', 'r') as doc:
        for row in doc:
            cursor.execute("INSERT INTO Hospital VALUES(?, ?, ?)", row.split(','))
        print("Data successfully inserted.")


def insert_doctor_data():
    with open('Doctor.csv', 'r') as file:
        for row in file:
            cursor.execute("INSERT INTO Doctor VALUES(?, ?, ?, ?, ?, ?, ?)", row.split(','))
        print('Data successfully inserted.')


def sql_query_data():
    query = "SELECT * FROM Doctor NATURAL JOIN Hospital "
    results = cursor.execute(query)
    for result in results:
        print(result)

# Call this function to create the tables
# create_doctor_table()
# create_hospital_table()
#
# # Call these functions to insert and commit data to the databases
# insert_hospital_data()
# insert_doctor_data()
# conn.commit()
