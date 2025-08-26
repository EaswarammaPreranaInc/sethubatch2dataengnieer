# eval()  function  demo  program
print(eval('25'))  # 25
print(eval('10.8'))  # 10.8
print(eval('False'))    # False
print(eval('3+4j'))   # (3+4j)
print(eval('Hyd'))  #Error due to not defined
print(eval("    'Hyd'   "))   # Hyd
print(eval('3 + 4 * 5'))    #3 + (4*5) = 3+20 = 23
print(eval('[10 , 20 , 15 , 18]'))   # [10, 20, 30, 40]
print(eval('{10,20,15,18,20,12,18}'))    # {10,12,15,18,20}
print(eval('(10 , 20 , 30)'))   # (10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))   # {10 : ‘Sec”}
print(eval(4 + 5))   #Error due to args is not a string.



#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))   # ‘hyd’
hyd = 'Sec'
print(eval('hyd'))    # ‘Sec’
sec = '25'
print(eval('sec'))    # ‘25’
print(eval(sec))   # 25
cyb = 10.8
print(eval('cyb'))    # 10.8
print(eval(cyb))      # Error due to the eval except the str.


#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))    # frist to print Hyd and next step is eval is None i.e.     Hyd
None



#  Find  outputs  (Home  work)
print(bool('False'))    # True
print(eval('False'))    # False
print(bool(''))	# False
print(eval('  ""  '))   # Empty string
print(eval(''))    #Error due to Empty string
print(eval('  " "   '))    # To print a space
print(eval(' '))    # Error 



# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))   # ‘Jaya Krishna’
print(type(x))   # <class ‘str’>
print(x)  # Jaya Krishna







# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')   # Jaya
print(len(a))  #  4
print(a)    # Jaya
b = eval(input('Enter   any  string  : '))    # ‘Krishna’
print(len(b))   #7
print(b)    #Krishna

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  # 25  10.8   Hyd 
print(a , b , c , sep = '---')    # 25 --- 10.8 --- Hyd
print(a , b , c , sep = '\n')   #  25 <new line> 10.8 <new line> Hyd
print(a , b , c)  # 25  10.8  Hyd
print(a , b , c , separator = ':')    #Error 


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  # 25  10.8  Hyd ---
print(a , b , c , sep = ',,,')   # 25,,, 10.8,,, Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')   # 25:::10.8:::Hyd	25  10.8  Hyd
print(a , b , c)

# Find outputs  (Home  work)
print('Hyd')  # Hyd
print()  # empty string
print('Sec')    # Sec
print()    # empty string
print('Cyb')    #  Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)   # [10, 20, 30, 40] (10, 20, 30, 40 ) {10, 20, 30, 40 }


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)  # 25.000000
print(type(b))   # <class ‘str’>
x = 10.8
y = '%d'  %x
print(y)    # 10
print(type(y))   # <class ‘str’>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)   # [10, 20, 15, 18]
print(type(n))   # <class ‘str’>

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)  # <5 spaces> 10.9
print('%10.3f'  %a)   # <4 spaces> 10.927
print('%.2f'  %a)   # 10.93
print('%.6f'  %a)   # 10.927400
print('%f'  %a)  # 10.927400





# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)     # Hyd
print('%s' , a)    #%s <space> Hyd
#print('%s'  a)     #Error
#print('%s' , %a)   # Error
print(a)    # Hyd






# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)   # [10, 20, 30,40]
print('%s' , a)  #%s <space> [10,20,30,40]
#print('%s'  a)   # Error
#print('%s' , %a)   #Error
#print('%l'  %a)   # Error
print(a)     # [10, 20, 30, 40]



#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))   # 25  10.924700  Hyd
print('%i    %g    %s'    %(a , b , c))  # 25  10.9247  ‘Hyd’
print('%s    %s    %s'  %(a , b , c))  # ‘25’  ’10.9247’  Hyd
print('%d    %g    %s'  , a , b , c)   # 25  10.9247  ‘Hyd’
#print('%d    %g      %s'   a , b , c)   # Error 
#print('%d    %g    %s'  ,  %(a , b , c))  # Error
#print('%d    %g    %s'    %a%b%c)    # Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)   # 25  10.924700  Hyd

