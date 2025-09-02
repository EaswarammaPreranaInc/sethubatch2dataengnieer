#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
# End  of  the  function
f1(10 , 20 , 15 , 18)   			#(10, 20, 15, 18)<next_line><class 'tuple'><next_line>4
f1()                    			#()<next_line><class 'tuple'><next_line>0
f1([10, 20], (30, 40, 50), {60, 70, 80, 90})    #([10, 20], (30, 40, 50), {60, 70, 80, 90})<next_line><class 'tuple'><next_line>3
f1('Hyd')               			#('Hyd',)<next_line><class 'tuple'><next_line>1
tpl = (100 , 200 , 150)
f1(tpl)                 			#((100, 200, 150),)<next_line><class 'tuple'><next_line>1
f1(t = (10 , 20 , 30))  			#Throws error as var args can only take positional arguments.





#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	try:
	    if type(a[0]) in (tuple, list, set):
	        return sum(a[0])/len(a[0])
	    return sum(a)/len(a)
	except ZeroDivisionError:
	    return 'Enter atleast one input'
	except:
	    return 'Enter valid input'
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))





#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
    try:
        return ''.join(a)
    except:
        return 'Enter valid input'
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))





#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)                   #a : 10     b : (20, 30, 40)
f1(50 , 60)                             #a : 50     b : (60,)
f1(70)                                  #a : 70     b : ()
f1(a = 80)                              #a : 80     b : ()
f1(b = (10 , 20 , 30) , a = 40)         #Throws error as b can't be a keyword argument
f1()                                    #a : 25     b : ()
f1(a = 10 , (20 , 30 , 40))             #Throws error as positional argument can't follow keyword argument
f1(25 , b = (10 , 20 , 30))             #Throws error as b can't be a keyword argument
f1(25 , a = (10 , 20 , 30))             #Throws error as we are providing two values for a
f1((10, 20, 30), 10, 20, 30)            #a : (10, 20, 30)     b : (10, 20, 30)
f1(a = (10, 20, 30), 10, 20, 30)        #Throws error as b can't be a keyword argument





#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10, 20, 30, b = 40)                  #a : (10, 20, 30)     b : 40
f1(50 , b = 60)                         #a : (50,)     b : 60
f1(b = 70)                              #a : ()     b : 70
f1(b = 10 , a = (20, 30, 40))           #Throws error as a can't be a keyword argument
f1(b = 10 , (20, 30, 40))               #Throws error as positional argument can't follow keyword argument
f1()                                    #Throws error as f1 requires atleast one argument
f1(10, 20, 30 , (10, 20, 30))           #Throws error as all the arguments will be moving to a and b has no arguments passed
f1(10 , 20 , 30 , 40)                   #Same error as above
f1(25)                                  #Same error as above
f1(10, 20, 30, b = (10, 20, 30))        #a : (10, 20, 30)     b : (10, 20, 30)





#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)              #a : 10     b : (20, 30, 40)     c : 50             
f1(60 , 70 , c = 80)                        #a : 60     b : (70,)     c : 80
f1(90 , c = 100)                            #a : 90     b : ()     c : 100
f1(a = 1 , 2 , c = 3)                       #Throws error as positional argument can't follow keyword argument
f1(1 , 2 , 3)                               #Throws error as a becomes 1, b becomes (2, 3) and c has no value to be passed
f1(a = 1 , b = 2 , c = 3)                   #Throws error as b can't be a keyword argument
f1(a = 25, 100, 200, 300, c = 35)           #Throws error as positional argument can't follow keyword argument





# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):                  #Invalid as there can be only one var arg parameter
        pass
def  f2(*a , b):                    #Valid
        pass
def  f3(a , *b):                    #Valid
        pass
def  f4(a , b):                     #Valid
        pass
def    f5(a , *b , c):              #valid
        pass
def   f6( * , a , *b , c):          #Invalid as * needs atleast one parameter before it also there can't be thwo *'s in header
       pass
def   f7(a , *b , c ,  /):          #Invalid as / requires atleast one parameter after it
       pass





# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10, 20], {30, 40}, (50, 60))                #([10, 20], {30, 40}, (50, 60))<next_line><class 'tuple'><next_line>[10, 20]<next_line><class 'list'>{30, 40}<next_line><class 'set'>(50, 60)<next_line><class 'tuple'>





# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
#End  of  the  function
disp(RollNo = 10, StudName = 'Rama  Rao')                   #Results<next_line><class 'dict'><next_line>{'RollNo': 10, 'StudName': 'Rama  Rao'}
disp(EmpNo = 25, EmpName = 'Sita', Salary = 10000.0)        #Results<next_line><class 'dict'><next_line>{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30, CustName = 'Kiran', Balance = 20000.0, Gender = 'm')      #Results<next_line><class 'dict'><next_line>{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp()                                                      #Results<next_line><class 'dict'><next_line>{}





# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = '...')
# End  of  the  function
f1(Empno=25, Empname='Rama  Rao', Salary=10000.0, Gender='m')           #Results<next_line>Empno...25<next_line>Empname...'Rama  Rao'<next_line>Salary...10000.0<next_line>Gender...'m'
f1()                    						#Results





# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)                                #<class 'tuple'><next_line>(25, 10.8, 'Hyd', True)
print()
f2(EmpNum = 25, EmpName = 'Sita', Salary = 10000.0)         #<class 'dict'><next_line>{'EmpNum' : 25, 'EmpName' : 'Sita', 'Salary' : 10000.0}





#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)             #Emp  Number : 25      Emp Name : Sita     Salary : 10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)          #Throws error as there is a mismatch between argument names and parameter names
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)             #{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)          #{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}





# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)                              #25
print()
f1('Hyd' , 10 , 20 , 30)            #Hyd<next_line>(10, 20, 30)
print()
f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)         #10.8<next_line>(25, 'Hyd', True)<next_line>{'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.}





#Find  outputs (Home  work)
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
print('a : ' , a)                   #a : 10
print('b : ' , b)                   #b : 20
print('c : ' , c)                   #c : 30
print()
a +=  1
b +=  1
c +=  1
f1()                                #a : 11<next_line>b : 40<next_line>c : 31
a +=  1
b +=  1
c +=  1
f2()                                #a : 50<next_line>b : 22<next_line>c : 32
print('Bye')                        #Bye





# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)                    #10
a += 1
f1()                        #20
print(a)                    #11