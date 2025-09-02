#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):                   
	return  a + b * c
#end  of  the  function  
print(f1(3 , 4 , 5))                            #23
print(f1(*[6 , 7 , 8]))                         #62
print(f1([6 , 7 , 8]))                          #error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))             #16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6}))     #14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))       #error
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}})       #{'c': 2, 'b': 4, 'a': 6}
print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6}))      #error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))               #error keyword argument should be after positional argument
print(sorted(a , rev = True))                   #error  rev is not a valid keyword argument
print(25 , 10.8 , 'Hyd' , separator = '\t')     #error  separator is not a valid keyword argument
print(25 , 10.8 , 'Hyd' , endofline = '\t')     #error  endofline is not a valid keyword argument
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') #error  keyword argument should be after positional argument



# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)     #a  :  10    b :  20
f1(b = 30 , a = 40)     #a  :  40    b :  30
f1(50 , 60)             #error  positional argument passed to keyword only argument
f1(70 , b = 80)         #error  positional argument passed to keyword only argument
f1(a = 15 , 25)         #error  positional argument passed to keyword only argument



#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)                #a  :  10    b :  20    c  :  30
f1(a = 40 , b = 50 , c = 60)            #a  :  40    b :  50    c  :  60
f1(c = 100 , b = 90 , a = 80)           #a  :  80    b :  90    c  :  100
f1(70 , 80 , c = 90)                    #error  positional argument passed to keyword only argument
f1(70 , 80 , 90)                        #error  positional argument passed to keyword only argument     
f1(c = 15 , b = 25 , 35)                #error  positional argument passed to keyword only argument



# Identify error (Home  work)
def   f1(a  , b , *):
        pass                            #error because atleast one named argument is required after *



#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)                     #a  :  10    b  :  20
f1(a = 30 ,  b = 40)            #error  keyword argument passed to positional only argument
f1(50 , b = 60)                 #error  keyword argument passed to positional only argument
f1(a = 70 , 80)                 #error  keyword argument passed to positional only argument


# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)                #a  :  10    b :  20    c  :  30
f1(40 , 50 , c = 60)            #a  :  40    b :  50    c  :  60
f1(a = 70 , b = 80 , c = 90)    #error  keyword argument passed to positional only argument
f1(a = 100 , b = 110 , 120)     #error  keyword argument passed to positional only argument
f1(a = 130 , 140 , c = 150)     #error  keyword argument passed to positional only argument
f1(160 , b = 170 , 180)         #error  keyword argument passed to positional only argument
f1(190 , b = 200 , c = 210)     #error  keyword argument passed to positional only argument



# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)         # a : 10      b : 20        c : 30     d : 40     e : 50
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)           #error
f1(1 , 2 , 3 , 4 , 5 , f = 6)                           #error
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)             #error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)     #a  :  10  	  b  :  20  	  c  :  30  	  d  :  40  	  e  :  50  	  f  :  60



# Identify error (Home  work)
def  f1(/ , a , b ,  c):                #at least one argument has to be before /
        pass
def   f2(a , b , c , *):                #keyword arguments has to follow bare *
        pass



# Identify  error  (Home  work)
def  f4(* , a , b , c , /):             # / must be ahead of *
	        pass


# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)              #3rd  function :10
f1(y = 20)              #error
f1(x = 30)              #error



# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))                                 #150
print(add(100 , 200))                           #330
print(add(100 , 200 , 300))                     #600
print(add(100 , c = 200))                       #320
print(add(c = 100 , b = 200 , a = 300))         #600
print(add(c = 100 , a = 200))                   #320
print(add())                                    #
print(add(a = 100 , 200))                       #error
print(add(100 ,  , 300))                        #error
print(add(100 ,  b , 300))                      #errror



# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):
	pass                                    #default argument has to be after positional arguments
def   f2(b , d , a = 10 , c = 20):
	pass                                    #no error



#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)                                          #20
f1()                                            #10
f1(a = 30)                                      #30



# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function

print(add(100 , 200))                      # 330
print(add(100 , 200 , 300))                # 620
print(add(100 , 200 , 300 , 400))          # 1000
print(add(b = 100 , a = 200))              # 330
print(add(100 , 200 , d = 300))            # 610
print(add(d = 100 , a = 200 , b = 300))    # 610
print(add(c = 100 , d = 200 , 300 , 400))  # Error : positional argument follows keyword argument
print(add(100 , 200 , c = 300 , x = 400))  # Error : unexpected keyword argument 'x'
print(add())                               # Error : missing 2 required positional arguments: 'a' and 'b'



#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))           #10
print(f1())             #25
print(f2(20))           #20
print(f2())             #error



 # Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function

disp('-' , 6)               # ------
disp('$')                   # $$$$
disp()                      # ****
disp(n = 5)                 # *****
disp(5)                     # 5555
disp(n = 7 , ch = '%')      # %%%%%%%
disp(7 , '@')               # @@@@@@@    (because ch=7, n='@' → TypeError)
disp(7 , n = 6)             # Error : multiple values for argument 'n'
disp(ch = '!' ,  5)         # Error : positional argument follows keyword argument




# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))
print(power(5))
print(power(b = 3 , a = 4.5))
print(power(3 + 4j))
print(power(True))
def   power(b = 2 , a):
 	 pass

# Outputs:
'''
64
25
91.125
(-7+24j)
1
errror
'''

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
print(add(10 , 20 , 30 , 40))           #100  (4-argument functions)
print(add(50 , 60 , 70))                #184   (4-argument functions)
print(add(80 , 90))                     #177   (4-argument functions)
print(add(100))                         #109    (4-argument functions)
print(add())                            #10     (4-argument functions)



# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)              #3-argument  function  :   10 20 30
disp(40 , 50 , 60 , 70)         #error
disp(80 , 90)                   #3-argument  function  :   80 90 25



# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))             #70
print(add())                            #30
print(add(a = 50))                      #70
print(add(b = 60 , a = 70))             #130
print(add(80 , 90))                     #error



# Find  outputs(Home  work)
def   add(a = 10 , b , c):                     #default parameters has to come after positional arguments
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))            #120
print(add(b = 60 , c = 70))                     #140
print(add(c = 80 , b = 90 , a = 100))           #170
print(add(c = 25 , a = 43))                     #error
print(add(1 , 2 , 3))                           #error
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass