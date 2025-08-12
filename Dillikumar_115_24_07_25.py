
# eval()  function  demo  program
print(eval('25'))            :  25
print(eval('10.8'))         : 10.8
print(eval('False'))         : false 
print(eval('3+4j'))         :  ( 3+4j ) #complex
print(eval('Hyd'))          :  Hyd    #String
print(eval("    'Hyd'   "))   : ‘error    # string
print(eval('3 + 4 * 5'))  : 23  # int
print(eval('[10 , 20 , 15 , 18]'))  : [10 , 20,15, 18]   : list 
print(eval('{10,20,15,18,20,12,18}'))   : {10,20,15,18,20,12,18}    # dict
print(eval('(10 , 20 , 30)'))  :   (10 , 20 , 30)           # tuple 
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) :  {10 : 'Sec'}
print(eval(4 + 5))    : error # int 
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))      : ‘hyd’
hyd = 'Sec'
print(eval('hyd'))  :  ‘sec’
sec = '25'     
print(eval('sec'))  : 25
print(eval(sec))   :  25
cyb = 10.8
print(eval('cyb'))  : 10.8
print(eval(cyb))   :  error 
#Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))  : “hyd”
#  Find  outputs  (Home  work)
print(bool('False'))   :  treue
print(eval('False'))  : false 
print(bool(''))    false
print(eval('  ""  '))  : “ “
print(eval(''))  : error 
print(eval('  " "   '))  :” “
print(eval(' '))  :error  
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))  : <class ‘eval’>
print(x)      :  nothing will be utill adding value to that x value 
# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')   : a=’kumar’
print(len(a)) : 5
print(a)  : ‘kumar’
b = eval(input('Enter   any  string  : '))  :  ‘kumar’
print(len(b))  : 5
print(b)  : ’kumar’
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')        : 25  10.8  'Hyd'  # with tab space 
print(a , b , c , sep = '---')         : 25---10.8---'Hyd'  
print(a , b , c , sep = '\n')   :
  25 
 10.8 
 'Hyd'  
print(a , b , c)  : error 
print(a , b , c , separator = ':')  : error # are not assigned type 
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  : 25  10.8  'Hyd'---
print(a , b , c , sep = ',,,')   : 25  10.8  'Hyd' ,,,

print(a , b , c , sep = ':::' , end = '\t\t\t')  
 25::: 10.8 ::: Hyd
print(a , b , c)  
#Find outputs  (Home  work)
print('Hyd')  : ’Hyd’
print() : empty , no ouput will be printed 
print('Sec') : ‘sec’
print()   : empty output 
print('Cyb')  : ‘Cyb’
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)  :
	[10 , 20 , 30 , 40],( 10 , 20 , 30 , 40),{ 10 , 20 , 30 , 40}
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)  :  25.0
print(type(b))   :   <class  ‘str’> 
x = 10.8
y = '%d'  %x
print(y) : 10
print(type(y)) : <class ‘int’>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)
print(type(n)) < class  ‘str’>
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  :     10.9 # 5 spacs
print('%10.3f'  %a):     10.927#4space
print('%.2f'  %a)     :10.92
print('%.6f'  %a)   : 10.927400
print('%f'  %a)   :   10.927400

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)   : Hyd
print('%s' , a) : hyd
print('%s'  a) :error 
print('%s' , %a)     : error 
print(a) 
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)  :  [10 , 20 , 30 , 40]
print('%s' , a)  : %s  [10 , 20 , 30 , 40]
print('%s'  a)  :  error
print('%s' , %a)  : error 
print('%l'  %a)  :  error 
print(a) : [10 , 20 , 30 , 40]
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))   :    25  10.927400   ‘Hyd’
print('%i    %g    %s'    %(a , b , c))  :   25  10.9274   ‘Hyd’

print('%s    %s    %s'  %(a , b , c)) : 25  10.9274   ‘Hyd’
print('%d    %g    %s'  , a , b , c)    : '%d    %g    %s'   25  10.9274   ‘Hyd’
print('%d    %g      %s'   a , b , c)   :  error
print('%d    %g    %s'  ,  %(a , b , c))  :error 
print('%d    %g    %s'    %a%b%c)       : error 
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)  	: 25  10.927400  s‘Hyd’  											
