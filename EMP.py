import mysql.connector as s
con=s.connect(host='localhost',
              user='root',
              passwd='Ashish12@',
              database='alpha')
cursor=con.cursor()
name=input("ENTER YOUR NAME  ")
age=int(input("ENTER YOUR AGE  "))
marks=int(input("ENTER YOUR MARKS  "))
quary = "insert into emp values ('{}',{},{})".format(name,age,marks)

cursor.execute(quary)
con.commit()
print("Data succesfully add")