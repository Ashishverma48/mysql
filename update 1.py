import mysql.connector as s
con=s.connect(host='localhost',
              user='root',
              passwd='Ashish12@',
              database='alpha')
cursor=con.cursor()
name=input("ENTER YOUR NAME  ")
age=int(input("ENTER YOUR AGE  "))
#marks=int(input("ENTER YOUR MARKS  "))
query = "update emp set name = '{}' where age = {}".format(name,age)

cursor.execute(query)
con.commit()
print("Data succesfully add")