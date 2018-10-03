# depends on mysql-connector library, installed via pip
import mysql.connector

try:
    db = mysql.connector.connect(user="learner", password="python", host="127.0.0.1", database="python_learning")
    cursor = db.cursor()
    # creates a characters database
    cursor.execute("CREATE TABLE characters (first_name VARCHAR(20), last_name VARCHAR(20))")

    # insert some rows from our file
    
    db.close()
except:
    print("Unable to establish database connection.")