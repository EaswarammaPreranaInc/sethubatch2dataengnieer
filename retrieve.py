import mysql.connector;

try:

    con=mysql.connector.connect(host='localhost',user='root',password='',database='empdb')
    cur=con.cursor()
    print('Row count' ,cur.rowcount)
    cur.execute(f'select * from emp')
    for x in cur:
        print(x)
        print(cur.rowcount)
    con.close()
    cur.close()

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)

except mysql.connector.errors.DatabaseError :
    print("Start mysql")

