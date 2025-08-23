# eval()  function  demo  program
print(eval('25')) # converts string to int 25
print(eval('10.8'))# converts string to 10.8
print(eval('False'))# converts string to bool False
print(eval('3+4j'))# converts string to comples 3 + 4j
print(eval('Hyd'))# Error converts string to object Hyd as there no object HYd
print(eval("    'Hyd'   ")) # 'Hyd'
print(eval('3 + 4 * 5')) # 24
print(eval('[10 , 20 , 15 , 18]'))# converts string to list [10 , 20 ,15 , 18]
print(eval('{10,20,15,18,20,12,18}'))# converts string to set {10 , 20 , 15 , 18 , 12} can be any orderr
print(eval('(10 , 20 , 30)'))# converts string to  tuple (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))# converts string to  dict {10 : 'Sec'}
print(eval(4 + 5)) # error 

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # string 25
print(eval(sec)) # int 25
cyb = 10.8
print(eval('cyb')) # float 10.8
print(eval(cyb)) # error as eval(10.8) throws error

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # print(eval('print("Hyd")')) ---> print(print('Hyd')) ---> Hyd <next line> None

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # bool False
print(bool('')) # False
print(eval('  ""  ')) # ""
print(eval('')) # error
print(eval('  " "   ')) # " "
print(eval(' ')) # error


# What  is  the  advantage  of  eval(input()) ? ---> coverts the user input to proper object
x = eval(input('Enter  any  input  :  ')) # (assume) 25
print(type(x)) # <class 'int'>
print(x) # 25


# What  is  a  better  approach  to  read  string  input ? ---> input()
a = input('Enter  any  string  :  ') # (assume) bhuvan
print(len(a)) # 6
print(a) #  bhuvan
b = eval(input('Enter   any  string  : ')) # (assume) bhuvan
print(len(b)) # error as there is no object bhuvan
print(b) # error as there is no object bhuvan


# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25 <tab> 10.8 <tab> Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25 <nextline> 10.8 <nextline> Hyd
print(a , b , c) # 25 <space> 10.8 <space> Hyd
print(a , b , c , separator = ':') # error as there is no separator

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)

'''
25 <space> 10.8 <space> Hyd--- 25,,,10.8,,,Hyd
25:10.8:Hyd<tab><tab><tab>25 <space> 10.8 <space> Hyd
'''

# Find outputs  (Home  work)
print('Hyd')
print()
print('Sec')
print()
print('Cyb')

'''
Hyd

Sec

Cyb
'''



# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10 , 20 , 30 , 40] <space> (10 , 20 , 30 , 40) <space> {10 , 20 , 30 , 40}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # string 25.000000
print(type(b)) # <class 'str' >
x = 10.8 
y = '%d'  %x
print(y) # string 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # string [10 , 20 , 15 , 18]
print(type(n)) # <class 'str'>



# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <5spaces>10.9
print('%10.3f'  %a) # <4spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.924700
print('%f'  %a) # 10.924700



# Find  outputs (Home  work)

a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a)  # Hyd
print('%s' , a) # %s <space> Hyd
print('%s'  a) # error as there is no % or comma
print('%s' , %a) # error as there is comma
print(a) # Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # string [10 , 20 , 30 , 40]
print('%s' , a) # %s <space> [10 , 20 , 30 , 40]
print('%s'  a) # error as there is no % or comma
print('%s' , %a) # error as there is no  comma
print('%l'  %a) # error as there is no format %l
print(a) # [10 , 20 , 30 , 40]



#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25 <space> 10.924700 <space> Hyd
print('%i    %g    %s'    %(a , b , c)) # 25 <space> 10.9247 <space> Hyd
print('%s    %s    %s'  %(a , b , c))  # 25 <space> 10.924700 <space> Hyd
print('%d    %g    %s'  , a , b , c)  # %d <space> %g <space> %s <space> 25 <space> 10.924700 <space> Hyd
print('%d    %g      %s'   a , b , c) # error as there is no comma or %
print('%d    %g    %s'  ,  %(a , b , c)) # error as there is comma
print('%d    %g    %s'    %a%b%c) # error 
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)

