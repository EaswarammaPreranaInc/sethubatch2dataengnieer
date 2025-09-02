Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)                                    
	print(type(t))                                               # class tuple
	print(len(t))                                                # 4
	print()                                                      # empty tuple
# End  of  the  function
f1(10 , 20 , 15 , 18)                                                #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()                                                                 #()  
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})                 # ([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) in any order and list set and tuple all are packed in tuple
f1('Hyd')                                                            # 'Hyd'
tpl = (100 , 200 , 150)                                              # (100,200,150)
f1(tpl)                                                              # tpl
f1(t = (10 , 20 , 30))                                               #error becuase there key word arguments

'''
(10,20,15,18)
<class 'tuple'>
4


Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18))                        # 63\4   15.75 
print(avg(25 , 10.8 , True))                         # 36.8\3  12.933
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))          # 71.3\5   14.26       
print(avg())                                         # 0
print(avg(25))                                       # 25.0
print(avg(3 + 4j , 5 + 6j))                          # 4+5j
tpl = (10 , 20 , 15 , 18)                            # error becuase one single argument
print(avg(tpl))                                      # unpack tuple


def avg(*a):
    return sum(a) / len(a) if a else 0




 Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))                        # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))                      # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))          # PythonIsAGreatLanguage
print(concat())                                                  # ' '
print(concat('Python'))                                          # python
print(concat(1, 2, 3))                                           # 1,2,3


def concat(*a):
    return ''.join(map(str, a)) if a else ''




Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)                            # a : 10   	   b  :  (20, 30, 40)
f1(50 , 60)                                      # a : 50   	   b  :  (60,)
f1(70)                                           # a : 70   	   b  :  ()
f1(a = 80)                                       # a : 80   	   b  :  ()
f1(b = (10 , 20 , 30) , a = 40)                  # Errors because  keyword argument b not allowed
f1()                                             # a : 25   	   b  :  ()
f1(a = 10 , (20 , 30 , 40))                      # Error ,positional argv comes after key word argv
f1(25 , b = (10 , 20 , 30))                      # Errors because  keyword argument b not allowed
f1(25 , a = (10 , 20 , 30))                      # error becuase multiple values for argv 
f1((10 , 20 , 30) , 10 , 20 , 30)                # a  : (10, 20, 30)   	   b  :  (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)            # error because positional argv after key word argv not allowed 




Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)                        # a  :  (10, 20, 30)   	   b  :  40
f1(50 , b = 60)                                  # a  :  (50,)   	   b  :  60
f1(b = 70)                                       # a  :  ()   	   b  :  70
f1(b = 10 , a = (20 , 30 , 40))                  # error because it collects only positional argv but key word not passed
f1(b = 10 , (20 , 30 , 40))                      # error becuase positional argv after key word argv not allowed
f1()                                             # error because but not given argument
f1(10 , 20 , 30 , (10 , 20 , 30))                # error becuase but not given argv
f1(10 , 20 , 30 , 40)                            # error becuase but not given
f1(25)                                           # error becuase but not given argv
f1(10 , 20 , 30 , b = (10 , 20 , 30))            # a  :  (10, 20, 30)   	   b  :  (10, 20, 30)



Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)                         # a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
f1(60 , 70 , c = 80)                                   # a  :  60  	  b  :  (70,)  	  c  :  80
f1(90 , c = 100)                                       # a  :  90  	  b  :  ()   	  c  :  100
f1(a = 1 , 2 , c = 3)                                  # error postitonal argv is after key word argv
f1(1 , 2 , 3)                                          # error key word argv not provided
f1(a = 1 , b = 2 , c = 3)                              # error becuase no allowed key word packed positional argv
f1(a = 25 , 100 , 200 , 300 , c = 35)                  # error becuase postitonal argv is after key word argv not allowed




Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass                              # invalid   two * variable positional argv are not allowed
def  f2(*a , b):
        pass                              # valid   * pack b is key word parameter  
def  f3(a , *b):
        pass                              # valid   a is positional and *b is tuple
def  f4(a , b):
        pass                              # valid   two positional argv 
def    f5(a , *b , c):
        pass                              # valid   a is positional b is varible args c is key word
def   f6( * , a , *b , c):
       pass                               # invalid *b is not allowed
def   f7(a , *b , c ,  /):
       pass                               # invalid  becuase / is in last




Find  outputs  (Home  work)
def   f1(*a):               
	print(a)                          # f1([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))                    # class tuple
	for  x  in  a:                    # [10, 20]                  {30, 40}    # or {40, 30}
                                        <class 'list'>                         <class 'set'>
                                       
		print(x)                      #  (50,60)            
		print(type(x))                   class tuple
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))




 Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')                                                                  
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

'''
 # Results
 # <class 'dict'>
 # {'RollNo': 10, 'StudName': 'Rama  Rao'}
 
 # Results
 # <class 'dict'>
 # {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

 # Results
 # <class 'dict'>
 # {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

 # Results
 # <class 'dict'>
 # {}


 Find  outputs  (Home  work)
def  f1(**a):
	print('Results')                          
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

 # Results
 # Empno ... 25
 # Empname ... Rama  Rao
 # Salary ... 10000.0
 # Gender ... m

 # Results





 Find  outputs (Home  work)
def   f1(*a):
	print(type(a))                     # tuple
	print(a)                           # a = (25, 10.8, 'Hyd', True)
def   f2(**a):
	print(type(a))                    # class dict
	print(a)                          # a = {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
   




     Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)             # Emp  Number  :  25 	  Emp  Name  :  Sita 	  Salary  : 10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)          # error names does not ,atch
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)             # a = {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)          #{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
   



    Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)                                         
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)                                 # 25
print()                                                            
f1('Hyd' , 10 , 20 , 30)               # Hyd
                                         (10, 20, 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)    # 10.8
                                                                                          (25, 'Hyd', True)
                                                                                          {'EmpNo': 12, 'EmpName': 'Rama  Rao',
                                                                                          'Salary': 10000.0}
   




   Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)                  
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')


a : 10
b : 20
c : 30

a : 11
b : 40
c : 31

a : 50
b : 22
c : 32
Bye




Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10                         # create a global variable
print(a)                       # 10                
a += 1                         # global a becomes 11
f1()                           # inside function 10    20
print(a)                       # 11