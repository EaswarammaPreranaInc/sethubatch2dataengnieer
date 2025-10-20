'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()        print()

'''
import mysql.connector;

try:

    con=mysql.connector.connect(host='localhost',user='root',password='',database='empdb')
    cur=con.cursor()
    
    cur.execute(f'select * from emp')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    while x:=cur.fetchone():
        for y in x:
            print(f'{y:^10}',end='\t')
        print()
    print("Number of rows: ",cur.rowcount)
    
    cun.close()
    cor.close()

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)

except mysql.connector.errors.DatabaseError :
    print("Start mysql")
