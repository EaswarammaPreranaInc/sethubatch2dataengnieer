##1
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

while (index := a.find('is', (index + 1) if 'index' in locals() else 0)) != -1:
    print(index)

print('End')

##2
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

start = 0
while True:
    try:
        index = a.index('is', start)
        print(index)
        start = index + 1
    except ValueError:
        break

print('End')

##3
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)  # Search from start up to previous index

print('End')

##4
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

end = len(a)  # start search from the end of the string
while True:
    try:
        index = a.rindex('is', 0, end)
        print(index)
        end = index  # update end position to search further left
    except ValueError:
        break

print('End')

##5
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

# Count total occurrences of "is"
print(a.count('is'))          # 4

# Count occurrences of "is" between index 19 and 48
print(a.count('is', 19, 48))  # 2

# Count occurrences of "was" (not present)
print(a.count('was'))         # 0

##6
print(a.count(' '))   # 3
print(a.count('\t'))  # 3
print(a.count('\n'))  # 3

##7
s = "babble"
first_char = s[0]
# Replace all occurrences of first_char with '*'
s = s.replace(first_char, '*')
# Restore the first character
s = first_char + s[1:]
print(s)

##8
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#['15', '36', '48']
print(a)#15:36:48

##9
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd\nis', 'green\tcity']
print(a . split('green'))#['Hyd\nis', 'city']
print(a . split(''))#error

##10
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd', 'is', 'green', 'city']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

##11
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())#['Hyd','is','green','city']
print(a . split(' '))#['Hyd','is','green','city']

##12
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']

##13
expr = "123+45+6+789"
parts = expr.split('+')         # ['123', '45', '6', '789']
total = sum(int(num) for num in parts)
print(total)
#print(sum(map(int, "123+45+6+789".split('+'))))

##14
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#'15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#'Hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#'10,20,15,25,52'
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#15:36:48
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#'Sankardayalsarma'
g = range(5)
print('-' . join(g))#'0-1-2-3-4'

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

##15
s = input("Enter a string: ")

if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "ing"

print(result)

##16
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha())#False
print('Hyd$'  . isalpha())#False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())#False
print(' '  .  isalpha())#False

##17
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())#False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#False
print(' ' . isdigit())#False
print(9247 . isdigit())#False

##18
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper())#False
print('HYD123' . isupper())#True
print('HYD+-$' . isupper())#False
print('' . isupper())#False
print('A2#' . isupper())#False

##19
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#False
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#False

# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())#False
print('hyd' . isalnum())#True
print('hYd' . isalnum())#False
print('9247' . isalnum())#True
print('' . isalnum())#False
print('A7g9'  . isalnum())#True

# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())#False
print('\t' . isspace())#True
print('' . isspace())#False
print(' ' . isspace())#False

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) 
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))

#a  :  25  	b  :  10.8  	c  :  Hyd  
#a  :  25  	b  :  10.8  	c  :  Hyd  
#a  :  Hyd  	b  :  10.8  	c  :  25  
#a  :  Hyd  	b  :  Hyd  	c  :  Hyd  
#a  :  25  	b  :  10.8  	c  :  Hyd  
#a  :  Hyd  	b  :  10.8  	c  :  25  
#a  :  25  	b  :  25  	c  :  25 

##20
# Program to determine type of character entered by user

ch = input("Enter a single character: ")

if ch.isalnum():  # Alphanumeric check
    print("Alphanumeric character")

    if ch.isalpha():  # Alphabet check
        print("Alphabet character")

        if ch.isupper():
            print("Upper case alphabet")
        elif ch.islower():
            print("Lower case alphabet")

    elif ch.isdigit():  # Digit check
        print("Digit character")

elif ch.isspace():  # White space check
    print("White space")

else:  # Special character check
    print("Special character")


##21
# Program to reverse a string without slice

a = input("Enter a string: ")
b = ""  # to store reversed string

for i in range(1, len(a) + 1):
    b = b + a[-i]   # pick last character first, move backwards

print("Reversed string:", b)

##22
# Program to reverse order of words without slice

a = input("Enter a sentence: ")
b = a.split()    # split into list of words
c = ""           # to store reversed order

for i in range(1, len(b) + 1):
    c = c + b[-i] + " "   # pick last word first, move backwards

print("Reversed sentence:", c.strip())  # strip() removes last extra space


##23
# Program to reverse each word in a sentence

a = input("Enter a sentence: ")
b = a.split()   # split sentence into words
c = ""          # store reversed words

for word in b:
    c = c + word[::-1] + " "   # reverse each word using slicing

print("Reversed words:", c.strip())  # remove last space

##24
# Program to sort string in alphabetical order

a = input("Enter a string: ")   # e.g., RAJESH
b = sorted(a)                   # returns list of sorted characters
c = "".join(b)                   # join list into string
print("Sorted string:", c)

##25
# Program to sort alphabets and digits separately

a = input("Enter a string: ")  # e.g., Z9K3PA7D51

# Sort entire string first
b = sorted(a)  # → ['1', '3', '5', '7', '9', 'A', 'D', 'K', 'P', 'Z']

alpha = ""
digit = ""

for ch in b:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch

# Combine alphabets and digits
result = alpha + digit
print("Sorted string:", result)






