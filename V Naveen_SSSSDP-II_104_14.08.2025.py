
#1.Modify   program  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

while (index := a.find('is', (index + 1) if 'index' in locals() else 0)) != -1:
    print(index)

print('End')

#2.Modify  the   program  with  index()  method


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = -1
while True:
    try:
        index = a.index('is', index + 1)
        print(index)
    except ValueError:
        break

print('End')


#3 . Modify  following  program  with  rfind()  method


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')  # find last occurrence first
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)  # search again to the left
print('End')


#4. Modify  following  program  with  rindex()  method


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = len(a)  # start from the end
while True:
    try:
        index = a.rindex('is', 0, index)  # search backwards
        print(index)
    except ValueError:
        break

print('End')


#5
# count() method demo program

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'

print(a.count('is'))            # 4 
print(a.count('is', 19, 48))    # 2  between index 19 and 47
print(a.count('was'))           # 0 


#6  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))     #3
print(a . count('\t'))    #3
print(a . count('\n'))    #3


#7. replace every first character occurence with *
s = 'babble'
st = s[0]             
result = st + s[1:].replace(st, '*')
print(result)

#8
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))  #['15', '36', '48']
print(a)               #'15:36:48'


#9
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))      #['Hyd\nis', 'green\tcity']
print(a . split())         #['Hyd', 'is', 'green', 'city']
print(a . split('green'))  #['Hyd\nis ', '\tcity']
print(a . split(''))       #Error

#10
# Find  outputs  (Home  work)
a = 'Hyd        is        green        city' #  There  is  tab  between  the  words
print(a . split('\t'))   #['Hyd', 'is', 'green', 'city']
print(a . split())       #['Hyd', 'is', 'green', 'city']
print(a . split(' '))    #['Hyd\tis\tgreen\tcity']

#11 Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())       #['Hyd', 'is', 'green', 'city']
print(a . split(' '))   #['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


#12
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))   #['www', 'gmail', 'com']

#13
# Program to evaluate an expression containing only + symbols

expr = input("Enter the expression: ")   # e.g. 123+45+6+789

numbers = expr.split('+')
total = sum(int(num) for num in numbers)
print("Sum:", total)


#14
a = ['15' , '36' , '48']
print(':' . join(a))        # 15:36:48

b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))        # Hyd is green city

c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))        # 15,20,25,10,52  

d = ['www' , 'gmail', 'com']
print('.' . join(d))        # www.gmail.com

e = [15 , 36 , 48]
print(':' . join(e))        #  Error


#15
a = 'Hyd is green city'

print(a.endswith('city'))            # True  

print(a.endswith('town'))            # False  

print(a.endswith('green', 3, 12))    # False  

print(a.endswith('green', 3, 13))    # True  

print(a.endswith(' ', 3, 13))        # False  

f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))         # SankarDayalSarma

g = range(5)
print('-' . join(g))        # Error:


#16
s = input("Enter a string: ")

if len(s) < 3:
    result = s
elif s.endswith('ing'):
    result = s + 'ly'
else:
    result = s + 'ing'

print("Output:", result)

#17

print('Hyd'.isalpha())        # True  

print('Rama  Rao'.isalpha())  # False  

print('Hyd4'.isalpha())       # False  

print('Hyd$'.isalpha())       # False  


print('9247'.isalpha())       # False  

print('+-$'.isalpha())        # False  


print('A2#'.isalpha())        # False  


print(''.isalpha())           # False  


print(' '.isalpha())          # False  





#18.

print('9247'.isdigit())       # True  

print('92a47'.isdigit())      # False  

print('92$47'.isdigit())      # False  

print('Hyd'.isdigit())        # False  

print('+-$'.isdigit())        # False  

print('A2#'.isdigit())        # False  

print(''.isdigit())           # False  

print(' '.isdigit())          # False  

print(9247.isdigit())         #  ERROR  






#19
print('HYd'.isupper())       # False  

print('HYD'.isupper())       # True  

print('9247'.isupper())      # False  

print('RAMA  RAO'.isupper()) # True  

print('+-$'.isupper())       # False  

print('HYD123'.isupper())    # True  

print('HYD+-$'.isupper())    # True  

print(''.isupper())          # False  

print('A2#'.isupper())       # True  


#20
print('hyD'.islower())       # False  

print('hyd'.islower())       # True  

print('9247'.islower())      # False  

print('rama  rao'.islower()) # True  

print('+-$'.islower())       # False  

print('hyd+-$'.islower())    # True  

print('abc123'.islower())    # True  

print(''.islower())          # False  

print('a2#'.islower())       # True  


#21
print('A7$g'.isalnum())     # False  

print('HYD'.isalnum())      # True  

print('+-$'.isalnum())      # False  

print('hyd'.isalnum())      # True  

print('hYd'.isalnum())      # True  

print('9247'.isalnum())     # True  

print(''.isalnum())         # False  

print('A7g9'.isalnum())     # True  


#22
print('\n  A\t'.isspace())   # False  

print('\n  \t'.isspace())    # True  

print('\n  7\t'.isspace())   # False  

print('\n'.isspace())        # True  

print('\n  $\t'.isspace())   # False  

print('\t'.isspace())        # True  

print(''.isspace())          # False  

print(' '.isspace())         # True  





#23

a , b , c = 25 , 10.8 , 'Hyd'

print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a , b , c))
# a  :  25          b  :  10.8          c  :  Hyd

print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a , b , c))
# a  :  25          b  :  10.8          c  :  Hyd

print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a , b , c))
# a  :  Hyd          b  :  10.8          c  :  25

print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a , b , c))
# a  :  Hyd          b  :  Hyd          c  :  Hyd

print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x = a , y = b , z = c))
# a  :  25          b  :  10.8          c  :  Hyd

print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z = a , y = b , x = c))
# a  :  Hyd          b  :  10.8          c  :  25

print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z = a , y = b , x = c))
# a  :  25          b  :  25          c  :  25





#24
# Program to determine the type of a user input character

ch = input("Enter any character: ")

if ch.isalnum():  #
    print("Alphanumeric character")
    if ch.isalpha():
        print("Alphabet character")
        if ch.isupper():
            print("Upper case alphabet")
        elif ch.islower():
            print("Lower case alphabet")
    elif ch.isdigit():
        print("Digit character")

elif ch.isspace():  
    print("White space")

else:  
    print("Special character")

#25. Write  a  program  to  reverse  a  string  without  slice

1
st=input("enter the string:")
st1=''
for i in range(len(st)):
    st1=st[i]+st1
print(st1)

#26. Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice


st=input("enter the string:")
st1=''
for i in st:
    for j in i:
        st1=i+st1
print(st1)

#27. Write  a  program  to  reverse  each  word  of  the  sentence


st = input("Enter the string: ")
st1 = ''

for word in st.split():      
    st1 += word[::-1] + ' '   
print(st1.strip())




#28. Write  a  program  to  sort  string  in  alphabetical  order

st = input("Enter the string: ")
sorted_st = ''.join(sorted(st))
print(sorted_st)


#29. Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order


st = input("Enter the string: ")   # Example: Z9K3PA7D51

# Step 1: Sort entire string
sorted_str = sorted(st) 

# Step 2: Separate alphabets and digits
alpha = ''
digit = ''
for ch in sorted_str:
    if ch.isalpha():
        alpha += ch
    else:
        digit += ch


result = alpha + digit
print(result)  # Output: ADKPZ13579