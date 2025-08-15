# eval()  function  demo  program
print(eval('25'))#int 25
print(eval('10.8'))#float 10.8
print(eval('False'))#bool False
print(eval('3+4j'))#complex 3+4j
print(eval('Hyd'))#string Hyd
print(eval("    'Hyd'   "))#str Hyd
print(eval('3 + 4 * 5'))#23 int
print(eval('[10 , 20 , 15 , 18]'))#list [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))#{10,20,15,18,20,12,18}
print(eval('(10 , 20 , 30)'))#tuple(10 , 20 , 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))#{10 : 'Hyd' , 10 : 'Sec'}
print(eval(4 + 5))#int 9

#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#string hyd
hyd = 'Sec'
print(eval('hyd'))#str sec
sec = '25'
print(eval('sec'))#str sec
print(eval(sec))#error
cyb = 10.8
print(eval('cyb'))#cyb
print(eval(cyb))#error

 #  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#error

#  Find  outputs  (Home  work)
print(bool('False'))#Truw
print(eval('False'))#bool False
print(bool(''))#False
print(eval('  ""  '))#empty str
print(eval(''))#error
print(eval('  " "   '))#empty str
print(eval(' '))#error


# What  is  the  advantage  of  eval(input()) ?#error
x = eval(input('Enter  any  input  :  '))# evaluates the object
print(type(x))#object type is printed
print(x)#input object is printed 

# What  is  a  better  approach  to  read  string  input ?

a = input('Enter  any  string  :  ')
print(len(a))#3
print(a)#hyd
b = eval(input('Enter   any  string  : '))
print(len(b))#4
print(b)#hello

# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t')#25  10.8   Hyd
print(a , b , c , sep = '---')25---10.8----Hyd
print(a , b , c , sep = '\n')#25
10.8
Hyd
print(a , b , c)#25
10.8
Hyd
print(a , b , c , separator = ':')25:10.8:Hyd


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25---10.8---hyd
print(a , b , c , sep = ',,,')#25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25                   10.8.           Hyd
print(a , b , c)#25 10.8,hyd

: # Find outputs  (Home  work)
print('Hyd')#hyd
print()#empty strx
print('Sec')#sec
print()#empty line
print('Cyb')#cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#'[10 , 20 , 30 , 40]'(10 , 20 , 30 , 40)'{10 , 20 , 30 , 40}'

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)#'25.000000'
print(type(b))#string float
x = 10.8
y = '%d'  %x#10
print(y)#10
print(type(y))string integer 
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)#' [10 , 20 , 15 , 18]'
print(type(n))#string list

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)#9.0
print('%10.3f'  %a)#10.927
print('%.2f'  %a)#10.92
print('%.6f'  %a)#10.927400
print('%f'  %a)#10.927400

 # Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) #'hyd'
print('%s' , a)#'hyd:
print('%s'  a)#error
print('%s' , %a)#error
print(a)#hyd

# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)#[10 , 20 , 30 , 40]
print('%s' , a)#[10 , 20 , 30 , 40]
print('%s'  a)#error
print('%s' , %a)#error
print('%l'  %a)#[10 , 20 , 30 , 40]
print(a)#[10 , 20 , 30 , 40]


 #Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))#25 10.927400  hyd
print('%i    %g    %s'    %(a , b , c))#25 10.9274   Hyd

print('%s    %s    %s'  %(a , b , c))#'25'.  '10.9274' 'hyd'
print('%d    %g    %s'  , a , b , c)#25
10.9274
'hyd'
print('%d    %g      %s'   a , b , c)#error

print('%d    %g    %s'  ,  %(a , b , c))#errlr
print('%d    %g    %s'    %a%b%c)#25
10.9274
Hyd
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)#error