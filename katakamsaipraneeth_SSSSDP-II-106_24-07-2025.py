# eval()  function  demo  program
print(eval('25')) # 25
print(eval('10.8')) # 10.8
print(eval('False')) # False
print(eval('3+4j')) # (3+4j)
print(eval('Hyd')) # Hyd
print(eval("    'Hyd'   ")) #'Hyd'
print(eval('3 + 4 * 5')) # 23
print(eval('[10 , 20 , 15 , 18]')) # [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}')) # {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)')) # (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5)) # 9


#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # 'hyd'
hyd = 'Sec' # str object
print(eval('hyd')) # hyd
sec = '25' # str object
print(eval('sec')) # 25
print(eval(sec)) # error
cyb = 10.8 # float object
print(eval('cyb')) # 10.8
print(eval(cyb)) # error

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # None

#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # True
print(bool('')) # False
print(eval('  ""  ')) # ""
print(eval('')) # empty
print(eval('  " "   ')) # " "
print(eval(' ')) # empty space

# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  ')) # eval should contains str to eval ,input converts any obj to str 
print(type(x)) # according to the input obj 
print(x) # prints x object

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # input is taken from keyboard to object
print(len(a)) # if input is seq it shows len else if nonseq it gives error
print(a) # prints object
b = eval(input('Enter   any  string  : ')) # converts str to respected object
print(len(b)) # prints length of object
print(b) # prints object

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' # multiple assignment 
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #  25  10.8   Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25
				10.8
				Hyd
print(a , b , c) # 25  10.8  Hyd
print(a , b , c , separator = ':') # 25 : 10.8 : Hyd


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' # multiple assignments
print(a , b , c , end = '---') # 25---10.8---Hyd
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # error
print(a , b , c) # 25  10.8  Hyd

# Find outputs  (Home  work)
print('Hyd') #Hyd
print() # empty space
print('Sec') # Sec
print() # empty space
print('Cyb') # Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40] # list object
t = (10 , 20 , 30 , 40)# tuple object
s = {10 , 20 , 30 , 40} # set object
print(l , t , s) # [10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25 # int object
b = '%f'  %a # converts int obj to float string --'25.000000'
print(b) 25.0
print(type(b)) # <class str>
x = 10.8 # float object
y = '%d'  %x # converts into integer 
print(y) # 10
print(type(y)) <class 'str'>
m = [10 , 20 , 15 , 18] # list object
n = '%s'  %m # converts any obj into string
print(n) # '[10 , 20 , 15 , 18]'
print(type(n)) # <class 'str'>

# Find  Outputs  (Home  work)
a = 10.9274 # float obj
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) # <5 spaces>10.9
print('%10.3f'  %a) # <4 spaces>10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400

# Find  outputs (Home  work)
a = 'Hyd' # str obj
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) # Hyd
print('%s' , a) # '%s' Hyd
print('%s'  a) # error
print('%s' , %a) # error
print(a) #Hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40] # list obj
print('%s'  %a) # '[10 , 20 , 30 , 40]'
print('%s' , a) # '%s'  [10 , 20 , 30 , 40]
print('%s'  a) # error
print('%s' , %a) # error
print('%l'  %a) # error
print(a) # [10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25 # int obj
b = 10.9274 # float obj
c = 'Hyd' # str obj
print('%d    %f    %s'  %(a , b , c)) # 25  10.927400  Hyd
print('%i    %g    %s'    %(a , b , c)) # 25  10.9274  Hyd
print('%s    %s    %s'  %(a , b , c)) # '25'  '10.9274'  'Hyd'
print('%d    %g    %s'  , a , b , c) # %d %g %s   25  10.9274  Hyd
print('%d    %g      %s'   a , b , c) # error
print('%d    %g    %s'  ,  %(a , b , c)) # error
print('%d    %g    %s'    %a%b%c) # error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25  10.927400  Hyd