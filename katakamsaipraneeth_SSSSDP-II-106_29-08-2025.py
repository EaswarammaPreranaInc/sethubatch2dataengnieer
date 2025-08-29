# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1() # call f1 function
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(x) # call f1 function
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(x , y) # call f1 function
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(x , y , z) # call f1 function with 3 positional arguments

'''
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		  Number  of   prime  numbers : 4
'''
############ program ###############
def prime(s):
    p = []
    for i in range(2, s + 1):
        c = 0
        for j in range(2, i):   
            if i % j == 0:
                c+=1           
        if c == 0:
            p.append(i)
    return p                 

a = int(input("Enter a number: ")) # How  to  read  a  number
x = prime(a)
print('Prime numbers:')
for num in x: # How  to  print  all  prime  numbers  between  2  and  user  input
    print(num)
print('Number of prime numbers:', len(x)) # print('Number  of  prime numbers  :  ' ,  ???)



# Find  outputs  (Home  work)
def    f1(a , b , c): # function header with positional arguments
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}') # prints and returns none
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # call function with keyword argm a  :  10    \t  b  :  20  \t  c :  30
f1(25 , 10.8 , 'Hyd') # a  :  25    \t  b  :  10.8  \t  c :  'Hyd'
f1(b = 40.7 , a = 50.2 , c = 60.5) # function call with keyword arguments -- a  :  50.2    \t  b  :  40.7  \t  c :  60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a  :  'Cyb'    \t  b  :  'Sec'  \t  c :  'Hyd'
f1(c = 3 + 4j , a = True , b = None) # a  :  True    \t  b  :  None  \t  c :  3 + 4j
f1(25 , c = 10.8 , b = 'Hyd') # a  :  25    \t  b  :  'Hyd'  \t  c :  10.8
f1(a = 100 , 200 , 300)  #  Error
f1(True , None , b = 'Hyd') # error
f1(10 , 20 , x = 30) # error
f1(10 , 20) # error


# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)


#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c): # function header
	return  a + b * c # return output
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62
print(f1([6 , 7 , 8])) # error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # error
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # error
print({{'c' : 2 , 'b' :  4 , 'a' : 6}}) # error
print(f1({'c' : 2 , 'a' : 4 , 'x' : 6})) # error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12] # list obj
print(sorted(reverse = True , a)) # error
print(sorted(a , rev = True)) # error
print(25 , 10.8 , 'Hyd' , separator = '\t') # error 
print(25 , 10.8 , 'Hyd' , endofline = '\t') # error
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') # error


# Keyword  only   arguments  demo  program
def   f1(* , a , b): # function header with * 
        print(F'a  :  {a}  \t  b :  {b}') # prints this line when fun called
# End  of  the  function
f1(a = 10 , b = 20) # a  :  10  \t  b :  20
f1(b = 30 , a = 40) # a  :  40  \t  b :  30
f1(50 , 60) # error
f1(70 , b = 80) # error
f1(a = 15 , 25) # error


#Find  outputs (Home  work)
def  f1(a , * , b , c): # function header
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ') # print stat
# End  of  function
f1(10 , b = 20 , c = 30) # a  :  10  \t  b :  20  \t  c  :  30 
f1(a = 40 , b = 50 , c = 60) # a  :  40  \t  b :  50  \t  c  :  60 
f1(c = 100 , b = 90 , a = 80) # a  :  80  \t  b :  90  \t  c  :  100 
f1(70 , 80 , c = 90) # error
f1(70 , 80 , 90) error
f1(c = 15 , b = 25 , 35) # a  :  35  \t  b :  25  \t  c  :  15 

# Identify error (Home  work)
def   f1(a  , b , *): # error because before * there are arguments 
        pass


#  Positional  only  arguments  demo  program
def   f1(a , b , /): # / is used for only positional arg
        print(F'a  :  {a}  \t  b  :  {b}') # print stat
# End  of   the  function
f1(10 , 20) # a  :  10  \t  b  :  20
f1(a = 30 ,  b = 40) # error
f1(50 , b = 60) # error
f1(a = 70 , 80) # error


# Find  outputs (Home  work)
def  f1(a , b , / , c): # function header
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a  :  10  \t  b :  20  \t  c  :  30 
f1(40 , 50 , c = 60) # a  :  40  \t  b :  50  \t  c  :  60 
f1(a = 70 , b = 80 , c = 90) # error
f1(a = 100 , b = 110 , 120) # error
f1(a = 130 , 140 , c = 150) # error
f1(160 , b = 170 , 180) # error
f1(190 , b = 200 , c = 210) # error


# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f): # function header
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a:10  \t  b:20   \t  c:30  \t  d:40  \t  e:50 \t  f:60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # error
f1(1 , 2 , 3 , 4 , 5 , f = 6) # error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # a:10  \t  b:20   \t  c:30  \t  d:40  \t  e:50 \t  f:60
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a:10  \t  b:20   \t  c:30  \t  d:40  \t  e:50 \t  f:60


# Identify error (Home  work)
def  f1(/ , a , b ,  c): # fun header error because no arg before /
        pass
def   f2(a , b , c , *): # error because no arg after *
        pass

# Identify  error  (Home  work)
def  f4(* , a , b , c , /): # error because of * and /
	        pass

# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd  function :  10
f1(y = 20) # error
f1(x = 30) # error


# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30): # fun header
        return   a + b + c 
#end  of  the  functiom
print(add(100))                        # 150
print(add(100 , 200))                  # 330
print(add(100 , 200 , 300))	       # 600
print(add(100 , c = 200))              # 320
print(add(c = 100 , b = 200 , a = 300))# 600
print(add(c = 100 , a = 200))          # 320
print(add())                           # error
print(add(a = 100 , 200))              # error
print(add(100 ,  , 300))               # error
print(add(100 ,  b , 300))             # error

# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): # error
	pass
def   f2(b , d , a = 10 , c = 20): # error no positional arg
	pass

#  Find  outputs (Home  work)
def   f1(a = 10): # func header
        print(a)
# End  of  the  function
f1(20) # 20
f1() # error
f1(a = 30) # 30


# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20): # fun header
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) # 610
print(add(c = 100 , d = 200 , 300 , 400)) # error
print(add(100 , 200 , c = 300 , x = 400)) # error
print(add()) # error


#  Find  outputs (Home  work)
def    f1(x = 25): # fun header
        return  x
def   f2(x): # f2 header
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1()) # 25
print(f2(20)) # 20
print(f2()) # error


# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # *****
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
disp(ch = '!' ,  5) # error


# Find  outputs (Home  work)
def  power(a , b  =  2): # fun header
        return  a ** b
#end of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
def   power(b = 2 , a): 
 	 pass


# Find outputs  (Home  work)
def   add(a , b): # fun header
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
print(add(10 , 20 , 30 , 40)) # 4-argument  function
				# 100
print(add(50 , 60 , 70)) # error
print(add(80 , 90)) # error
print(add(100)) # error
print(add()) # error


# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :  10 20 30
disp(40 , 50 , 60 , 70) # error
disp(80 , 90) # error


# Find outputs(Home  work)
def   add(* , a = 10 , b = 20): # 
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50)) # 70
print(add(b = 60 , a = 70)) # 130
print(add(80 , 90)) # error


# Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # 120
print(add(b = 60 , c = 70)) # 140
print(add(c = 80 , b = 90 , a = 100)) # 270
print(add(c = 25 , a = 43)) # 68
print(add(1 , 2 , 3)) # error
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): # error
		pass