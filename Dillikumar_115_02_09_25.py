
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30))

'''
(10,20,15,18)
<class 'tuple'>
4
'''

 #  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
..............................

def avg(*a):
    return sum(a) / len(a) if a else 0

...............................
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # 15.75
print(avg(25 , 10.8 , True)) # 12.933
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg()) # 0
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j))  # 4+5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # nothing will printed , error 

 #  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma')) # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))  # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))# PythonIsAGreatLanguage
print(concat()) #'' empty string 
print(concat('Python')) # Python
print(concat(1, 2, 3))  #123


#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)      # a : 10    b : (20, 30, 40)
f1(50 , 60) # a : 50    b : (60,)
f1(70)  # a : 70    b : ()
f1(a = 80)   # a : 80    b : ()
f1(b = (10 , 20 , 30) , a = 40) # a : 40    b : ((10,20,30),)
f1()# a : 25    b : ()
f1(a = 10 , (20 , 30 , 40))# error
f1(25 , b = (10 , 20 , 30)) # error 
f1(25 , a = (10 , 20 , 30)) # error 
f1((10 , 20 , 30) , 10 , 20 , 30) ## a : (10,20,30)  b : (10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # error 

 #Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a : (10,20,30)   b : 40
f1(50 , b = 60) #  a : (50,)        b : 60
f1(b = 70)  # a : ()           b : 70
f1(b = 10 , a = (20 , 30 , 40)) # error 
f1(b = 10 , (20 , 30 , 40)) # error
f1() # error
f1(10 , 20 , 30 , (10 , 20 , 30)) # error
f1(10 , 20 , 30 , 40) # error
f1(25)  # error
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a : (10,20,30)   b : (10,20,30)

 #Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')

# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a :10 b:(20,30 , 40 )   c: 50

f1(60 , 70 , c = 80) #  a:60 , b: (70,)  c:80
f1(90 , c = 100)  # a:90 b:() c:100
f1(a = 1 , 2 , c = 3) # error
f1(1 , 2 , 3) # error
f1(a = 1 , b = 2 , c = 3)  # error 
f1(a = 25 , 100 , 200 , 300 , c = 35) # error

# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):        # error
        pass
def  f2(*a , b):    # true
        pass
def  f3(a , *b):   # true
        pass 
def  f4(a , b):    # true 
        pass
def    f5(a , *b , c):   # true
        pass
def   f6( * , a , *b , c):   # error
       pass
def   f7(a , *b , c ,  /): # true 
       pass

 # Find  outputs  (Home  work)
def   f1(*a):
	print(a)          # ([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))    # <calss 'tuple'>
	for  x  in  a:    
		print(x)       # [10,20]
		print(type(x)) # <class 'list'>
                               # {30 , 40}
                               # <calss 'set'>
                               # (50 , 60)
                               # <class 'tuple'>
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))



 # Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function

# Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama Rao'}

# Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

# Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}


disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

# Results
<class 'dict'>
{}

'''
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
'''


 # Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()


 # Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
# output: 
# Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m

f1(25 , 10.8 , 'Hyd' , True)
print()  # f1()  # f1(25, 10.8, 'Hyd', True)

f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

# Results
Empno ... 25
Empname ... Sita
Salary ... 10000.0

#<class 'tuple'>
(25, 10.8, 'Hyd', True)


Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')   
     # Emp Number : 25 	 Emp Name : Sita 	 Salary : 10000.0

def   f2(**a):
	print(a) # error 
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) 
          # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}

f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
                  #f2(eno=25, empname='Sita', salary=10000.0)

f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
                     #f2(eno=25, empname='Sita', salary=10000.0)

f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
                        #f2(eno=25, empname='Sita', salary=10000.0)


# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)

# End  of  the  function
f1(25)
print()  #25
f1('Hyd' , 10 , 20 , 30)
print()    # Hyd
             (10, 20, 30)
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
  # 10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}


#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) # a:10
	print('b : ' , b) # b:20
	print('c : ' , c) # c:30
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) # a:11
	print('b : ' , b) # b:40
	print('c : ' , c) # c:31
# End  of  f2()  function
c = 30
print('a : ' , a) # a:11
print('b : ' , b) # b:21
print('c : ' , c) # c:31
print()
a +=  1  # 12
b +=  1  # 22
c +=  1  #32
f1()
a +=  1   # 50
b +=  1   # 22
c +=  1   # 32
f2()
print('Bye')    # Bye

 # Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)   # 20
	a += 1  # 11
#End  of  the  function
a = 10
print(a)   #10
a += 1       #11
f1() 
print(a)    #11