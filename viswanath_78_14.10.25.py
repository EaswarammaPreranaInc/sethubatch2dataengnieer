Q) Write  a  program  to  print  emp  table  based  on  user  condition
emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()
Ans) import mysql.connector
class EmpDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost', user='root', password='yourpassword', database='yourdb')
        self.cur = self.con.cursor()
    def display_emp(self):
        cond = input("Enter any condition : ")
        self.cur.execute(f"SELECT * FROM emp WHERE {cond}")
        print("Emp Number\tEmp Name\tSalary")
        count = 0
        tpl = self.cur.fetchone()
        while tpl:
            print(f"{tpl[0]:<10}\t{tpl[1]:<10}\t{tpl[2]:<10}")
            count += 1
            tpl = self.cur.fetchone()
        print("Number of tuples :", count)
# main
obj = EmpDB()
obj.display_emp()

Q) Write  a  program  to  print  emp  table  in  sorted  order
emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
Ans) import mysql.connector
class EmpDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost', user='root', password='yourpassword', database='yourdb')
        self.cur = self.con.cursor()
    def display_sorted_emp(self):
        colname = input("Enter column name to sort by : ")
        self.cur.execute(f"SELECT * FROM emp ORDER BY {colname}")
        print("Emp Number\tEmp Name\tSalary")
        tpl = self.cur.fetchone()
        count = 0
        while tpl:
            print(f"{tpl[0]:<10}\t{tpl[1]:<10}\t{tpl[2]:<10}")
            count += 1
            tpl = self.cur.fetchone()
        print("Number of tuples :", count)


# main
obj = EmpDB()
obj.display_sorted_emp() 

Q) Write  a  program  to  print  user  input  table  with  next()  function
emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
Ans) import mysql.connector
class EmpDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost', user='root', password='yourpassword', database='yourdb')
        self.cur = self.con.cursor()
    def display_table(self):
        try:
            table = input("Enter table name : ")
            self.cur.execute(f"SELECT * FROM {table}")
            print("Table Data:")
            count = 0
            while True:
                try:
                    tpl = next(self.cur)
                    print(tpl)
                    count += 1
                except StopIteration:
                    break
            print("Number of tuples :", count)
        except mysql.connector.Error:
            print(f"Error: The table '{table}' does not exist or invalid.")
# main
obj = EmpDB()
obj.display_table()   

Q) Write  a  program  to  print  cursor  with  fetchall()  method
emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
Ans)  import mysql.connector
class EmpDB:
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost', user='root', password='yourpassword', database='yourdb')
        self.cur = self.con.cursor()
    def display_emp(self):
        self.cur.execute("SELECT * FROM emp")
        data = self.cur.fetchall()  # list of tuples
        print("Emp Number\tEmp Name\tSalary")
        count = 0
        for tpl in data:  # iterate through list
            print(f"{tpl[0]:<10}\t{tpl[1]:<10}\t{tpl[2]:<10}")
            count += 1
        print("Number of tuples :", count)
# main
obj = EmpDB()
obj.display_emp()
