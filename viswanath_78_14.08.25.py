q)Modify  following  program  with  walrus  operator
Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
ans) a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = 0
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

q) index()  method  demo  program
Modify  the  following  program  with  index()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
ans) a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . index('is')
while  index != -1:
	print(index)
	index = a . index('is' , index + 1)
print('End')

q)rfind()  method  demo  program
Modify  following  program  with  rfind()  method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
ans) a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' ,0, index)
print('End')

q)	rindex()   method  demo  program
Modify  following  program  with  rindex()  method
Hint: Use   try  and  except
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
ans) a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rindex('is')
while  index != -1:
	print(index)
	index = a . rindex('is' , 0 , index )
print('End')

q)count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) #3
print(a . count('was')) #0

a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) #3
print(a . count('\n')) #3

q) Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
ans)a = input('enter the input : ')
c = ''
for i in range(len(a)):
    if i!=0 and a[i] == a[0]:
        c += '*'
    else:
        c += a[i]
print(c)   

a = '15:36:48'
print(a . split(':')) # a = ['15', '36', '48']
print(a) # 15:36:48

a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split('green')) # ['Hyd\nis ', '\tcity']
print(a . split('')) # error, empty separator

a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd' , 'is', 'green', 'city']
print(a . split()) # ['Hyd' , 'is', 'green', 'city']
print(a . split(' ')) #['Hyd\tis\tgreen\tcity']

a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd' , 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

a = 'www.gmail.com'
print(a . split('.')) # ['www' , 'gmail' , 'com']

q) Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
ans)a = input('Enter the expression: ')
c = a.split('+')
total = 0
for num in c:
    total += int(num)
print(total)

a = ['15' , '36' , '48']
print(':' . join(a)) # ‘15:36:48’
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # ‘Hyd is green city’
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # ‘15,25,52,20,10’
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # ‘www.gmail.com’
e = [15 , 36 , 48]
print(':' . join(e)) # error,input must be a list of strings
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # SankarDayalSarma 
g = range(5)
print('-' . join(g)) # error,input must be a list of strings


a = 'Hyd is green city'
print(a . endswith('city')) # True, ends with city
print(a . endswith('town')) # False, doesn’t ends with city
print(a . endswith('green' , 3 , 12)) # True, ends with green btw those indexes
print(a . endswith('green' , 3 , 13)) # False, doesn’tends with green btw those indexes
print(a . endswith(' ' , 3 , 13)) # False, doesn’t ends with ‘’ btw those indexes

q)Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters
ans) a = input('Enter the string: ')
if len(a) < 3:
    print(a)
elif a.endswith('ing'):
    print(a + 'ly')
else:
    print(a + 'ing')

print('Hyd'.isalpha())        # True, all letters
print('Rama  Rao'.isalpha())  # False, contains space
print('Hyd4'.isalpha())       # False, contains digit
print('Hyd$'.isalpha())       # False, contains symbol
print('9247'.isalpha())       # False, all digits, no letters
print('+-$'.isalpha())        # False, only symbols
print('A2#'.isalpha())        # False, contains digit and symbol
print(''.isalpha())           # False, empty string
print(' '.isalpha())          # False, space is not a letter

print('9247'.isdigit())    # True, all characters are digits
print('92a47'.isdigit())   # False, contains letter 'a'
print('92$47'.isdigit())   # False, contains symbol '$'
print('Hyd'.isdigit())     # False, only letters
print('+-$'.isdigit())     # False, only symbols
print('A2#'.isdigit())     # False, contains letter and symbol
print(''.isdigit())        # False, empty string
print(' '.isdigit())       # False, space is not a digit
print(9247.isdigit())      # Error: int object has to be in str

print('HYd'.isupper())    # False, contains lowercase letter
print('HYD'.isupper())    # True, all letters are uppercase
print('9247'.isupper())   # False, no letters at all
print('RAMA  RAO'.isupper())  # True, all letters uppercase and spaces ignored
print('+-$'.isupper())    # False, no letters at all
print('HYD123'.isupper()) # True, all letters uppercase, digits ignored
print('HYD+-$'.isupper()) # True, all letters uppercase, symbols ignored
print(''.isupper())       # False, empty string
print('A2#'.isupper())    # True, all letters uppercase, digits and symbols ignored

print('hyD'.islower())      # False, contains uppercase letter
print('hyd'.islower())      # True, all letters are lowercase
print('9247'.islower())     # False, no letters at all
print('rama  rao'.islower())# True, all letters lowercase and spaces ignored
print('+-$'.islower())      # False, no letters at all
print('hyd+-$'.islower())   # True, all letters lowercase, symbols ignored
print('abc123'.islower())   # True, all letters lowercase, digits ignored
print(''.islower())         # False, empty string
print('a2#'.islower())      # True, all letters lowercase, digits and symbols ignored

print('A7$g'.isalnum())   # False, contains symbol $
print('HYD'.isalnum())    # True, all characters are letters
print('+-$'.isalnum())    # False, only symbols
print('hyd'.isalnum())    # True, all characters are letters
print('hYd'.isalnum())    # True, all characters are letters
print('9247'.isalnum())   # True, all characters are digits
print(''.isalnum())       # False, empty string
print('A7g9'.isalnum())   # True, all characters are letters or digits

print('\n  A\t'.isspace())   # False, contains letter A
print('\n  \t'.isspace())    # True, contains only whitespace characters
print('\n  7\t'.isspace())   # False, contains digit 7
print('\n'.isspace())        # True, newline is whitespace
print('\n  $\t'.isspace())   # False, contains symbol $
print('\t'.isspace())        # True, tab is whitespace
print(''.isspace())          # False, empty string
print(' '.isspace())         # True, space is whitespace

a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a , b , c)) # a : 25   b : 10.8   c : Hyd 
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a , b , c)) # a : 25 	 b : 10.8   c : Hyd 
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a , b , c)) # a : Hyd   b : 10.8   c : 25 
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a , b , c)) # a : Hyd   b : Hyd   c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x = a , y = b , z = c)) # a : 25   b : 10.8   c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z = a , y = b , x = c)) # a : Hyd   b : 10.8   c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z = a , y = b , x = c)) # a : 25   b : 25   c : 25 

q)Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
ans) ch = input("Enter any character : ")
if ch.isalnum():
    print("Alpha Numeric Character")
    if ch.isalpha():
        print("Alphabet Character")
        if ch.isupper():
            print("Upper case Alphabet")
        else:
            print("Lower case Alphabet")
    else:
        print("Digit Character")
elif ch.isspace():
    print("White Space")
else:
    print("Special Character")

q) Write  a  program  to  reverse  a  string  without  slice
    Let  input  be   Hyd
    What  is  the  output ?  --->  dyH
ans) a = input("Enter a string: ")
b = ''	
for i in range(1, len(a) + 1):
    b += a[-i]
print(b)

q)Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
    Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd
Ans) a = input("Enter a sentence: ")
b = a.split()  
c = ''
for i in range(1, len(b) + 1):
    c +=  b[-i] + ' '
print(c)

q)Write  a  program  to  reverse  each  word  of  the  sentence
    Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic
Ans) a = input("Enter a sentence: ")
b = a.split()   
c = ''
for word in b:
    c += word[::-1] + ' '
print(c)


q) Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
Ans) a = input("Enter a string: ")
b = sorted(a)       
c = ''
for ch in b:
    c += ch        
print(c)

q) Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579
Ans) a = input("Enter a string: ")
b = sorted(a)   
alpha = ''
digit = ''
for ch in b:
    if ch.isalpha():
        alpha += ch
    else ch.isdigit():
        digit += ch
c = alpha + digit
print(c)
