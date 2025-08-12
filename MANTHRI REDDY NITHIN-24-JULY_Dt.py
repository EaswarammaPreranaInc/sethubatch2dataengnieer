# eval()  function  demo  program
print(eval('25')) # 25
print(eval('10.8')) # 10.8
print(eval('False')) # False
print(eval('3+4j')) # 3+4j
print(eval('Hyd')) # Error
print(eval("    'Hyd'   ")) # Hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)')) # (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10 : 'Sec'}
print(eval(4 + 5)) # Error

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))
# Hyd
# None


#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # True
print(bool('')) # False
print(eval('  ""  ')) # 'blank'
print(eval('')) # Error
print(eval('  " "   ')) # 'blank'
print(eval(' ')) # Error


# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # eval converts 'String' object into appropriate class object
print(type(x)) # any type of class based of object x 
print(x) 


# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # This approach is best for read string input
print(len(a)) # length of string a
print(a)
b = eval(input('Enter   any  string  : ')) # In this approach we will input always given in a quotes
print(len(b))  # length of string b
print(b)

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25  10.8  Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25<New line>10.8<New line>Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # 25 : 10.8 : Hyd


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 'Hyd'---
print(a , b , c , sep = ',,,') # 25 ,,, 10.8 ,,, Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25 ::: 10.8 ::: Hyd      
print(a , b , c) # 25 10.8 'Hyd'


# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # blank or empty statement
print('Sec') # Sec
print() # blank or empty statement
print('Cyb') # Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40} 
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.0
print(type(b)) # < class float >
x = 10.8
y = '%d'  %x # 10
print(y) # 10
print(type(y)) # < class int >
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # '[10 , 20 , 15 , 18]'
print(type(n)) # < class str >

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # < 5 spaces >10.9
print('%10.3f'  %a) # < 4 spaces >10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)  # Hyd
print('%s' , a) # %s Hyd
print('%s'  a) # Error
print('%s' , %a) Error
print(a) # Hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # ' [10 , 20 , 30 , 40]'
print('%s' , a) # %s  [10 , 20 , 30 , 40]
print('%s'  a) # Error
print('%s' , %a) # Error
print('%l'  %a) # Error
print(a) #  [10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c)) # 25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c)) # 25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c) # %d %g %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c) # Error
print('%d    %g    %s'  ,  %(a , b , c)) # Error
print('%d    %g    %s'    %a%b%c) # Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd
