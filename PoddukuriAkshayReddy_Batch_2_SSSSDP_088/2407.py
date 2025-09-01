24/07

# eval()  function  demo  program
print(eval('25')) # 25
print(eval('10.8')) # 10.8
print(eval('False')) # True
print(eval('3+4j')) # 3+4j
print(eval('Hyd')) # Error
print(eval("    'Hyd'   ")) # Hyd
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # [10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) # {10,20,15,18,12} in any order
print(eval('(10 , 20 , 30)')) # (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10:'Hyd'}
print(eval(4 + 5)) 


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # Hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error


#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd


#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool(''))  # False
print(eval('  ""  ')) # empty
print(eval('')) #   # Error
print(eval('  " "   ')) # Empty 
print(eval(' '))    # Error


# What  is  the  advantage  of  eval(input()) ?  # convert string into object
x = eval(input('Enter  any  input  :  '))
print(type(x)) # object
print(x)   # object


# What  is  a  better  approach  to  read  string  input ?  first approach
a = input('Enter  any  string  :  ')
print(len(a)) 
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)


# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  # 25	10.8	Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25
10.8
Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # Error due to separator


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd:::			25 10.8 Hyd
print(a , b , c)

# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # Empty
print('Sec') # Sec
print() # Empty
print('Cyb') # cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.0000
print(type(b)) # <class 'str'>
x = 10.8
y = '%d'  %x
print(y) # 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10,20,15,18]
print(type(n)) # <class 'str'>

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  # <5 spaces>10.9
print('%10.3f'  %a) # <4spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)  # Hyd
print('%s' , a)  # %s Hyd
print('%s'  a)  #Error
print('%s' , %a) # Error
print(a) # Hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40] 
print('%s'  %a) # [10, 20, 30, 40]
print('%s' , a) # %s [10, 20, 30, 40]
print('%s'  a) # Error comma or % any one of them is required
print('%s' , %a) # Error comma or % both are not allowed
print('%l'  %a)  # %l is not valid
print(a)  # [10, 20, 30, 40]

#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))  # 25    10.927400    Hyd
print('%i    %g    %s'    %(a , b , c)) # 25    10.9274    Hyd
print('%s    %s    %s'  %(a , b , c))  # 25    10.9274    Hyd
print('%d    %g    %s'  , a , b , c) # %d    %g    %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c)  # Error
print('%d    %g    %s'  ,  %(a , b , c)) # Error
print('%d    %g    %s'    %a%b%c) # Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.9274 Hyd