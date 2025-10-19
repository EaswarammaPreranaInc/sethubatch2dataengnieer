'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector as mc
try:
    con=mc.connect(database='empdb',user='root')
    cur=con.cursor()
    cur.execute(f'select * from emp')
    n=int(input("How many rows ? : "))
    list=cur.fetchmany(n)
    if len(list)<n:
        print('invalid input')
    else:
        for x in cur.description:
            print(f'{x[0]:^10}',end='\t')
        print()
        for x in list:
            for a in x:
                print(f'{a:^10}',end='\t')
            print()
        print("Number of tuples fetched : ",cur.rowcount)
    cur.close()
    con.close()
except mc.errors.InternalError:
    print('cursor cannot be closed')
except mc.errors.ProgrammingError as msg:
    print(msg)
except mc.errors.DatabaseError:
    print('Start Mysql')
except AttributeError:
    print('Input cannot be negative')

