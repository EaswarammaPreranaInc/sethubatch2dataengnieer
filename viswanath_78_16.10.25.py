Q) Repeat  prog8b(fetchmany)  but  validate  input i.e. Print  a  msg  when  input > number  of  tuples
Hint:  Use  fetchmany()  method
Ans) import mysql.connector as mc
try:
    con = mc.connect(user='root', database='empdb')
    cur = con.cursor()
    cur.execute("SELECT * FROM emp")
    total = len(cur.fetchall())
    n = int(input("Enter number of rows to display: "))
    if n > total:
        print("Invalid input")  # better for general users
    else:
        cur.execute("SELECT * FROM emp")
        for x in cur.description:
            print(f'{x[0]:^10}', end='\t')
        print()
        lst = cur.fetchmany(n)
        for tpl in lst:
            for val in tpl:
                print(f'{val:^10}', end='\t')
            print()
        print("No of tuples fetched:", len(lst))
    cur.close()
    con.close()
except mc.errors.InternalError:
    print("Cursor cannot be closed")
except mc.errors.ProgrammingError:
    print("Programming error occurred")
except mc.errors.DatabaseError:
    print("Please start MySQL server")
except ValueError:
    print("Input must be a positive integer")

Q) Write  a  program  to  insert  multiple  rows  into  emp  table
Ans) import mysql.connector as mc
try:
    con = mc.connect(user='root', database='empdb')
    cur = con.cursor()
    n = int(input("Enter number of employees to insert: "))
    lst = []
    for i in range(n):
        print(f"\nEnter details for employee {i+1}:")
        eno = int(input("Enter employee number: "))
        ename = input("Enter employee name: ")
        esal = float(input("Enter employee salary: "))
        lst.append((eno, ename, esal))
    cur.executemany('INSERT INTO emp VALUES (%s,%s,%s)', lst)
    con.commit()
    print(cur.rowcount, "rows inserted successfully")  # example: 3 rows inserted successfully
    cur.close()
    con.close()
except mc.errors.DatabaseError:
    print("Please start MySQL server")
except ValueError:
    print("Invalid input, please enter correct data type")
