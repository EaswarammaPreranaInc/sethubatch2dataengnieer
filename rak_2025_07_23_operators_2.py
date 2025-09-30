#  ++  and  --  operators  demo  program
a = 25
print(++a)  #+(+a) => +a => 25, + is unary operator evaluates from right to left
#print(a++) #SyntaxError: name, operator, operator has no meaning in python
print(a++1) #a+(+1) => 26, unary + evaluated first
print(--a)  #-(-a) => 25, unary - is evaluated first
#print(a--)  #SyntaxError: name, operator, operator has no meaning in python
print(a--1) #a-(-1) = 26, unary - is evaluated first
print(-a)   #-25, unary operator
print(+-a)  #+(-25) = -25, unary - is evaluated first
print(-+a)  #-(+25) = -25, unary + is evaluated first


#  Semicolon  demo  program
print('One');                                  #print 'One' and move next line
print('Two');                                  #print 'Two' and move next line
print('Three');                                #print 'Three' and move next line
print('Hyd')  ;   print('Sec') ; print('Cyb')  #separates three print statements
#print('Hyd') print('Sec') print('Cyb')        #SyntaxError: Statements must be separated by newlines or semicolons



#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #Nearest  Prev  integer  10
print(math . ceil(10.8))   #Nearest  next  integer  11
print(math . floor(25.0))  #25 
print(math . ceil(25.0))   #25 
print(math . floor(-3.5))  #Prev   integer  -4
print(math . ceil(-3.5))   #Next  integer  -3
print(math . floor(-9.0))  #-9  
print(math . ceil(-9))     #-9 
print(math . floor(25.1))  #25
print(math . ceil(25.1))   #26
#print(math.ceil(4+7j))    #TypeError, must be real number not complex
#print(floor(3.5))         #NameError: name 'floor' is not defined, No  floor()  in current  module
#print(ceil(3.5))          #NameError: name 'ceil' is not defined, No  ceil()  in current  module
#floor and ceil returns only int


# gcd()  function  demo  program
import  math                   
print(math . gcd(12 , 15))     #3, 15%12=3, 12%3=0,3%0 ans is 3
print(math . gcd(12 , 18))     #6, 18%12=6, 12%6=0,6%0 ans is 6
print(math . gcd(4 , 7))       #1, 7%4=3, 4%3=1, 3%1=0,1%0 ans is 1
print(math . gcd(7 , 7))       #7, 7%7=0, 7%0, ans 7
print(math . gcd(-18 , -27))   #9, 27%18=9, 18%9=0, 9%0 ans is 9
print(math . gcd(-4 , 6))      #2, 6%4=2, 4%2=0, 2%0 ans is 2
print(math . gcd(0 , 7))       #7, gcd integer and 0 is integer
print(math . gcd(3 , 0))       #3, gcd between integer and 0 is integer
print(math . gcd(0 , 0))       #0, 
#print(gcd(5 , 15))            #NameError: gcd is not defined


# fabs()  function  demo   program
import  math
print(math . fabs(-10))   #10.0
print(math . fabs(-25.6)) #25.6
print(math . fabs(20))    #20.0
print(math . fabs(35.8))  #35.8
#print(fabs(-25))         #NameError: name 'fabs' is not defined, No  fabs()  function  in  current  module



#  max()  and  min()   functions  demo  program
from  builtins  import   max , min            #Optional : max() and min() functions are automatically imported from builtins module
print(max(10.8 , 20.6))                       #20.6, max of two
print(min(10.8 , 20.6 , 5.9 , 12.3))          #5.9, min of all
print(max(25 , 10.8))                         #25, max of two
import  builtins                              #Mandatory :  Not  imported  automatically
print(builtins . max(10 , 20 , 30))           #30, max of all
print(builtins . min(10 , 20 , 15 , 5 ,12))   #5, min of all
#print(max(3+4j, 5+5j))                       #TypeError: '>' not supported between instances of 'complex' and 'complex'


#pow()  function  demo  program
import  math
print(math . pow(2 , 3))                  #2 ^ 3 = 8.0
print(math . pow(-2 , -3))                #-2 ^ -3
print(math . pow(10 , -2))                #10 ^ -2 = 0.01
print(math . pow(4 , math . pow(3 , 2)))  #4 ^ 3 ^ 2 = 4 ^ 9
print(math.pow(2.3, 4))                   #27.98409999
#print(math.pow(2+4j, 2))                 #TypeError: must be real number, not complex
#print(math.pow('2', 2))                  #TypeError: must be real number, not str



# Find  outputs
#How  to  import   kw  list
from keyword import kwlist
#How  to  print  kwlist
print(kwlist)                           #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
                                        #'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
                                        #  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
                                        # 'return', 'try', 'while', 'with', 'yield']
#How  to  print  number  of  keywords
print(len(kwlist))                      #35    
#How  to  print  type  of kwlist
print(type(kwlist))                     #<class 'list'>
#print(keyword . kwlist)                #NameError: keyword module is not imported, only list is imported




#  Find  outputs  (Home  work)
#How  to  import   keyword  module
import keyword
#How  to  print  kwlist
print(keyword.kwlist)                   #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
                                        #'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
                                        #  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
                                        # 'return', 'try', 'while', 'with', 'yield']
#How  to  print  number  of  keywords
print(len(keyword.kwlist))              #35
#How  to  print  type  of kwlist
print(type(keyword.kwlist))             #<class 'list'>
#print(kwlist)                          #NameError: only module keyword in imported not memebers

