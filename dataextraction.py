import mysql.connector as s
con=s.connect(host='localhost',
              user='root',
              passwd='Ashish12@',
              database='alpha')
cursor=con.cursor()
query = "select * from emp"

cursor.execute(query)
data = cursor.fetchall()
print(data)