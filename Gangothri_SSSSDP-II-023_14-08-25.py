'''Modify  following  program  with  walrus  operator
Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')
'''output:
4
23
42
46
End'''

'''index()  method  demo  program
Modify  the  following  program  with  index()  method'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index1 = a . index('is')
while  index1 != -1:
	print(index1)
	index1 = a . index('is' , index1 + 1)
print('End')
'''output:
4
23
42
46
End'''
'''(Home  work)
Modify  following  program  with  rfind()  method'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
#rfind()  method  demo  program
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index1 = a . rfind('is')
while  index1 != -1:
    print(index1)
    index1 = a . rfind('is' ,0, index1)
print('End')
'''output:
46
42
23
4
End'''
'''  (Home  work)
rindex()   method  demo  program
#Modify  following  program  with  rindex()  method
Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a.rindex('is')  # start from the right
    while True:
        print(index)
        index = a.rindex('is', 0, index)  # search to the left of current index
except ValueError:
    print('End')

'''output:
46
42
23
4
End '''   

# count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3'''

#Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
#Let  input  be  'babble'
#What  is  the  output ?  ---> ba**le
s = input("Enter a string: ")
first_char = s[0]
result = first_char + s[1:].replace(first_char, '*')
print(result)
'''output:
Enter a string: abbbaabaa
abbb*b*'''
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#[15,36,48] 
print(a)#15:36:48   

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split('green'))#['Hyd\nis ', '\tcity']
print(a . split(''))#ValueError: empty separator

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd', 'is', 'green', 'city']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There are 3 spaces between  the words
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a.split(''))#ValueError: empty separator

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a.split('.'))#['www', 'gmail', 'com']

#Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols.Let  input  be  123+45+6+789.Print  the  sum  result
e=input("Enter the Expression")
s=e.split('+')
print(s)
total=0
for i in s:
      total+=int(i)
print("Sum=",total)      
'''output:
Enter the Expression123+89+90+56+157
['123', '89', '90', '56', '157']
Sum= 515'''
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#25,52,20,10,15
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))#TypeError:  expected str instance, int found
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma
g = range(5)
print('-' . join(g))#TypeError:  expected str instance, int found

# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

#Write  a  program  to  append  'ing'  to  input  string.Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.Leave  the  string  unchanged  if  string  has  lessthan  three  characters
#1) What  is  the  output  if  input  is  'interest' ?  ---> interesting
#2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly
#3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
a=input("Enter a string: ")
if(len(a)<3):
    result=a
    print(result)
elif a.endswith("ing"):
      result=a+"ly"   
      print(result)
else:   
       print(a+"ing")
'''output:
Enter a string: interest
interesting  
Enter a string: hi
hi
Enter a string: interesting
interestingly'''
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

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())#False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#False
print(' ' . isdigit())#False
print(9247 . isdigit())#AttributeError: 'int' object has no attribute 'isdigit'

# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper())#False
print('HYD123' . isupper())#True
print('HYD+-$' . isupper())#True
print('' . isupper())#False
print('A2#' . isupper())#True

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


# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())#False
print('hyd' . isalnum())#True
print('hYd' . isalnum())#True
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
print(' ' . isspace())#True

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a ,y=b,x=c))
'''output:
a  :  25  	  b  :  10.8  	  c  :  Hyd  
a  :  25  	  b  :  10.8  	  c  :  Hyd  
a  :  Hyd  	  b  :  10.8  	  c  :  25  
a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd  
a  :  25  	  b  :  10.8  	  c  :  Hyd  
a  :  Hyd  	  b  :  10.8  	  c  :  25  
a  :  25  	  b  :  25  	  c  :  25'''

'''Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet
2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet
3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character
4) What  is  the  output  if  input  is  '$' ?  ---> Special  character
5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space
6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space
7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space'''
ch = input("Enter a character: ")
if ch.isspace():
    print("White space")

# Check for alphanumeric characters
elif ch.isalnum():
    print("Alphanumeric character")    
    if ch.isalpha():  # Alphabet check
        print("Alphabet character")        
        if ch.isupper():
            print("Upper case alphabet")
        elif ch.islower():
            print("Lower case alphabet")            
    elif ch.isdigit():
        print("Digit character")
# If not alphanumeric or whitespace, then it's special
else:
    print("Special character")
'''output:
Enter a character: 4
Alphanumeric character
Digit character
Enter a character: A
Alphanumeric character
Alphabet character
Upper case alphabe
Enter a character: a
Alphanumeric character
Alphabet character
Lower case alphabet
Enter a character: $
Special character'''
#Write  a  program  to  reverse  a  string  without  slice
a = input("Enter a string: ")
b = ''
for i in range(1, len(a) + 1):
    b = b + a[-i]   
print("Reversed string:", b)
'''output:
Enter a string: Gangothri
Reversed string: irhtognaG'''

#Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
a = input("Enter a sentence: ")
b = a.split()  
c = ''
for i in range(1, len(b) + 1):
    c = c + b[-i] + ' '
print(c.strip()) 
'''output:
Enter a sentence: Hyd is green city
city green is Hyd'''

#Write  a  program  to  reverse  each  word  of  the  sentence
a = input("Enter a sentence: ")
result = ''
for word in a.split():
    result += word[::-1] + ' '
print(result.strip())
'''output:
Enter a sentence: Butterfly is beautiful
ylfrettuB si lufituaeb'''

#Write  a  program  to  sort  string  in  alphabetical  order
a = input("Enter a string: ")
sorted_chars = sorted(a)
result = ''.join(sorted_chars)
print(result)
'''output:
Enter a string: JHANSI
AHIJNS'''

#Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
a = input("Enter a string: ")
sorted_chars = sorted(a)
alpha = ''
digit = ''
for ch in sorted_chars:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
result = alpha + digit
print(result)
'''OUTPUT:
Enter a string: AGHKROUP77649053
AGHKOPRU03456779'''