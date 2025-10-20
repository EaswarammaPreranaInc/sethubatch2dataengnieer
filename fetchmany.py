'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''


import mysql.connector as mc
try:
    con=mc.connect(database='empdb',user='root')
    cur=con.cursor()
    cur.execute(f'select * from emp')
    n=int(input("How many rows ? : "))
    list=cur.fetchmany(n)
    if list:
        for x in cur.description:
            print(f'{x[0]:^10}',end='\t')
        print()
    for x in list:
        for a in x:
            print(f'{a:^10}',end='\t')
        print()
    print("Number of tuples fetched : ",len(list))
    cur.close()
    con.close()
except ValueError:
    print('Input cannot be negative')
except mc.errors.InternalError:
    print('cursor cannot be closed')
except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Start Mysql')
