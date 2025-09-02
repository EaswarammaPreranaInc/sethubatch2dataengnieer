# Modify  following  program  with  walrus  operator. Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
   print(index)
print('End')


'''
(Home  work)
index()  method  demo  program. Modify  the  following  program  with  index()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while True:
   try:
       index = a.index('is', index + 1)
       print(index)
   except ValueError:
       break
print('End')


'''
(Home work)
rfind() method demo program. Modify following program with rfind() method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is')
while index != -1:
   print(index)
   index = a.rfind('is', 0, index)
print('End')


'''
(Home work)
rindex() method demo program. Modify following program with rindex() method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
   index = a.rindex('is')
   while index != -1:
       print(index)
       index = a.rindex('is', 0, index)
except ValueError:
   print("No more occurrences found.")
print('End')


# Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

s = input("Enter a string: ")
first_char = s[0]
result = first_char + s[1:].replace(first_char, '*')
print(result)


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the sumresult
'''

expr = input("Enter the expression: ")
numbers = expr.split('+')
total = sum(int(num) for num in numbers)
print("Sum:", total)


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters.
'''

s = input("Enter a string: ")
if len(s) < 3:
   result = s
elif s.endswith("ing"):
   result = s + "ly"
else:
   result = s + "ing"
print(result)


#  Write a program to determine user input is alphabet , digit , white space or special character

ch = input("Enter a single character: ")

if ch.isalnum():
   print("Alphanumeric character")

   if ch.isalpha():
       print("Alphabet character")

       if ch.isupper():
           print("Upper case alphabet")
       else:
           print("Lower case alphabet")

   elif ch.isdigit():
       print("Digit character")

elif ch.isspace():
   print("White space")

else:
   print("Special character")


'''
Write a program to reverse a string without slice
Let input be Hyd
What is the output ? ---> dyH
'''

s = input("Enter any string: ")
rev = ""
for i in range(1, len(s) + 1):
   rev += s[-i]
print("Reverse String :", rev)


'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
Let  input  be  Hyd  is  green  city
What  is  the  output ?  ---> city   green   is   Hyd
'''

s = input("Enter any sentence: ")
words = s.split()
rev_sentence = ""
for i in range(1, len(words) + 1):
   rev_sentence += words[-i] + " "
print("Reverse order of words:", rev_sentence.strip())


'''
Write  a  program  to  reverse  each  word  of  the  sentence
Let  input  be  Hyd  is  green  city
What  is  the  output ?  ---> dyH si neerg ytic
'''

s = input("Enter any sentence: ")
words = s.split()
rev_sentence = ""
for word in words:
   rev_sentence += word[::-1] + " "
print("Reversed each word:", rev_sentence.strip())


'''
Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  ---> AEHJRS
'''

s = input("Enter any string: ")
sorted_str = "".join(sorted(s))
print("Sorted string:", sorted_str)


'''
Write a program to sort string such that alphabets in alphabetical order and digits in ascending order
Let input be Z9K3PA7D51
What is the output ? ---> ADKPZ13579
'''

s = input("Enter any string: ")
alpha = ""
digit = ""
for ch in sorted(s):
   if ch.isalpha():
       alpha += ch
   elif ch.isdigit():
       digit += ch
result = alpha + digit
print("Sorted string:", result)


# count() method demo program (Home work)

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))         # 4
print(a.count('is', 19, 48)) # 2
print(a.count('was'))        # 0


# Find outputs (Home work)

a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))   # 3
print(a.count('\t'))  # 3
print(a.count('\n'))  # 3


# Find outputs (Home work)

a = '15:36:48'
print(a.split(':'))   # ['15', '36', '48']
print(a)              # 15:36:48


# Find outputs (Home work)

a = 'Hyd\nis green\tcity'
print(a.split(' '))       # ['Hyd\nis', 'green\tcity']
print(a.split())          # ['Hyd', 'is', 'green', 'city']
print(a.split('green'))   # ['Hyd\nis ', '\tcity']
print(a.split(''))        # ERROR: empty separator


# Find outputs (Home work)

a = 'Hyd\tis\tgreen\tcity'  # There is a tab between the words
print(a.split('\t'))        # ['Hyd', 'is', 'green', 'city']
print(a.split())            # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))         # ['Hyd\tis\tgreen\tcity'] (no spaces to split)


# Find outputs (Home work)

a = 'Hyd   is   green   city'  # There are 3 spaces between the words
print(a.split())               # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))            # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


# Find outputs (Home work)

a = 'www.gmail.com'
print(a.split('.'))            # ['www', 'gmail', 'com']


# Find outputs (Home work)

a = ['15', '36', '48']
print(':'.join(a))            # 15:36:48
b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))            # Hyd is green city
c = {'10', '20', '15', '25', '52'}
print(','.join(c))            # sets are unordered e.g. 25,15,52,20,10
d = ['www', 'gmail', 'com']
print('.'.join(d))            # www.gmail.com
e = [15, 36, 48]
print(':'.join(e))            # Error - join() expects strings, not integers
f = ['Sankar', 'Dayal', 'Sarma']
print(''.join(f))             # SankarDayalSarma
g = range(5)
print('-'.join(g))            # Error - join() expects strings, not integers


# endswith() method demo program (Home work)

a = 'Hyd is green city'
print(a.endswith('city'))           # True
print(a.endswith('town'))           # False
print(a.endswith('green', 3, 12))   # True
print(a.endswith('green', 3, 13))   # False
print(a.endswith(' ', 3, 13))       # False


#  isalpha()  method  demo  program (Home work)

print('Hyd'.isalpha())        # True, all letters
print('Rama Rao'.isalpha())   # False, contains a space
print('Hyd4'.isalpha())       # False, contains a digit
print('Hyd$'.isalpha())       # False, contains a special char
print('9247'.isalpha())       # False, only digits, no letters
print('+-$'.isalpha())        # False, only special chars
print('A2#'.isalpha())        # False, letters + digit + special char
print(''.isalpha())           # False, empty string
print(' '.isalpha())          # False, only space


# isdigit()  method  demo  program  (Home  work)

print('9247'.isdigit())   # True, all digits
print('92a47'.isdigit())  # False, contains a letter
print('92$47'.isdigit())  # False, contains a special char
print('Hyd'.isdigit())    # False, all letters
print('+-$'.isdigit())    # False, only special chars
print('A2#'.isdigit())    # False, letter, digit, and special char
print(''.isdigit())       # False, empty string
print(' '.isdigit())      # False, space only
print(9247 .isdigit())    # ERROR, int object has no attribute 'isdigit'


# isupper()  method  demo  program  (Home  work)

print('HYd'.isupper())        # False, contains lowercase
print('HYD'.isupper())        # True, all letters uppercase
print('9247'.isupper())       # False, no letters
print('RAMA  RAO'.isupper())  # True, all letters uppercase (spaces ignored)
print('+-$'.isupper())        # False, no letters
print('HYD123'.isupper())     # True, all letters uppercase (digits ignored)
print('HYD+-$'.isupper())     # True, all letters uppercase (special chars ignored)
print(''.isupper())           # False, empty string
print('A2#'.isupper())        # True, all letters uppercase


# islower()  method  demo  program  (Home  work)

print('hyD'.islower())        # False, contains uppercase
print('hyd'.islower())        # True, all letters lowercase
print('9247'.islower())       # False, no letters
print('rama  rao'.islower())  # True, all letters lowercase (spaces ignored)
print('+-$'.islower())        # False, no letters
print('hyd+-$'.islower())     # True, all letters lowercase (special chars ignored)
print('abc123'.islower())     # True, all letters lowercase (digits ignored)
print(''.islower())           # False, empty string
print('a2#'.islower())        # True, all letters lowercase


# isalnum() method demo program (Home work)

print('A7$g'.isalnum())   # False, contains special character $
print('HYD'.isalnum())    # True, all alphabetic
print('+-$'.isalnum())    # False, only special characters
print('hyd'.isalnum())    # True, all alphabetic
print('hYd'.isalnum())    # True, all alphabetic (case doesn't matter)
print('9247'.isalnum())   # True, all digits
print(''.isalnum())       # False, empty string
print('A7g9'.isalnum())   # True, letters and digits only


# isspace() method demo program (Home work)

print('\n  A\t'.isspace())   # False, contains letter 'A'
print('\n  \t'.isspace())    # True, only whitespace characters (newline, spaces, tab)
print('\n  7\t'.isspace())   # False, contains digit '7'
print('\n'.isspace())        # True, only newline
print('\n  $\t'.isspace())   # False, contains special char '$'
print('\t'.isspace())        # True, only tab
print(''.isspace())          # False, empty string
print(' '.isspace())         # True, only space


# Find outputs (Home work)

a, b, c = 25, 10.8, 'Hyd'
print('a: {} \t b: {} \t c: {}'.format(a, b, c))
print('a: {0} \t b: {1} \t c: {2}'.format(a, b, c))
print('a: {2} \t b: {1} \t c: {0}'.format(a, b, c))
print('a: {2} \t b: {2} \t c: {2}'.format(a, b, c))
print('a: {x} \t b: {y} \t c: {z}'.format(x=a, y=b, z=c))
print('a: {x} \t b: {y} \t c: {z}'.format(z=a, y=b, x=c))
print('a: {z} \t b: {z} \t c: {z}'.format(z=a, y=b, x=c))


Output:
a: 25 	 b: 10.8 	 c: Hyd
a: 25 	 b: 10.8 	 c: Hyd
a: Hyd 	 b: 10.8 	 c: 25
a: Hyd 	 b: Hyd 	 c: Hyd
a: 25 	 b: 10.8 	 c: Hyd
a: Hyd 	 b: 10.8 	 c: 25
a: 25 	 b: 25 	 c: 25

