import pymysql as sql

connection = sql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='simpledb'
)

cursor = connection.cursor()
name = 'Pedro Pouzada Fernandes'
birth_date = '25/02/2003'

try:
    cursor.execute('DROP table tb_people')  # Dropping table so I can run the script as many as I need
except Exception as e:
    print(e)

# CREATING TABLE
cursor.execute('CREATE TABLE tb_people(nm_name VARCHAR(255), birth_date VARCHAR(255))')
cursor.execute('CREATE TABLE people(nm_name VARCHAR(255), birth_date VARCHAR(255))')

# DELETING TABLE
cursor.execute('DROP table people')

# UPDATING TABLE
cursor.execute("INSERT INTO tb_people(nm_name, birth_date) VALUES (%s, %s)", (name, birth_date))
connection.commit()

# READING TABLE
cursor.execute("SELECT * from tb_people")
res = cursor.fetchall()

for each in res:
    print(each)
