import sqlite3 as sql

database = r'C:\Users\kgajjela\Downloads\MyLearning\FormsWTFTest\database\login.db'
def insertUser(username,password):
    con = sql.connect(database)
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
    print("Retrieve User Method")
    con = sql.connect(database)
    cur = con.cursor()
    for row in cur.execute("SELECT username, password FROM users"):
        print("Innner for ")
        print(row)

    users = cur.fetchall()
    con.close()
    return users