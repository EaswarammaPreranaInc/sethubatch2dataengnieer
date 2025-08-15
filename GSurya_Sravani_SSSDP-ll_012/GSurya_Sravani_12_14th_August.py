# Q1) count() method
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))   # 3
print(a.count('\t'))  # 3
print(a.count('\n'))  # 3


# Q2) split() method 
a = 'Hyd\nis green\tcity'
print(a.split(' '))       # ['Hyd\nis', 'green\tcity']
print(a.split())          # ['Hyd', 'is', 'green', 'city']
print(a.split('green'))   # ['Hyd\nis ', '\tcity']
try:
    print(a.split(''))    # ValueError: empty separator
except ValueError as e:
    print("Error:", e)    # Error: empty separator


# Q3) split() method
a = 'Hyd\tis\tgreen\tcity'
print(a.split('\t'))    # ['Hyd', 'is', 'green', 'city']
print(a.split())        # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))     # ['Hyd\tis\tgreen\tcity']


# Q4) split() with multiple spaces
a = 'Hyd   is   green   city'
print(a.split())        # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))     # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
# split() method
a = 'www.gmail.com'
print(a.split('.'))# ['www', 'gmail', 'com']


#  join() method 
a = ['15', '36', '48']
print(':'.join(a)) # 15:36:48

b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))# Hyd is green city

c = {'10', '20', '15', '25', '52'}
print(','.join(c))# order may vary (e.g., '52,20,25,15,10')

d = ['www', 'gmail', 'com']
print('.'.join(d))#www.gmail.com

e = [15, 36, 48]
# print(':'.join(e))# error

f = ['Sankar', 'Dayal', 'Sarma']
print(''.join(f))#SankarDayalSarma

g = range(5)
# print('-'.join(g)) # error
# endswith() method
a = 'Hyd is green city'
print(a.endswith('city'))             # True
print(a.endswith('town')) #False
print(a.endswith('green', 3, 12))     # True
print(a.endswith('green', 3, 13))     # False
print(a.endswith(' ', 3, 13))         # True

isalpha() method

print('Hyd'.isalpha()) # True
print('Rama  Rao'.isalpha())#False
print('Hyd4'.isalpha()) # False
print('Hyd$'.isalpha())  # False
print('9247'.isalpha())  # False
print('+-$'.isalpha()) # False
print('A2#'.isalpha()) # False
print(''.isalpha()  # False
print(' '.isalpha())# False

isdigit() method
python
print('9247'.isdigit()) # True
print('92a47'.isdigit()) # False
print('92$47'.isdigit()) # False
print('Hyd'.isdigit())# False
print('+-$'.isdigit()) # False
print('A2#'.isdigit()) # False
print(''.isdigit())# False
print(' '.isdigit())  # False
# print(9247.isdigit())  #Error

isupper() method
python
print('HYd'.isupper()) # False
print('HYD'.isupper())# True
print('9247'.isupper())# False
print('RAMA  RAO'.isupper())  # True
print('+-$'.isupper())# False
print('HYD123'.isupper())#True
print('HYD+-$'.isupper()) #True
print(''.isupper())# False
print('A2#'.isupper())# True

print('A7$g'.isalnum())# False
print('HYD'.isalnum()) # True
print('+-$'.isalnum()) # False
print('hyd'.isalnum()) # True
print('hYd'.isalnum())    # True
print('9247'.isalnum())# True
print(''.isalnum())# False
print('A7g9'.isalnum())# True

print('\n  A\t'.isspace()) # False
print('\n  \t'.isspace())    # True
print('\n  7\t'.isspace())# False
print('\n'.isspace())# True
print('\n  $\t'.isspace()) # False
print('\t'.isspace()) # True
print(''.isspace())  # False
print(' '.isspace()) # True

a, b, c = 25, 10.8, 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}'.format(a, b, c))  # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}'.format(a, b, c))               # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}'.format(a, b, c))               # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}'.format(a, b, c))               # a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}'.format(x=a, y=b, z=c))         # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}'.format(z=a, y=b, x=c))         # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}'.format(z=a, y=b, x=c))         # a  :  25  	  b  :  25  	  c  :  25


#walrus operator 
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

#Modify  the  following  program  with  rfind()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , 0,index)
print('End')                                                                                                                              46
42
23
4
End

#Modify  following  program  with  rindex()  method

#Hint: Use   try  and  except
try:
  a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
  b = a . rindex('is')
  while  b != -1:
	  print(b)
	  b = a . rindex('is' ,  0,b)
  print('End')
except :
    print("error")                                                                                                                              46
42
23
4
error

#Modify  following  program  with  index()  method
try:
  a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
  b = a . index('is')
  while  b != -1:
	  print(b)
	  b = a . index('is' ,b+1 )
  print('End')

except:
   print("error")
4
23
42
46
error

a = "babble"
b = a[0] + a[1:].replace("b", "*")  
print(b)
ba**le

a = input("Enter the expression: ")   
b = a.split("+")                   
sum = 0
for num in b:
    sum += int(num)
print(f"sum is :{sum} ")
Enter the expression: 125+30+60
sum is :215

a=input("enter a string: ")
b=a.endswith("ing")
if len(a)<=2:
     print(a)
elif  b:
       a= a+"ly"
       print(a)
else :
     a= a+ "ing"
     print(a)

a=input("enter any character : ")
b=a.isalpha()
c=a.isdigit()
d=a.isupper()
e=a.islower()
f=a.isspace()
h=a.isalnum()
if b:
   print("It is a Alpha Numeric Charcter")
if c:
   print("It is a digfit")
elif d:
   print("It is a uppercase chracter")
elif e:
   print("It is a lower character")
elif f:
   print("It is a special character")
elif h:
   print("It is a  combination of character and a number ")
  C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
enter any character : A7g9
It is a  character and a special Character

C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
enter any character : Afg3
It is a  combination of character and a number

C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
enter any character : A
It is a Alpha Numeric Charcter
It is a uppercase chracter

C:\Users\G SURYA SRAVANI>python C:\learnpython\mypython.py
enter any character : ad
It is a Alpha Numeric Charcter
It is a lower character


a = input("Enter a string: ")
b = ""
for i in range(1, len(a) + 1):
    b += a[-i]
print("Reversed string:", b)

Enter a string: Python
Reversed string: nohtyP


a = input("Enter a sentence: ")
b = a.split()   # split into words
c = ""
for i in range(1, len(b) + 1):
    c += b[-i] + " "
print(c)

city green is Hyd

# sorting of string 
a = input("Enter a string: ")
b = list(a)      
b.sort()         
Print(" ".join(b))

a="hyd is green city"
b=a.split(" ")

for i in range(len(b)):

         b[i] = "".join(sorted(b[i]))
print(b)

a=input("enter a string and numbers: ")
b = "".join(sorted(a))
alpha = ""
digit = ""
for ch in b:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
print(alpha)
print(digit)
enter a string and numbers: acgbs321
abcgs
123