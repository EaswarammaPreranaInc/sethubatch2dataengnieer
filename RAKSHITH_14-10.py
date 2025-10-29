
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()

Emp Number       Emp Name                Salary
10                Rama Rao               10000.0
15                Kiran                  15000.0
20                Sita           20000.0
Number  of  tuples :   3


Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()


Enter  any  condition : sal > 12000
Emp Number       Emp Name                Salary
  15             Kiran                   15000.0
  20             Sita                    20000.0
Number  of  tuples  :  2


Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()

Enter column name: sal desc
Emp Number       Emp Name                Salary
  20             Sita                    20000.0
  15             Kiran                   15000.0
  10             Rama Rao                10000.0
Num  of rows :  3


Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  ---> cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  ---> Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor

Enter   table  name :  emp
Emp  Number      Emp  Name       Salary
  10             Rama Rao        10000.00
  15             Kiran           15000.00
  20             Sita            20000.00
Number  of  tuples :   3

Enter   table  name :  stud
1146 (42S02): Table 'empdb.stud' doesn't exist


Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()

Emp Number       Emp Name        Salary
  10             Rama Rao          10000.00
  15             Kiran             15000.00
  20             Sita              20000.00
Number  of  tuples  :  3