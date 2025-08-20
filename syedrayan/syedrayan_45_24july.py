# eval()  function  demo  program
print(eval('25')) # int object 25
print(eval('10.8')) # float object 10.8
print(eval('False')) # bool object False
print(eval('3+4j')) # complex object (3+4j)
#print(eval('Hyd')) # Hyd
print(eval("    'Hyd'   ")) #    'Hyd'   
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) #[10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) #{10,20,15,18,20,12}
print(eval('(10 , 20 , 30)'))#(10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10:'Hyd',10:'Sec'}
#print(eval(4 + 5)) # error arg must be string

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
#print(eval(cyb)) # error arg must  be a string

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # first inner funtion print("Hyd") executes and prints Hyd and return None i.e.  eval('None') returns None print(None)

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # ""
#print(eval('')) # '' # error
print(eval('  " "   ')) # " "
#print(eval(' '))# error

# What  is  the  advantage  of  eval(input()) ?
#bool() gives true to every input except "" but eval() converts the string to corresponding class object 
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # rayan
print(len(a)) # 5
print(a) # rayan
b = eval(input('Enter   any  string  : ')) # "rayan"
print(len(b)) # 5
print(b)# rayan

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25  10.8    Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25 <nextline> 10.8 <nextline> Hyd
print(a , b , c) # 25 10.8 Hyd
#print(a , b , c , separator = ':') # seperator is not a keyword

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 Hyd---
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd <3tab spaces>
print(a , b , c)# 25 10.8 Hyd

# Find outputs  (Home  work)
print('Hyd') # Hyd
print() #<nextline>
print('Sec') # Sec
print() # <nextline>
print('Cyb')# Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # string float 25.000000
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x
print(y) # string int 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # str list [10,20,15,18]
print(type(n))# <class 'str'>

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <6 spaces>11.0
print('%10.3f'  %a) # <5 spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f' %a)# 10.927400

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)  # Hyd
print('%s' , a) # %s Hyd
#print('%s'  a) # error
#print('%s' , %a) # error
print(a)# Hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # [10,20,30,40]
print('%s' , a) # %s [10,20,30,40]
#print('%s'  a) # error
#print('%s' , %a) # error
#print('%l'  %a) # error
print(a)# [10,20,30,40]

#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c)) #  25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c)) # 25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c) # %d %g %s 25 10.9274 Hyd
# print('%d    %g      %s'   a , b , c) # error
#print('%d    %g    %s'  ,  %(a , b , c)) # error
#print('%d    %g    %s'    %a%b%c) # 25 10.9274 Hyd
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd