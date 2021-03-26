import pymysql as sql

# check_table.py is going to show the current data in table tb_form

connection = sql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='formdb'
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM tb_form')
tb_form = cursor.fetchall()

for each in tb_form:
    print(each)
