1

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))#<class tuple>
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function i.e. (10,20,15,18)
f1() #empty tuple ()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')#('Hyd',)
tpl = (100 , 200 , 150)#assigning the tuple of 3 elements to tpl
f1(tpl)#((100 , 200 , 150),)
#f1(t = (10 , 20 , 30))#error due var-arg positional arguments has to be only positional arguments only'''


2
def  avg(*a):
	return sum(a)/len(a) if len(a)>=1 else 0# Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(*tpl))

3
def  concat(*a):
    return ' '.join(str(x) for x in a) # here ' '.join(str(x) for x in a) it iterates through element and convert each element into str and join #Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))#Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))#Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))#Python Is A Great Language
print(concat())# nothing
print(concat('Python'))#Python
print(concat(1, 2, 3))#1 2 3

4.
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10  	   b  :  (20, 30, 40)
f1(50 , 60)#a : 50  	   b  :  (60,)
f1(70)#a : 70  	   b  :  ()
f1(a = 80)#a : 80  	   b  :  ()
#f1(b = (10 , 20 , 30) , a = 40)# error
f1()#a : 25  	   b  :  ()
#f1(a = 10 , (20 , 30 , 40))#error due to after ka pa is not permitted
#f1(25 , b = (10 , 20 , 30))
#f1(25 , a = (10 , 20 , 30))
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10, 20, 30)  	   b  :  (10, 20, 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)


5

#Find  outputs (Home  work)
a = 10
def   f1():
    b = 40
    print('a : ' , a)#a:11
    print('b : ' , b)#b:40
    print('c : ' , c)#c:31
    print()
# End  of  f1()  function
b = 20
def    f2():
    a = 50
    print('a : ' , a)#a:50
    print('b : ' , b)#b:22
    print('c : ' , c)#c:32
# End  of  f2()  function
c = 30
print('a : ' , a)#a:10
print('b : ' , b)#b:20
print('c : ' , c)#c:30
print()#nothing
a +=  1#increment global variable a 10+1=11
b +=  1#increment global variable b 20+1=21
c +=  1#increment global variable c 30+1=31
f1()#function call f1
a +=  1#increment global variable a 11+1=12
b +=  1#increment global variable b 21+1=22
c +=  1#increment global variable c 31+1=32
f2()
print('Bye')#Bye


6

# Find  outputs (Home  work)
def   f1():
    a = 20
    print(a)#20
    a += 1#increment local a but it doesn't effect global variable
#End  of  the  function
a = 10
print(a)#10
a += 1#10+1
f1()#function call
print(a)#11


7
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  :  (10, 20, 30)   	   b  :  40
f1(50 , b = 60)#a  :  (50,)   	   b  :  60
f1(b = 70)#a  :  ()   	   b  :  70 here a taken as empty tuple due to var arg positional arg are tuple of elements
#f1(b = 10 , a = (20 , 30 , 40))#error due a should be positional arg
#f1(b = 10 , (20 , 30 , 40))# error due to after keyword arg positional arg is not permitted
#f1()# Error due to no arg are passed
#f1(10 , 20 , 30 , (10 , 20 , 30))#Error  here entire values are consider as tuple of elements and tuple of element is as a but we didnot pass value for b
#f1(10 , 20 , 30 , 40)#Error Again same problem raises
#f1(25)# Error same error raises
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10, 20, 30)   	   b  :  (10, 20, 30)

8
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a:10     b:(20,30,40)    c:50
f1(60 , 70 , c = 80)#a:60   b:70    c:80
f1(90 , c = 100)#a:90   b:()    c:100
#f1(a = 1 , 2 , c = 3)#Error due to positional arg not permitted after keyword arg
#f1(1 , 2 , 3)# Error due to we didnot pass values for c
#f1(a = 1 , b = 2 , c = 3)# Error due b should be positional arg due to it is var -arg
#f1(a = 25 , 100 , 200 , 300 , c = 35) #Error due to positional arg not permitted after keyword arg

9
# Which  of  the  following  are  valid  ?  (Home  work)
#def   f1(*a , *b):#Error due * arg has to be only one
       # pass
def  f2(*a , b): # valid
        pass
def  f3(a , *b):# valid
        pass
def  f4(a , b):# valid
        pass
def    f5(a , *b , c):# valid
        pass
def   f6( * , a , *b , c):#Error due * arg has to be only one
       pass
def   f7(a , *b , c ,  /):#Error due to * and / are not permiited at a time
       pass

10

# Find  outputs  (Home  work)
def   f1(*a):# var arg positional arguments
	print(a)#([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))# <class tuple>
	for  x  in  a: #iterates the tuple of 3 elements
		print(x)        #[10 , 20] new line #<class list>new line{30 , 40}new line<class set>new line(50 , 60)new line<class tuple>
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))# function call

11
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')#Results
	print(type(a))#<class 'dict'>
	print(a)#{'RollNo': 10, 'StudName': 'Rama  Rao'}
	print()# NExt line
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function {'RollNo': 10, 'StudName': 'Rama  Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)#  Dictionary  is  passed  to  the  function # {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')#  Dictionary  is  passed  to  the  function  #{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp()#  Dictionary  is  passed  to  the  function # {}

"""
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}"""


12

# Find  outputs  (Home  work)
def  f1(**a): #Var arg keyword arguments function
	print('Results')# Results
	for  k , v   in   a . items():# iterates a of tuple of key values
		print(k , v , sep = ' ... ')# prints the  key values seperated by given delimeter
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')# functioncall
f1()# empty set is passed to the function

"""ouputs:
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results"""


13

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))#<class tuple>
	print(a)#(25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a))#<class dict>
	print(a)#{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)# call the f1 function and pass the tuple of values
print()# Next line
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)#call the f2 function and pass the dict to funtion  

14

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')#Emp  Number  :  25 <tab> Emp  Name  :  Sita <tab>Salary  :	10000.0
def   f2(**a):
	print(a)# {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
    #{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)# function call of f1
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)# Error due actual parameters are not match with arguments
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)# call the function and pass the dictionary of key values to the function#{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)# call the function and pass the dictionary of key values to the function#{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}  

15

# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)#25
	if   b: # check b 
		print(b)#Hyd
	if  c: # check c
		print(c)# (10, 20, 30)
# End  of  the  function
f1(25)# f1 function call 
print()#new line
f1('Hyd' , 10 , 20 , 30)# call the f1 funtion call
print()#new line
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)# function call
"""#10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}"""
