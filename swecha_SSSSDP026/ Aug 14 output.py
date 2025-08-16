 Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) #3
print(a . count('\n')) #3

 Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15', '36', '48']
print(a)
outputs: 15:36:48

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) 
print(a . split())
print(a . split('green'))
print(a . split(''))
outputs:
[]'Hyd\nis', 'green\tcity']     
['Hyd', 'is','green','city']
['Hyd is '' city']
error

Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))# ['Hyd',  'is',  'green',  'city']
print(a . split())# ['Hyd', 'is', 'green', 'city'] 
print(a . split(' '))# ['Hyd\tis\tgreen\tcity]

Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # 'Hyd', 'is', 'green', 'city'
print(a . split(' '))#'Hyd', '', '', 'is', '', '', 'green', '', '', 'city'

Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # []'www', 'gmail', 'com']

 Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city') 
print(' ' . join(b)) # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))# 10 20 15 25 52 
d = ['www' , 'gmail', 'com']
print('.' . join(d))# www.gmail.com
# e = [15 , 36 , 48]
# print(':' . join(e))# error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # sankarDayalSarma
g = range(5)
print('-' . join(g)) # error

endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13))# False
print(a . endswith(' ' , 3 , 13))# True

 isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha()) # False
print('Hyd$'  . isalpha()) # False
print('9247'  .  isalpha()) # False
print('+-$'    .  isalpha()) # False
print('A2#'  .   isalpha()) #False
print(''  .  isalpha()) # False
print(' '  .  isalpha()) #False

isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit()) # False
print('Hyd' . isdigit()) # False
print('+-$' . isdigit()) # False
print('A2#' . isdigit()) # False
print('' . isdigit()) # False
print(' ' . isdigit()) # False
print(9247 . isdigit()) # False

isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper()) # True
print('+-$' . isupper()) # False
print('HYD123' . isupper()) # True
print('HYD+-$' . isupper()) # True
print('' . isupper()) # False
print('A2#' . isupper()) # True


islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower()) # True
print('+-$' . islower()) # False
print('hyd+-$' . islower()) #  True
print('abc123' . islower())# True
print('' . islower()) # False
print('a2#' . islower()) # True


isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum()) # False
print('hyd' . isalnum()) # True
print('hYd' . isalnum()) # True
print('9247' . isalnum()) # True
print('' . isalnum()) # False
print('A7g9'  . isalnum()) # True


isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace()) #False
print('\n' . isspace()) # True
print('\n  $\t' . isspace()) # False
print('\t' . isspace()) # True
print('' . isspace()) # False
print(' ' . isspace()) # True

Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
#output:
a : 25     b : 10.8    c : Hyd
a  : 25     b : 10.8     c : Hyd
a  : 25     b : 10.8     c : Hyd
a  : Hyd     b : 10.8     c : 25
a  : Hyd     b : Hyd     c : Hyd
a  : Hyd     b : 10.8     c : 25
a  : Hyd     b : Hyd     c : Hyd





