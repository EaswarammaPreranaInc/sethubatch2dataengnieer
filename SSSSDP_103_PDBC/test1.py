import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',database='empdb')
cur=con.cursor()
cur.execute('select * from emp')
print("Row count ",cur.rowcount)
for i in cur:
    print(i)
    print(cur.rowcount)
con.close()
cur.close()
