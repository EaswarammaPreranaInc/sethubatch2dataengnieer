# What  is   the   better  way  to  read  string  input ?  --->  input()
a = input('Enter  any  string  :  ')       #  'Hyd'
print(len(a))                              #  3
print(a)                                   #  Hyd
b = eval(input('Enter   any  string  : ')) #  'Hyd'
print(len(b))                              #   3
print(b)                                   #  Hyd


#Print Function
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')        #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')       #  25 <tab> 10.8 <tab> Hyd
print(a , b , c , sep = '---')      # 25---10.8---Hyd
print(a , b , c , sep = '\n')       # 25 <next line> 10.8<next line> Hyd
print(a , b , c)                    # 25 <space> 10.8 <space> Hyd
#print(a , b , c , separator = ':') # TypeError : No separator keyword argument for print() function

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')                  #25 <space> 10.8 <space> Hyd  ---  <same  line>
print(a , b , c , sep = ',,,')                  #25,,,10.8,,,Hyd  <next  line>
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd  <tab><tab><tab>  <same  line>
print(a , b , c)                                #25 <space> 10.8 <space> Hyd  <next  line>

#sep is middle, end is last

# Find outputs  (Home  work)
print('Hyd') #Hyd  <next  line>
print()      #<next  line>
print('Sec') #Sec <next  line>
print()      #<next  line>
print('Cyb') #Cyd  <next  line>

#don't forget to write how output has ended


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10, 20, 30, 40]  <space> (10, 20, 30, 40)  <space> {40, 10, 20, 30}  (set  in  any  order)



#Eval Function
# eval()  function  demo  program
print(eval('25'))                         #  Converts  '25'  to  25
print(eval('10.8'))                       #  Converts  '10.8'  to   10.8
print(eval('False'))                      #  Converts  'False'  to   False
print(eval('3+4j'))                       #  Converts  '3+4j'  to   3+4j
print(eval('Hyd'))              #  Converts   'Hyd'  to  object  Hyd  which  does  not  exist  and  hence  NameError
print(eval("    'Hyd'   "))               #  Converts  "    'Hyd'   "  to   'Hyd'
print(eval('3 + 4 * 5'))                  #  Converts   '3+4*5'   to   3+4*5 = 23
print(eval('[10 , 20 , 15 , 18]'))        #  Converts  '[10 , 20 , 15 , 18]'  to  [10 , 20 , 15 , 18]
print(eval('{10,20,15,18,20,12,18}'))     #  Converts  '{10,20,15,18,20,12,18}'  to  {10,20,15,18,12}
print(eval('(10 , 20 , 30)'))             #  Converts  '(10,20,30)'  to  (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))  #  Converts  "{10 : 'Hyd' , 10 : 'Sec'}"  to   {10 : 'Sec'}
print(eval(4 + 5))  

#Tricky program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))  #Converts   "   'hyd'  "  to   'hyd'
hyd = 'Sec'
print(eval('hyd'))           #Converts  'hyd'  to  object  hyd   which  is  'Sec'
sec = '25'
print(eval('sec'))           #Converts  'sec'  to  object   sec  which  is  '25'
print(eval(sec))             #Converts   object  sec  which  has   '25'  to  integer  25
cyb = 10.8
print(eval('cyb'))           #Converts  'cyb'  to  object   cyb   which  is   10.8
#print(eval(cyb))            #TypeError :  cyb  is  neither  a  string literal  nor  a  str  object (or bytes or code object)



#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))   #  print(print("Hyd"))  --->  print(None)  --->  None
#when solving think like cpu, step by step. never like human brain



#  Find  outputs  (Home  work)
print(bool('False'))     #True :  'False'  is   a  non-empty  string
print(eval('False'))     #converts  'False'  to  False
print(bool(''))          #Converts  ''  to   False
print(eval('  ""  '))    #Converts  '   ""   '  to   ""  i.e.  Empty  string
#print(eval(''))         #SyntaxError  :  Converts  ''  to   nothing
print(eval('  " "   '))  #Converts  '   " "   '  to   " "  i.e.   space
#print(eval(' '))        #SyntaxError :  Converts  ' '  to   nothing

# What  is  the  advantage  of  eval(input()) ?  --->  It  can  read  any  kind  of  input
try:
	x = eval(input('Enter  any  input  :  '))
	print(type(x))
	print(x)
except:
	print('Input  string  should  be in quotes')

#Enter  any  input  :  {23:23, 234:nsjd} #NameError:name 'nsjd' is not defined, even value you have to give as string



# Formats  demo  program
a = 25.68
print('%d'  %a)       #Converts  object  'a'  to   string  integer  due  to  '%d'  i.e.  '25'
print('%s'  %a)       #Converts  object  'a'  to   string  due  to  '%s'  i.e.  '25.68'
print('%f'  %a)       #Converts  object  'a'  to   string  float   due  to  '%f'  i.e.  '25.680000'
print('%g'  %a)       #Converts  object  'a'  to   string  float   due  to  '%g'  i.e.  '25.68'
#print('%f' ,  %a)    #Invalid Syntax, string and percent together form one token, Error  due  to  comma
print('a : ' ,  a)    #a :  <space> 25.68
print('%f' ,  a)      #%f  <space>  25.68
#print('%f'  a)       #Invalid Syntax  :  %  is  missing  for  object  'a'
#print('a:'  %a)      #TypeError: not all arguments converted during string formatting, format is missing


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a             # Converts  object  'a'  to  string  float  due  to  '%f'
print(b)                 # 25.000000
print(type(b))           # <class 'str'>
x = 10.8
y = '%d'  %x             #  Converts  object  'x'  to  string  int  due  to  '%d'
print(y)                 # 10
print(type(y))           # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m             #   Converts  list   to  string   list  due  to  '%s'
print(n)                 #  [10 , 20 , 15 , 18]
print(type(n))           # <class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #<3  spaces>10.93
print('%9.1f'  %a)  #<5 spaces> 10.9
print('%10.3f'  %a) #<4 spaces> 10.927
print('%.2f'  %a)   #10.93
print('%.6f'  %a)   #10.927400
print('%f'  %a)     #10.927400
print('%g' %a)      #10.9274

# '%x.yf', x is total chars, y is chars after decimal


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)   #<4  spaces>Hyd
print('%-7s'  %a)  #Hyd <4 spaces>
print('%2s'  %a)   #Hyd  and  ignores  smaller  width  2
print('%s'  %a)    #Hyd
print('%s' , a)    #%s  <space>  Hyd
#print('%s'  a)    #SyntaxError : Either comma is missing between %s and object 'a' (or) % is missing for object 'a'
#print('%s' , %a)  #SyntaxError due to comma
print(a)           #Hyd

#- means left alignment, + means right alignment, number means total chars


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)          #Converts  [10 , 20 , 30 , 40]  to  "[10, 20, 30, 40]"
print('%s' , a)          #%s  <space>  [10, 20, 30, 40]
#print('%s'  a)          #Invalid Syntax:   comma  is  missing  between   %s  and  list  'a'  (or)  %  is  missing  for  list  'a'
#print('%s' , %a)        #Invalid Syntax: Error  due  to  comma
#print('%l'  %a)         #ValueError: incomplete format :  %l  format  does  not  exist
print(a)                 #[10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d  %f  %s'  %(a , b , c))         #25 <4  spaces> 10.927400 <4  spaces> Hyd
print('%i  %g  %s'  %(a , b , c))         #25 <4  spaces> 10.9274 <4  spaces> Hyd
print('%s  %s  %s'  %(a , b , c))         #25 <4  spaces> 10.9274 <4  spaces> Hyd
print('%d  %g  %s'  , a , b , c)          #%d    %g    %s  <space> 25  <space> 10.9274  <space> Hyd
#print('%d%g%s'  a, b, c)          #Invalid Syntax :comma is missing between the format and objects (or) % is missing for objects a , b, c
#print('%d  %g  %s' ,  %(a , b , c))      #Invalid Syntax: Error  due  to  comma
#print('%d  %g  %s'  %a%b%c)              #TypeError: not enough arguments for format string, due  to  multiple  %'s
print('%d' %a  , '%f' %b ,  '%s' %c)      #25 <space> 10.927400 <space> Hyd


