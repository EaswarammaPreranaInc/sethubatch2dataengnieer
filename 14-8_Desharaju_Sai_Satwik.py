a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
while (index := a.find('is', (index + 1) if 'index' in locals() else 0)) != -1:
    print(index)
print('End')
# 4
# 23
# 40
# End

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is', index + 1)
except ValueError:
    print('End')
# 4
# 23
# 40
# End

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)
print('End')
# 40
# 23
# 4
# End

# rindex() method version
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a.rindex('is')
    while True:
        print(index)
        index = a.rindex('is', 0, index)
except ValueError:
    print('End')
# 40
# 23
# 4
# End

# count() method demo program
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))         # 4
print(a.count('is', 19, 48)) # 1
print(a.count('was'))        # 0

a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))   # 0
print(a.count('\t'))  # 3
print(a.count('\n'))  # 3

s = 'babble'
print(s[0] + s[1:].replace(s[0], '*'))  # ba**le

# split(':')
a = '15:36:48'
print(a.split(':'))  # ['15', '36', '48']
print(a)             # 15:36:48

a = 'Hyd\nis green\tcity'
print(a.split(' '))     # ['Hyd\nis', 'green\tcity']
print(a.split())        # ['Hyd', 'is', 'green', 'city']
print(a.split('green')) # ['Hyd\nis ', '\tcity']
# print(a.split(''))    # ValueError: empty separator

# split with tab
a = 'Hyd\tis\tgreen\tcity'
print(a.split('\t'))  # ['Hyd', 'is', 'green', 'city']
print(a.split())      # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))   # ['Hyd\tis\tgreen\tcity']

a = 'Hyd   is   green   city'
print(a.split())     # ['Hyd', 'is', 'green', 'city']
print(a.split(' '))  # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# split('.')
a = 'www.gmail.com'
print(a.split('.'))  # ['www', 'gmail', 'com']

expr = '123+45+6+789'
print(sum(map(int, expr.split('+'))))  # 963

a = ['15', '36', '48']
print(':'.join(a))  # 15:36:48
b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))  # Hyd is green city
c = {'10', '20', '15', '25', '52'}
print(','.join(c))  # order may vary
d = ['www', 'gmail', 'com']
print('.'.join(d))  # www.gmail.com
# e = [15, 36, 48]
# print(':'.join(e)) # TypeError
f = ['Sankar', 'Dayal', 'Sarma']
print(''.join(f))   # SankarDayalSarma
# g = range(5)
# print('-'.join(g)) # TypeError

a = 'Hyd is green city'
print(a.endswith('city'))       # True
print(a.endswith('town'))       # False
print(a.endswith('green', 3, 12)) # True
print(a.endswith('green', 3, 13)) # False
print(a.endswith(' ', 3, 13))     # True



# isalpha()
print('Hyd'.isalpha())      # True
print('Rama  Rao'.isalpha())# False
print('Hyd4'.isalpha())     # False
print('Hyd$'.isalpha())     # False
print('9247'.isalpha())     # False
print('+-$'.isalpha())      # False
print('A2#'.isalpha())      # False
print(''.isalpha())         # False
print(' '.isalpha())        # False

# isdigit()
print('9247'.isdigit())     # True
print('92a47'.isdigit())    # False
print('92$47'.isdigit())    # False
print('Hyd'.isdigit())      # False
print('+-$'.isdigit())      # False
print('A2#'.isdigit())      # False
print(''.isdigit())         # False
print(' '.isdigit())        # False
# print(9247.isdigit())     # AttributeError

# isupper()
print('HYd'.isupper())      # False
print('HYD'.isupper())      # True
print('9247'.isupper())     # False
print('RAMA  RAO'.isupper())# True
print('+-$'.isupper())      # False
print('HYD123'.isupper())   # True
print('HYD+-$'.isupper())   # True
print(''.isupper())         # False
print('A2#'.isupper())      # True

# islower()
print('hyD'.islower())      # False
print('hyd'.islower())      # True
print('9247'.islower())     # False
print('rama  rao'.islower())# True
print('+-$'.islower())      # False
print('hyd+-$'.islower())   # True
print('abc123'.islower())   # True
print(''.islower())         # False
print('a2#'.islower())      # True

# isalnum()
print('A7$g'.isalnum())     # False
print('HYD'.isalnum())      # True
print('+-$'.isalnum())      # False
print('hyd'.isalnum())      # True
print('hYd'.isalnum())      # True
print('9247'.isalnum())     # True
print(''.isalnum())         # False
print('A7g9'.isalnum())     # True

# isspace()
print('\n  A\t'.isspace())  # False
print('\n  \t'.isspace())   # True
print('\n  7\t'.isspace())  # False
print('\n'.isspace())       # True
print('\n  $\t'.isspace())  # False
print('\t'.isspace())       # True
print(''.isspace())         # False
print(' '.isspace())        # True

# format()
a, b, c = 25, 10.8, 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a, b, c))
# a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a, b, c))
# a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a, b, c))
# a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a, b, c))
# a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x=a, y=b, z=c))
# a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z=a, y=b, x=c))
# a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z=a, y=b, x=c))
# a  :  25  	  b  :  25  	  c  :  25



# Reverse string without slice
s = "Rama Rao"
rev = ''
for i in range(1, len(s) + 1):
    rev += s[-i]
print(rev)  # oaR amaR

s = "Hyd is green city"
words = s.split()
rev = ''
for i in range(1, len(words) + 1):
    rev += words[-i] + ' '
print(rev.strip())  # city green is Hyd

s = "Hyd is green city"
for word in s.split():
    print(word[::-1], end=' ')
# dyH si neerg ytic

print()  # newline

# Sort string alphabetically
s = "RAJESH"
print(''.join(sorted(s)))  # AEHJRS

# Sort string alphabets then digits
s = "Z9K3PA7D51"
alpha = ''.join(sorted([c for c in s if c.isalpha()]))
digit = ''.join(sorted([c for c in s if c.isdigit()]))
print(alpha + digit)  # ADKPZ13579
