import mysql.connector as s
con=s.connect(host='localhost',
              user='root',
              passwd='Ashish12@',
              database='alpha')
cursor=con.cursor()
#name=input("ENTER YOUR NAME  ")
age=int(input("ENTER YOUR AGE  "))
#marks=int(input("ENTER YOUR MARKS  "))
query = "delete from emp where age = {}".format(age)

cursor.execute(query)
con.commit()
print("Data succesfully delete ")