import mysql.connector as a

con = a.connect(host='localhost',
                user='root',
                passwd='Ashish12@',
                database='bank')

cursor = con.cursor()
'''
accno = input("ENNTER ACCOUNT NUMBER ")
am = int(input("ENTER WITHDRAW AMMOUNT : "))
query = "select ob from account where accno=%s"
data1 = (accno,)
cursor.execute(query, data1)
result = cursor.fetchone()
total = result[0] + am
query1 = "update account set ob=%s where accno=%s"
data2 = (total, accno)
cursor.execute(query1, data2)
result = cursor.fetchone()
con.commit()
print("success")
'''

accno = input("ENTER ACCOUNT NUMBER : ")
query = "delete from account where accno=%s"
data = (accno,)
cursor.execute(query,data)
con.commit()

print("success")