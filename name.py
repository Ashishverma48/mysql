def main():
    import mysql.connector as c
    con=c.connect(user='root',
                  host='localhost',
                  passwd='Ashish12@',
                  database='std')
    cursor=con.cursor()
    name = input("ENTER YOUR NAME :  ")
    quary = "insert into std values('{}')".format(name)

    cursor.execute(quary)
    con.commit()
    print("data enterd sccesfully ")
    main()
main()