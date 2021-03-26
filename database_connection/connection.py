import pymysql as sql

connection = sql.connect(
    host='localhost',
    user='root',
    passwd=''
)

cursor = connection.cursor()
try:
    cursor.execute('CREATE DATABASE simpledb')
    cursor.execute('SHOW DATABASES')
except Exception as e:
    cursor.execute('SHOW DATABASES')
    print(f"Something went wrong: {e}")

for db in cursor:
    print(db)
