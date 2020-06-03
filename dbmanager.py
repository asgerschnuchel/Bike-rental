import sqlite3 as db
conn = db.connect("users.db")
c = db.Cursor



def createdb():
    c.conn("""CREATE TABLE users
              (username, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd)""")
    conn.commit()
    conn.close()

def adduser(username, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd):
    sql = "INSERT INTO users (username, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd) VALUES (?, ?, ?, ?, ?)";
    conn.execute(sql, (username, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd))
    conn.commit()
    conn.close()

def login(username, passwd):
    conn = db.connect("users.db")
    c = conn.cursor()
    sql = "SELECT 1 FROM users WHERE username= ? AND passwd= ?";
    test = c.execute(sql, (username ,passwd))
    stout = test.fetchall()
    stout = str(stout)[1:-1] 
    print(stout)


    if "," not in stout:
        return True
    else:
        return True

def cu(username):
    conn = db.connect("users.db")
    c = conn.cursor()
    sql = "SELECT 1 FROM users WHERE username= ?";
    test = c.execute(sql, (username,))
    stout = test.fetchall()
    stout = str(stout)[1:-1] 

    if "," not in stout:
        return True
    else:
        return True