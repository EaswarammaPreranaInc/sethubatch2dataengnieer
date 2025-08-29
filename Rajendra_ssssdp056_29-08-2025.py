
'''
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing
Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite
What  are  the  outputs  if  input  is  10  ?  --->     Prime   numbers
							2
							3
			      			        5
						        7
						        Number  of   prime  numbers : 4
'''

def checkprime(num):
    for i in range(2, num//2 + 1):
        if num%i == 0:
            return False
    return True        
    
ip = int(input('Enter a number : '))
if ip <= 2:
    print('Invalid input')
else:
    cnt = 0
    print(f'Prime numbers between 2 and {ip} :')
    for i in range(2, ip+1):
        if checkprime(i):
            cnt += 1
            print(i)
    print('Number of prime numbers : ', cnt)





# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a : {a}\tb : {b}\tc : {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)            #a : 10    b : 20    c : 30
f1(25 , 10.8 , 'Hyd')                   #a : 25    b : 10.8    c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)      #a : 50.2    b : 40.7    c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')   #a : Cyb    b : Sec    c : Hyd
f1(c = 3 + 4j , a = True , b = None)    #a : True    b : None    c : 3+4j
f1(25 , c = 10.8 , b = 'Hyd')           #a : 25    b : Hyd    c : 10.8
f1(a = 100 , 200 , 300)  #  Error
f1(True , None , b = 'Hyd')             #Throws error as None would initially get assigned to b, but we are again providing another avlue for b
f1(10 , 20 , x = 30)                    #Throws error as there is no x in formal arguments
f1(10 , 20)                             #Throws error as f1 needs 3 arguments but we only passed 2





# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)				#Emp Number :   25  	  Emp  Name :        Rama Rao  	  Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)	#Emp Number :   35  	  Emp  Name :            Sita  	  Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)						#Emp  Number : Rama Rao  	  Emp  Name : 30000.0          	  Salary : 20





#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))                            #23
print(f1(*[6 , 7 , 8]))                         #62
print(f1([6 , 7 , 8]))                          #Throws error as function expects 3 seperate values but only one list is being passed
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))             #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))     #14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))       #Throws error as function expects 3 seperate values but only one dictionary is being passed
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})       #{'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))      #This throws error as x isn't one of the formal parameters





# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))                         #Throws error as positional arguments can't follow keyword arguments 
print(sorted(a , rev = True))                             #Throws error as the keword name is reverse not rev
print(25 , 10.8 , 'Hyd' , separator = '\t')               #Throws error as the keyword name is sep not separator
print(25 , 10.8 , 'Hyd' , endofline = '\t')               #Throws error as the keyword name is end not endofline
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')       #Throws error as positional arguments can't follow keyword arguments 





# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)         #a  :  10     b :  20
f1(b = 30 , a = 40)         #a  :  40     b :  30
f1(50 , 60)                 #Throws error as f1 only expects only keyword arguments due to usage of * at the beginning
f1(70 , b = 80)             #Throws error as f1 only expects only keyword arguments due to usage of * at the beginning
f1(a = 15 , 25)             #Throws error as f1 only expects only keyword arguments due to usage of * at the beginning





#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)            #a  :  10     b :  20     c  :  30 
f1(a = 40 , b = 50 , c = 60)        #a  :  40     b :  50     c  :  60 
f1(c = 100 , b = 90 , a = 80)       #a  :  80     b :  90     c  :  100 
f1(70 , 80 , c = 90)                #Throws error as the 2nd argument must be a keyword argument
f1(70 , 80 , 90)                    #Throws error as f1 can accept only one positional argument
f1(c = 15 , b = 25 , 35)            #Throws error as positional arguments can't follow keyword arguments





# Identify error (Home  work)
def   f1(a  , b , *):          #* is used so that the arguments before it are keyworded. So * must be followed by atleast one formal parameter 
        pass





#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)                     #a  :  10     b  :  20
f1(a = 30 ,  b = 40)            #Throws error as arguments before / are ought to be positional not keyword
f1(50 , b = 60)                 #Throws error as arguments before / are ought to be positional not keyword
f1(a = 70 , 80)                 #Throws error as positional arguments can't follow keyword argument





# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)                #a  :  10     b :  20      c  :  30
f1(40 , 50 , c = 60)            #a  :  40     b :  50      c  :  60
f1(a = 70 , b = 80 , c = 90)    #Throws error as a and b can accept only positional arguments not keyword
f1(a = 100 , b = 110 , 120)     #Throws error as a and b can't be keyword arguments also a positional argument can't follow a keyword argument
f1(a = 130 , 140 , c = 150)     #Throws error as a can't be keyword arguments also a positional argument can't follow a keyword argument
f1(160 , b = 170 , 180)         #Throws error as b can't be a keyword argument also a positional argument can't follow a keyword argument
f1(190 , b = 200 , c = 210)     #Throws error as b can't be a keyword argument





# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)       #a  :  10     b  :  20      c  :  30      d  :  40     e  :  50     f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)     #Throws error as b can't be a keyword argument
f1(1 , 2 , 3 , 4 , 5 , f = 6)                     #Throws error as e must be keyword not positional argument
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)       #Throws error as a positional argument can't follow keyword argument
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)           #a  :  10     b  :  20      c  :  30      d  :  40     e  :  50     f  :  60





# Identify error (Home  work)
def  f1(/ , a , b ,  c):        #There must be atleast one formal argument before /
        pass
def   f2(a , b , c , *):        #There must be atleast one formal argument after *
        pass





# Identify  error  (Home  work)
def  f4(* , a , b , c , /):       #This creates a contradiction as a, b and c must be keyword arguments due to their presence after *. 
	pass			  #But due to their presence before / they must only accept positional arguments. So this causes error





# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)          #3rd  function :  10
f1(y = 20)          #Throws error as the last function f1 overwrites the previous two f1 functions and it expects z in case of keyword argument
f1(x = 30)          #Same error as above





# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))                     #150     
print(add(100 , 200))               #330
print(add(100 , 200 , 300))         #600
print(add(100 , c = 200))           #320
print(add(c=100, b=200, a=300))     #600
print(add(c = 100 , a = 200))       #320
print(add())                        #Throws error as add() expects atleast one argument
print(add(a = 100 , 200))           #Throws error as positional argument can't follow keyword argument
print(add(100 ,  , 300))            #Throws error as the syntax is invalid
print(add(100 ,  b , 300))          #Throws error as 2nd argument must be a value.





# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):       #A parameter without any default value can't follow one with default
	pass
def   f2(b , d , a = 10 , c = 20):
	pass





#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)              #20
f1()                #10
f1(a = 30)          #30





# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))                   #330   
print(add(100 , 200 , 300))             #620
print(add(100 , 200 , 300 , 400))       #1000
print(add(b = 100 , a = 200))           #330
print(add(100 , 200 , d = 300))         #610
print(add(d=100, a=200, b=300))         #610
print(add(c=100, d=200, 300, 400))      #Throws error as positional arguments can't follow keyword arguments
print(add(100, 200, c=300, x=400))      #Throws error as x is not one among formal arguments
print(add())                            #Throws error as add() expects atleast 2 arguments





#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))               #10
print(f1())                 #25
print(f2(20))               #20
print(f2())                 #Throws error as f2() expects one argument





# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)                       #------
disp('$')                           #$$$$
disp()                              #****
disp(n = 5)                         #*****
disp(5)                             #20
disp(n = 7 , ch = '%')              #%%%%%%
disp(7 , '@')                       #@@@@@@@
disp(7 , n = 6)                     #42
disp(ch = '!' ,  5)                 #Throws error as positional argument can't follow a keyword argument





# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))                 #64
print(power(5))                     #25
print(power(b = 3, a = 4.5))        #91.125
print(power(3 + 4j))                #-7+24j
print(power(True))                  #1
def   power(b = 2 , a):             #Invalid as a default parameter can't be before a non default parameter
 	 pass





# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40))       #4-argument  function<next line>100
print(add(50 , 60 , 70))            #4-argument  function<next line>184
print(add(80 , 90))                 #4-argument  function<next line>177
print(add(100))                     #4-argument  function<next line>109
print(add())                        #4-argument  function<next line>10





# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)              #3-argument  function  :   10 20 30
disp(40 , 50 , 60 , 70)         #Throws error as disp() takes atmost 3 elements
disp(80 , 90)                   #3-argument  function  :   80 90 25





# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))         #70
print(add())                        #30
print(add(a = 50))                  #70
print(add(b = 60 , a = 70))         #130
print(add(80 , 90))                 #Throws error as add() expects keyword arguments not positional





# Find  outputs(Home  work)
def   add(a = 10 , b , c):                      #Throws error as non default parameters can't follow default parameters
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))            #120
print(add(b = 60 , c = 70))                     #140
print(add(c = 80 , b = 90 , a = 100))           #270
print(add(c = 25 , a = 43))                     #Throws error as keyword argument for b is missing
print(add(1 , 2 , 3))                           #add() expects keyword arguments only not positional
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):  #Throws error as positional argument c can't follow keyword argument b
		pass
