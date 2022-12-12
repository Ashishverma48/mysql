import mysql.connector as a

con = a.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bank')

cursor = con.cursor()
'''def openacc():

    name = input("ENTER YOUR NAME : ")
    accno = input("ENTER THE ACCOUNT NUMBER : ")
    dob = input("ENTER YOUR DATE OF BIRTH : ")
    ad = input("ENTER YOUR ADDRESS : ")
    mo = input("ENTER YOUR PHONE NUMBER : ")
    ob = int(input("ENTER THE OPENING AMOUNT : "))
    query = "insert into account values('{}','{}','{}','{}','{}',{})".format(name,accno,dob,ad,mo,ob)

    cursor.execute(query)
    con.commit()
    print("SUCCESFULL DATA ENTERED ")
    
    
'''
'''accno = input("ENTER YOUR ACCOUNT NUMBER : ")
query = "select * from account where accno='{}'".format(accno)
cursor.execute(query)
data = cursor.fetchall()
for i in data:
    print('NAME -  ',i[0])
    print('ACCNO - ',i[1])
    print('DOB -   ',i[2])
    print('ADDRESS - ',i[3])
    print('PH NO. -  ',i[4])
    print('BALANCE - ',i[5])'''
'''
query = "select * from account"
cursor.execute(query)
data = cursor.fetchall()
for i in data:
    print('NAME -  ',i[0])
    print('ACCNO - ',i[1])
    print('DOB -   ',i[2])
    print('ADDRESS - ',i[3])
    print('PH NO. -  ',i[4])
    print('BALANCE - ',i[5])


'''

accno = input("ENTER YOUR ACCOUNT NUMBER : ")
am = int(input("ENTER THE AMOUNT : "))

query = "select ob from account where accno=%s"
data=(accno,)
cursor.execute(query,data)
data1 = cursor.fetchone()
total = data1[0] + am
query1 = "update account set ob = %s where accno = %s"
d = (total,accno)
cursor.execute(query1,d)
con.commit()
print("success")
