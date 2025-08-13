# eval()  function  demo  program

print(eval('25'))     # 25
print(eval('10.8'))  # 10.8
print(eval('False')) # False
print(eval('3+4j')) # 3+4j
print(eval('Hyd'))  #error
print(eval("    'Hyd'   ")) # hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # [10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) # {18, 20, 10, 12, 15}
print(eval('(10 , 20 , 30)'))			# (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10: 'Sec'}
print(eval(4 + 5)) #error
----------------------------------------------------
#  Tricky  program
# Find  outputs  (Home  work)

print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd'))  # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec))  # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # error
----------------------------------------
#  Tricky  program
#  Find  output  (Home  work)

print(eval('print("Hyd")')) # True
					None
--------------------------------------------
#  Find  outputs  (Home  work)

print(bool('False')) # True
print(eval('False'))  # False
print(bool(''))        # False
print(eval('  ""  '))  # empty
print(eval(''))        #  error
print(eval('  " "   ')) # empty
print(eval(' '))        #  error
----------------------------------------------
# What  is  the  advantage  of  eval(input()) ?

x = eval(input('Enter  any  input  :  ')) # 30
print(type(x)) #  <class 'str'>  
print(x) # 30
-------------------------------------------------
# What  is  a  better  approach  to  read  string  input ?

a = input('Enter  any  string  :  ') # 'Srisai'
print(len(a))  #  8
print(a)  #  'Srisai'
b = eval(input('Enter   any  string  : ')) # 'Srisai'
print(len(b)) # 6
print(b) #  Srisai
-------------------------------------------
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25	10.8	  Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25
					10.8
					Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # 25 : 10.8 : Hyd
------------------------------------------
# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # empty
print('Sec') # Sec
print() # empty
print('Cyb') # Cyb
-------------------------------
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  # 25 10.8 Hyd---
print(a , b , c , sep = ',,,')   # 25 ,,, 10.8 ,,, Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')  #  25:::10.8:::Hyd
print(a , b , c)                  # 25 <space>10.8<space> #  Hyd
---------------------------------------
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)     # [10, 20, 30, 40]   (10, 20, 30, 40)   {40, 10, 20, 30}
-----------------------------------
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x
print(y) # 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10,20,15,18]
print(type(n)) <class 'str'>
----------------------------------------
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)   # <5 spaces>10.9
print('%10.3f'  %a)  # <4 spaces>10.93
print('%.2f'  %a)    # <>10.93
print('%.6f'  %a)
print('%f'  %a)
----------------------------------
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)  # Hyd
print('%s' , a)  #  %s   Hyd
print('%s'  a)  # error
print('%s' , %a) # error
print(a) # Hyd
-------------------------------------------
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
print('%d    %g      %s'   a , b , c) # error
print('%d    %g    %s'  ,  %(a , b , c) )# error
print('%d    %g    %s'    %a%b%c) # error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)

 Outputs :-

25    10.927400    Hyd
25    10.9274    Hyd
25    10.9274    Hyd
%d    %g    %s 25 10.9274 Hyd
25 10.927400 Hyd

























































































