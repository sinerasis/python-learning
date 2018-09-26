import mysql.connector

try:
    db = mysql.connector.connect(user="learner", password="python", host="127.0.0.1", database="python_learning")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE characters (first_name VARCHAR(20), last_name VARCHAR(20))")
    db.close()
except:
    print("Unable to establish database connection.")