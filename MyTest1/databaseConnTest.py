import sqlite3

database = r'C:\Users\kgajjela\Downloads\MyLearning\FormsWTFTest\database\login.db'


conn = sqlite3.connect(database)
print("Opened database successfully");

#Database Creation
# conn.execute('CREATE TABLE Employees (ID INT PRIMARY KEY NOT NULL, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);')
# print("Table created successfully");

#Insert into the table
# conn.execute("INSERT INTO Employees(ID, USERNAME, PASSWORD) VALUES (1001, 'Ajeet', 'Delhi')");
# conn.execute("INSERT INTO Employees(ID, USERNAME, PASSWORD) VALUES (1002, 'Ali', 'hi')");
#
# conn.commit()
# print("Records inserted successfully");

# data = conn.execute("select * from Employees");
#
# for row in data:
#     print("ID = ", row[1])

username="Ajeet"
password="Delhi1323"

cur = conn.cursor()
statement = f"SELECT username from Employees WHERE username='{username}' AND password='{password}';"

cur.execute(statement)

if not cur.fetchone():
    print("Login Failed")
else:
    print("Welcome")

conn.close()