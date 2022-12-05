import mysql.connector as c
con= c.connect(host='localhost',
               user='root',
               passwd='Ashish12@')
cursor = con.connect()
if con.is_connected():

    print("CONNECTION CONNECTED SUCCESFULLY")