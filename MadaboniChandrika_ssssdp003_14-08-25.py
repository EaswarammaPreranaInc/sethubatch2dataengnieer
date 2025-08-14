

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while  (index := a.find('is', index + 1)) != -1:
	print(index)
print('End')


#second program
print()
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
start=0
try:
    while True:
        idx = a.index('is', start)
        print(idx)
        start = idx + 1
except ValueError:
    print('End')

#third program
print()
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index !=-1:
	print(index)
	index = a . rfind('is' ,0, index)
print('End')


#fourth program
print()
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a.rindex('is')
    while True:
        print(index)
        index = a.rindex('is',0, index)
except ValueError:
    print('End')


#fifth program
print()
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0

#sixth program
print()
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3

#seventh program
print()
a=input("enter any string: ")
first_char=a[0]
result=first_char
for i in a[1:]:
    if i== first_char:
        result += '*'
    else:
        result += i
print("modified string is:", result)

#eighth program
print()
a = '15:36:48'
print(a . split(':'))
print(a)#['15', '36', '48']

#ninth program
print()
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split('is'))#['Hyd\n', ' green\tcity']
print(a . split('green'))#['Hyd\nis ', ' city']
print(a.split(''))#['H', 'y', 'd', '\n', 'i', 's', ' ', 'g', 'r', 'e', 'e', 'n', '\t', 'c', 'i', 't', 'y']

#tenth program
print()
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))# ['Hyd', 'is', 'green', 'city']
print(a . split())# ['Hyd', 'is', 'green', 'city']
print(a.split(' '))#['Hyd' 'is' 'green' 'city']

#eleventh program
print()
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())# ['Hyd','is','green','city']
print(a . split(' '))#['Hyd', 'is', 'green', 'city']

#twelfth program
print()
a = 'www.gmail.com'
print(a.split('.'))# ['www', 'gmail', 'com']

      
#thirteenth program
print()
a=input("enter an expression: ")
parts=a.split('+')
total=0
for part in parts:
    total+= int(part)
print("Sum result:", total)


#14th program
print()
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#15:36:48
f = ['Sankar' , 'Dayal' , 'Sarma']
#print('' . join(f))#sankarDayalSarma
g = range(5)
#print('-' . join(g))


#15th program
print()
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#false
#print(a . endswith(' ' , 3 , 13)


#16th program
print()
a=input("enter any string:")
if len(a)<3:
    result=a
elif a.endswith('ing'):
    result=a+'ly'
else:
    result=a+'ing'
print("modified string:",result)


#17th program
print()
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha())#False
print('Hyd$'  . isalpha())#False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())#False
print(' '  .  isalpha())#False


#18th program
print()
print('9247' . isdigit())# True
print('92a47' . isdigit())# False
print('92$47' . isdigit())#False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#False
print(' ' . isdigit())#False
#print(9247 . isdigit())

#19th program
print()
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper()) #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper())#False
print('HYD123' . isupper())#True
print('HYD+-$' . isupper())#True
print('' . isupper())#False
print('A2#' . isupper())#True

#20th program
print()
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#True

#21th program
print()
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())#False
print('hyd' . isalnum())#True
print('hYd' . isalnum())#True
print('9247' . isalnum())#True
print('' . isalnum())#False
print('A7g9'  . isalnum())#True


#22nd program
print()
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())#False
print('\t' . isspace())#True
print('' . isspace())#True
print(' ' . isspace())#True


#23rd program
print()
a=input("enter any input:")
if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Digit")
elif a.isspace():
    print("white space")
else:
    print("special char")


#24th program
print()
a=input("enter any string:")
b=""
for i in a:
    b=i+b
print("reversed string:",b)


#25th program
print()
a=input("enter any string:")
print(sorted(a))


#26th program
print()
a = input("Enter any string: ")
alphabets = ""
digits = ""
for char in a:
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        digits += char

sorted_alphabets = "".join(sorted(alphabets))
sorted_digits = "".join(sorted(digits))

print("Sorted string:", sorted_alphabets + sorted_digits)




















