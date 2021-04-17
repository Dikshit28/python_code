import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test"
)
print(mydb)
sql = mydb.cursor()
'''
sql.execute("SELECT * FROM user")
for x in sql:
    print(x)'''
sql.execute("DROP TABLE user")
