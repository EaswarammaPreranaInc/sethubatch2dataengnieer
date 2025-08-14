# eval()  function  demo  program
print(eval('25'))  #  25
print(eval('10.8'))  #  10.8
print(eval('False'))  #  False
print(eval('3+4j'))  # 3+4j
print(eval('Hyd'))  #  Hyd
print(eval("    'Hyd'   "))  #  'Hyd'
print(eval('3 + 4 * 5'))  #  23
print(eval('[10 , 20 , 15 , 18]'))  #  [10 , 20 , 15 , 18]'
print(eval('{10,20,15,18,20,12,18}'))  #  {10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)'))  #  (10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))  #  { 10 : 'Sec'}
print(eval(4 + 5))  #  9



#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  #  'hyd'
hyd = 'Sec'  
print(eval('hyd'))  #  Sec
sec = '25'
print(eval('sec'))  #  25
print(eval(sec))  #  25
cyb = 10.8
print(eval('cyb'))  #cyb
print(eval(cyb))  #  10.8

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))  #   Hyd

#  Find  outputs  (Home  work)
print(bool('False'))  #  False
print(eval('False'))  #  False
print(bool(''))  #  False
print(eval('  ""  '))  # ""
print(eval(''))  #  ''
print(eval('  " "   '))  #  " "
print(eval(' '))  #  empty

# What  is  the  advantage  of  eval(input()) ?   #  Its used to convert the string data to real data.
x = eval(input('Enter  any  input  :  '))  
print(type(x))  #  Class 'int'
print(x)  #  25

# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')  # 'hyd'
print(len(a))  #  3
print(a)  #  hyd
b = eval(input('Enter   any  string  : '))  #  'sec'
print(len(b))  #  3
print(b)  #  Sec

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')  #  25	10.8	Hyd
print(a , b , c , sep = '---')  #  25---10.8---Hyd
print(a , b , c , sep = '\n')  #  25  <nextline>  10.8 < Nextline> Hyd
print(a , b , c)  #  25	10.8 Hyd
print(a , b , c , separator = ':')  #  Error


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  #    25 10.8 'Hyd'---  
print(a , b , c , sep = ',,,')  #  25 ,,,10.8 ,,,'Hyd'
print(a , b , c , sep = ':::' , end = '\t\t\t')   25 :::10.8 :::'Hyd'			
print(a , b , c)   #  25 10.8 'Hyd'

# Find outputs  (Home  work)
print('Hyd')  #  Hyd
print()  #  Empty
print('Sec')  #  Sec
print()  #  Empty
print('Cyb')  #  Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)   #   [10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)  #   25.000000
print(type(b))  #  float 'str'
x = 10.8
y = '%d'  %x
print(y)  #  10
print(type(y))  #  class 'str'
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)  #  [10 , 20 , 15 , 18]
print(type(n)) #  class str


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f' % a)  # '   10.93'
print('%9.1f' % a)  # '  10.9'
print('%10.3f' % a)  #  '   10.927'
print('%.2f' % a)  #  '10.93'
print('%.6f' % a)  #  '10.927400'
print('%f' % a)  # '10.927400'

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)   #  [10,20,30,40]
print('%s' , a) #  Error
print('%s'  a)  #  Error
print('%s' , %a)  #  Error
print('%l'  %a)  #  error
print(a)  #  [10,20,30,40]
