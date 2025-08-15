#Home Work-1
# eval()  function  demo  program
print(eval('25'))#25 as int
print(eval('10.8'))#10.8 as float
print(eval('False'))#False as bool
print(eval('3+4j')) #3+4j as complex
print(eval('Hyd')) #Hyd as string
print(eval("    'Hyd'   "))#Hyd as string
print(eval('3 + 4 * 5'))#23
print(eval('[10 , 20 , 15 , 18]'))#[10, 20, 15, 18]
print(eval('{10,20,15,18,20,12,18}'))#{10,15,20,12,18}
print(eval('(10 , 20 , 30)'))#(10, 20, 30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) #{10:'Sec'}
print(eval(4 + 5))#9

#Home Work-2
#  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) #hyd
hyd = 'Sec' 
print(eval('hyd')) #hyd
sec = '25'
print(eval('sec'))#sec
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#cyb
print(eval(cyb))#10.8

#Home Work-3
#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd None

#Home work-4
#  Find  outputs  (Home  work)
print(bool('False'))#True
print(eval('False'))#False
print(bool(''))#False
print(eval('  ""  '))#empty string
print(eval(''))#empty string
print(eval('  " "   '))#<space> string
print(eval(' '))#<space> string

#Home Work-5
# What  is  the  advantage  of  eval(input()) ?
we dont need to do type casting depending on the input entering like int() if input entered is int ,....
x = eval(input('Enter  any  input  :  '))#assuming entered int
print(type(x))#<class 'int'>
print(x)#entered value

#Home Work-6
# What  is  a  better  approach  to  read  string  input ?
we can use input function instead this way we can avoid type casting to string again
a = input('Enter  any  string  :  ')#say entered SSSD,
print(len(a))#4
print(a)#SSSD
b = eval(input('Enter   any  string  : '))#say entered SSSDclass
print(len(b))#9
print(b)#SSSDclass

#Home Work-7
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')   #   25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #25<tab space>10.8<tab space>Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')#25<new line>10.8<new line>Hyd
print(a , b , c)#25 10.8 Hyd
print(a , b , c , separator = ':')#25:10.8:Hyd

#Home Work-8
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25 10.8 Hyd---
print(a , b , c , sep = ',,,')#25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25:::10.8:::Hyd<tab space><tab space><tab space>
print(a , b , c)#25 10.8 Hyd

#Home Work-9
# Find outputs  (Home  work)
print('Hyd')#Hyd
print()#<new line>
print('Sec')#Sec
print()#<new line>
print('Cyb')#Cyb

#Home Work-10
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

#Home Work-11
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)#25.0 as string
print(type(b))#<class 'str'>
x = 10.8
y = '%d'  %x
print(y)#10
print(type(y))#<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m 
print(n)#'[10, 20, 15, 18]'
print(type(n))#<class 'str'>

#Home Work-12
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a) #<7spaces>10.9
print('%10.3f'  %a) #<8 spaces>10.927
print('%.2f'  %a) #10.93
print('%.6f'  %a)#10.927400
print('%f'  %a)#10.927400

#Home Work-13
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #  <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4   spaces>
print('%2s'  %a)   #  Hyd  and  ignores  smaller width
print('%s'  %a) #Hyd
print('%s' , a)#%s Hyd
print('%s'  a) #error
print('%s' , %a)#error
print(a)#Hyd

#Home Work-14
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)#'[10 , 20 , 30 , 40]'
print('%s' , a)#%s [10 , 20 , 30 , 40]
print('%s'  a)# error
print('%s' , %a) #error
print('%l'  %a)# [10 , 20 , 30 , 40]
print(a)[10 , 20 , 30 , 40]

#Home Work-15
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c))#25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))#25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c)#%d %g %s 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c)#error
print('%d    %g    %s'  ,  %(a , b , c))#25 10.9274 Hyd
print('%d    %g    %s'    %a%b%c) #error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #25 10.927400 Hyd
