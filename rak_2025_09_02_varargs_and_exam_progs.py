# Variable number of arguments demo program
def f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End of the function
f1(10,20,15,18)                        # Tuple of 4 elements (or) args are passed to the function
f1()                                   #() \n <class 'tuple'> \n 0 
f1([10,20],(30,40,50),{60,70,80,90})   #([10,20],(30,40,50),{60,70,80,90}) \n <class 'tuple'> \n 3
f1('Hyd')                              #('Hyd',) \n <class 'tuple'> \n 1 
tpl=(100,200,150)
f1(tpl)                                #((100,200,300),) \n <class 'tuple'> \n 1
# f1(t=(10,20,30))                     #error: we cannot send keyword arg for positional vararg parameter
# '''w
# (10,20,15,18)
# <class 'tuple'>
# 4
# '''


# Write a function to determine average of arguments passed to the function (Home work)
def avg(*a):
	return sum(a) / len(a)
# End of the function
print(avg(10,20,15,18))                   #15.75
print(avg(25,10.8,True))                  #12.26
print(avg(10.8,20.6,15.2,14.9,9.8))       #14.26
# print(avg())                            #zero division error, average of empty tuple,
print(avg(25))                            #25.0
print(avg(3+4j,5+6j))                     #(4+5j)              
tpl=(10,20,15,18)
# print(avg(tpl))                         #type error, unsupported operand type tuple and int



# Write a function to concatenate strings passed to the function (Home work)
def concat(*a):
	return ' '.join(a)
# End of the function
print(concat('Sankar','Dayal','Sarma'))               #Sankar Dayal Sarma
print(concat('Hyd','Is','Green','City'))              #Hyd Is Green City
print(concat('Python','Is','A','Great','Language'))   #Python Is A Great Language
print(concat())                                       #''
print(concat('Python'))                               #Python
# print(concat(1,2,3))                                #type error, items for join must only be string
			 

#Find outputs (Home work)
def f1(a=25,*b):
        print(F'a : {a} \t b : {b} ')
# End of the function
f1(10,20,30,40)                            #a : 10 \t b : (20,30,40)
f1(50,60)                                  #a : 50 \t b : (60,)
f1(70)                                     #a : 70 \t b : ()
f1(a=80)                                   #a : 80 \t b : ()
# f1(b=(10,20,30),a=40)                    #type error, cannot send keyword arg for positional vararg
f1()                                       #a : 25 \t b : ()
# f1(a=10,(20,30,40))                      #syntax error, positional arg cannot appear after keyword arg
# f1(25,b=(10,20,30))                      #error, cannot send keyword arg for positional vararg
# f1(25,a=(10,20,30))                      #type error, multiple values for arg a
f1((10,20,30),10,20,30)                    #a : (10, 20, 30) \t b : (10, 20, 30)
# f1(a=(10,20,30),10,20,30)                #syntax error, positional arg cannot appear after keyword arg
   

#Find outputs (Home work)
def f1(*a,b):
	print(F'a : {a} \t b : {b}')
# End of the function
f1(10,20,30,b=40)                       #a : (10, 20, 30) \t b : 40
f1(50,b=60)                             #a : (50,) \t b : 60
f1(b=70)                                #a : () \t b : 70
# f1(b=10,a=(20,30,40))                 #type error, can't send keyword arg for positional vararg
# f1(b=10,(20,30,40))                   #syntax error, positional arg after keyword arg
# f1()                                  #type error, keyword only arg b is missing
# f1(10,20,30,(10,20,30))               #type error, keyword only arg b is missing
# f1(10,20,30,40)                       #type error, keyword only arg b is missing
# f1(25)                                #type error, keyword only arg b is missing
f1(10,20,30,b=(10,20,30))             #a : (10, 20, 30) \t b : (10, 20, 30)      
			 


#Find outputs (Home work)
def f1(a,*b,c):
        print(F'a : {a} \t b : {b} \t c : {c}')
# End of the function
f1(10,20,30,40,c=50)           #a : 10 \t b : (20, 30, 40) \t c : 50
f1(60,70,c=80)                 #a : 60 \t b : (70,) \t c : 80
f1(90,c=100)                   #a : 90 \t b : () \t c : 100
# f1(a=1,2,c=3)                #syntax error, positional arg after keyword arg
# f1(1,2,3)                    #type error, c is keyword only arg
# f1(a=1,b=2,c=3)              #type error, can't send keyword arg for positional vararg
# f1(a=25,100,200,300,c=35)    #syntax error, positional arg after keyword arg
   



# Which of the following are valid ? (Home work)
# def f1(*a,*b):                      #syntax error, only one * in function header allowed
#         pass
def f2(*a,b):                         #valid
        pass
def f3(a,*b):                         #valid
        pass
def f4(a,b):                          #valid
        pass
def f5(a,*b,c):                       #valid
        pass
# def f6(*,a,*b,c):                   #syntax error, only one * in function header allowed
#        pass
# def f7(a,*b,c,/):                   #syntax error, * should be after /
#        pass

			 

# Find outputs (Home work)
def f1(*a):
	print(a)                  #([10,20],{30,40},(50,60))
	print(type(a))            #<class 'tuple'>
	for x in a:
		print(x)            
		print(type(x))       
# End of the function
f1([10,20],{30,40},(50,60))    #[10,20] \n <class 'list'> \n {30,40} \n <class 'set'> \n (50,60) \n <class 'tuple'>




# Variable number of keyword arguments demo program
def disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End of the function
disp(RollNo=10,StudName='Rama Rao')                        #Results \n <class 'dict'> \n {'RollNo': 10, 'StudName': 'Rama Rao'}
disp(EmpNo=25,EmpName='Sita',Salary=10000.0)               #Results \n <class 'dict'> \n {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo=30,CustName='Kiran',Balance=20000.0,Gender='m')  #Results \n <class 'dict'> \n {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp()                                                     #Results \n <class 'dict'> \n {}
'''
<class 'dict'>
{'RollNo':10,'StudName':'Rama Rao'}
'''



# Find outputs (Home work)
def f1(**a):
	print('Results')                  
	for k,v in a.items():
		print(k,v,sep=' ... ')        
# End of the function
f1(Empno=25,Empname='Rama Rao',Salary=10000.0,Gender='m') #Results \n Empno...25 \n Empname...Rama Rao \n Salary...10000.0 \n Gender...m
f1()                                                      #Results \n



# Find outputs (Home work)
def f1(*a):
	print(type(a))
	print(a)
def f2(**a):
	print(type(a))
	print(a)
# End of the function
f1(25,10.8,'Hyd',True)                         #<class 'tuple'> \n (25,10.8,'Hyd',True)
print()                                        #\n
f2(EmpNum=25,EmpName='Sita',Salary=10000.0)    #<class 'dict'> \n { EmpNum : 25, EmpName : 'Sita', Salary : 10000.0 }
   



# Find outputs (Home work)
def f1(empno,ename,sal):
	print(F'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')
def f2(**a):
	print(a)
# End of the function
f1(empno=25,ename='Sita', sal=10000.0)        #Emp Number : 25 \t Emp Name : Sita \t Salary : 10000.0
# f1(eno=25,empname='Sita', salary=10000.0)   #type error, there is no arg name eno for f1
f2(empno=25,ename='Sita', sal=10000.0)        #{'empno' : 25, 'ename' : 'Sita', 'sal' : 10000.0}
f2(eno=25,empname='Sita', salary=10000.0)     #{'eno' : 25 , 'empname' : 'Sita', 'salary' : 10000.0}
   


# Find outputs (Home work)
def f1(a,*b,**c):
	print(a)
	if b:
		print(b)
	if c:
		print(c)
# End of the function
f1(25)                                                                 #25
print()                                                                #\n
f1('Hyd',10,20,30)                                                     #Hyd \n (10,20,30) 
print()                                                                #\n
f1(10.8,25,'Hyd',True,EmpNo=12,EmpName='Rama Rao',Salary=10000.0)      #10.8 \n (25, 'Hyd', True) \n {EmpNo : 12, EmpName : 'Rama Rao', Salary : 10000.0)}
   


'''
Write a program to evaluate expression like calculator

Let input be 3+4*5-6/2=
What is the output ? ---> 14.5

Hint: Use while loop

Iteration a op b result
------------------------------------------------------
1 3 + 4 7 ---> 'a'

2 7 * 5 35 ---> 'a'

3 35 - 6 29 ---> 'a'

4 29 / 2 14.5 ---> 'a'

5 14.5 = --- ----

Enter any expression terminated by = : 3+4*5-6/2=
Result : 14.5
'''



'''
Write a program to print roman equivalent of a number
1000 - M
900 - CM
500 - D
400 - CD
100 - C
90 - XC
50 - L
40 - XL
10 - X
9 - IX
5 - V
4 - IV
1 - I

1) What is the output if input is 3878 ? ---> MMMDCCCLXXVIII

2) What is the result of 3878 // 1000 ? ---> 3
How many M's are concatenated to the sting ? ---> Three becoz 3878 / 1000 is 3
What is the result of 3878 % 1000 ? ---> 878

3) What is the result of 878 // 900 ? ---> 0
How many CM's are concatenated to the string ? ---> Zero becoz 878 / 900 is 0
What is the result of 878 % 900 ? ---> 878

4) What is the result of 878 // 500 ? --->1
How many D's are concatenated to the string ? ---> One becoz 878 / 500 is 1
What is the result of 878 % 500 ? ---> 378
and so on
	 
Enter any number : 3878
Roman Equivalent : MMMDCCCLXXVIII
'''
d = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL', 10 : 'X', 9 : 'IX', 5 : 'V', 4 : 'IV', 1 : 'I'}
n = int(input('Enter any integer number:  '))
code = ''
for k in d:
    r = n // k
    code += (d[k] * r)
    n = n % k
print(f'Roman Equivalent : {code}')


'''
Write a program to print each digit of the number in words

Let input be 9247
What is the output ? ---> Nine Two Four Seven

a=['Zero','One','Two',....'Nine']

Iteration ch int(ch) a[int(ch)] s
--------------------------------------------------------
''
1 '9' 9 'Nine' ''+'Nine'+' '

2 '2' 2 'Two' 'Nine '+'Two'+' '

3 '4' 4 'Four' 'Nine Two '+'Four'+' '

4 '7' 7 'Seven' 'Nine Two Four '+'Seven'+' '
Enter any number : 9247
Nine Two Four Seven
'''


num_str = input('Enter the integer number')
d = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
ans = ''
for c in num_str:
    ans += d[int(c)] + ' '
print(ans)




'''
Write a program to print all the rotations of the string

1) Let input be S P A C E
0 1 2 3 4
What are the outputs ? ---> SPACE
PACES
ACESP
CESPA
ESPAC

2) What are the indexes of SPACE ? ---> 0 to 4
What are the indexes of PACES ? ---> 1 to 4,0 to 0
What are the indexes of ACESP ? ---> 2 to 4,0 to 1
What are the indexes of CESPA ? ---> 3 to 4,0 to 2
What are the indexes of ESPAC ? ---> 4 to 4,0 to 3

3) What are the indexes in general ? ---> i to length-1 and 0 to i-1
Enter any string : SPACE
Rotations
SPACE
PACES
ACESP
CESPA
ESPAC
'''

s = input('Enter any string:  ')
for i in range(len(s)):
    print(s[i:] + s[:i])



'''
Write a program to print mathematical table of a number

Let input be 7,
What is the output ? ---> 7*1=7
7*2=14
7*3=21
.....
7*10=70
Enter table number : 7
7*1=7
7*2=14
7*3=21
7*4=28
7*5=35
7*6=42
7*7=49
7*8=56
7*9=63
7*10=70
'''

n = int(input('Enter any number:  '))
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')


'''
Write a program to print following pyramid
Input: 5

    A
   A B
  A B C
 A B C D
A B C D E


i ch
---------------------
1 'A'

2 'A' to 'B'

3 'A' to 'C'

4 'A' to 'D'

5 'A' to 'E'
How many lines ? : 7
       A
      A B
     A B C
    A B C D
   A B C D E
  A B C D E F
 A B C D E F G
'''

n = int(input('Enter any integer number:  '))
for row in range(1, n+1):
    for i in range(n-row):
        print(' ', end='') 
    for i in range(1, row+1):
        print(chr(i+64), end=' ')
    print()



#Find outputs (Home work)
a=10
def f1():
	b=40
	print('a : ',a)
	print('b : ',b)
	print('c : ',c)
	print()
# End of f1() function
b=20
def f2():
	a=50
	print('a : ',a)
	print('b : ',b)
	print('c : ',c)
# End of f2() function
c=30
print('a : ',a)          #a : 10
print('b : ',b)          #b : 20
print('c : ',c)          #c : 30
print()                  #\n
a+=1                     #modifies global a = 11
b+=1                     #modifies global b = 21
c+=1                     #modifies global c = 31
f1()                     #a : 11 \n b : 40 \n c = 31
a+=1                     #modifies global a = 12
b+=1                     #modifies global b = 22
c+=1                     #modifies global c = 32
f2()                     #a : 50 \n b : 22 \n c : 32
print('Bye')             #Bye


# Find outputs (Home work)
def f1():
	a=20
	print(a)
	a+=1
#End of the function
a=10                    
print(a)                  #10
a+=1                      #modifies global a = 11
f1()                      #20 and modifies local a = 21
print(a)                  #11
