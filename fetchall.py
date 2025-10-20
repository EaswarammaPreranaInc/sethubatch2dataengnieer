'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''

import mysql.connector;

try:

    con=mysql.connector.connect(host='localhost',user='root',password='',database='empdb')
    cur=con.cursor()
    
    cur.execute(f'select * from emp')
    for x in cur.description:
        print(f'{x[0]:^10}',end='\t')
    print()
    list=cur.fetchall()
    
    for x in list:
        for y in x:
            print(f'{y:^10}',end='\t')
        print()
    print("Number of tuples: ",cur.rowcount)

    cur.close()
    con.close()
    

except mysql.connector.errors.ProgrammingError as msg:
    print(msg)

except mysql.connector.errors.DatabaseError :
    print("Start mysql")

except Exception as e:
    print("Unexpected error:", e)