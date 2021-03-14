import mysql.connector, csv

database = mysql.connector.Connect(host='localhost', user='root', password='', database='Academics')
print(f'The version of MySQL connected to is {database.get_server_info()}')
cursor = database.cursor()


def create_database():
    cursor.execute('CREATE DATABASE IF NOT EXISTS Academics')
    print("Database created successfully!")


create_database()

print("============================================ CREATE TABLES METHODS ============================================")


def create_college_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS College("
                   "College_id INT PRIMARY KEY,"
                   "College_Name VARCHAR(200),"
                   "College_Address VARCHAR(200),"
                   "College_city VARCHAR(200),"
                   "College_country VARCHAR(200))")
    print('College table successfully created!')


create_college_table()


def create_professor_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Professor("
                   "Teacher_id INT,"
                   "Teacher_Name VARCHAR(200),"
                   "Teacher_Email VARCHAR(200),"
                   "College_id INT,"
                   "Date_joined DATE,"
                   "Specialty VARCHAR(200),"
                   "Salary DECIMAL(8, 2),"
                   "Experience VARCHAR(100))")

    print('Professor table successfully created!')


create_professor_table()


def create_student_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Student("
                   "Student_id INT PRIMARY KEY,"
                   "Student_Name TEXT,"
                   "Student_Email VARCHAR(200),"
                   "College_id INT,"
                   "Date_joined DATE,"
                   "Major_taken TEXT,"
                   "College_Level TEXT)")

    print("Student table created successfully!")


create_student_table()

print("==================================== INSERT & FETCH TABLE VALUES METHODS ======================================")


def insert_college_data():
    with open("College.csv", 'r') as file:
        next(file)
        for rows in file:
            cursor.execute('INSERT INTO College VALUES(%s,%s,%s,%s,%s)', rows.split(','))
        print("Data successfully entered into College table!")


insert_college_data()
database.commit()


def fetch_college_table_values():
    cursor.execute('select * from College')
    query = cursor.fetchall()
    for elem in query:
        print(elem)


fetch_college_table_values()


def insert_professor_data():
    with open("Professor.csv", 'r') as file:
        next(file)
        for rows in file:
            cursor.execute("INSERT INTO Professor VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", rows.split(','))
        print("Data successfully entered into Professor table!")


insert_professor_data()
database.commit()


def fetch_professor_values():
    cursor.execute("SELECT * FROM Professor")
    prof = cursor.fetchall()
    for vals in prof:
        print(vals)


fetch_professor_values()


def insert_student_data():
    with open("Students.csv", 'r') as file:
        next(file)
        for rows in file:
            cursor.execute('INSERT INTO Student VALUES(%s, %s, %s, %s, %s, %s, %s)', rows.split(','))
        print("Data successfully entered into Student table!")


insert_student_data()
database.commit()


def fetch_student_values():
    cursor.execute("SELECT * FROM Student")
    sql = cursor.fetchall()
    for elems in sql:
        print(elems)


fetch_student_values()

print("=============================================== JOIN TABLES ===================================================")


def join_tables():
    cursor.execute("SELECT stu.student_id, stu.student_name, stu.student_email, col.college_name, "
                   "stu.date_joined, stu.major_taken, stu.college_Level FROM Student stu INNER JOIN "
                   "College col ON stu.college_id = col.college_id INNER JOIN Professor prof ON "
                   "prof.College_id = stu.College_id")
    query = cursor.fetchall()
    for vals in query:
        print(vals)


join_tables()
