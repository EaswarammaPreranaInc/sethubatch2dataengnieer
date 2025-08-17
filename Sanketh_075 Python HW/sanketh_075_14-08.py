'''
#find method with Walrus operator
a= "Hyd is green city. hitec city is beautiful. secundrabad is bigger the namopally"

whle (index := a.find('is',(index + 1)if 'index' in locals() else 0)) !=1:
    print(index)
print('End')

#Index method to find string
a= "Hyd is green city. hitec city is beautiful. secundrabad is bigger the namopally"

try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is',index+1)
except ValueError:
    print('End')

#rfind method
a= "Hyd is green city. hitec city is beautiful. secundrabad is bigger the namopally"

index= a.rfind('is')
while index !=-1:
    print(index)
    index = a.rfind('is',0,index)
print('End')

#rindex method
a= "Hyd is green city. hitec city is beautiful. secundrabad is bigger the namopally"

try:
    index = a.rindex('is')
    while True:
        print(index)
        index=a.rindex('is',0,index)
except ValueError:
    print('End')

#replace every occurance of first character except first
s= input("Enter a string: ")
first_char= s[0]
result= first_char + s[1:].replace(first_char, '*')
print("result:", result)


#Evaluate expression with + operator only
number = input("enter numbers: ")
summ = number.split('+')
total = 0
for n in summ:
    total += int(n)
print("total:",total)

#Append 'ing' to 'ly'
s=input("enter a string:")
if len(s) < 3:
    print("write something more than 3 letters")
elif s.endswith("ing"):
    print(s + 'ly')
else:
    print(s + 'ing')

#Reverse of string without using slice
s = input("Enter a string:")
rev=''
for i in range(1,len(s)+1):
    rev += s[-i]
print("Reverse String:",rev)

#Reverse order of words without slice
s = input("enter a sentence:")
words = s.split()
rev_sentence = ''
for i in range(1,len(s)+1):
    rev_sentence += words[-i]+''
print(rev_sentence.strip())

#Reverse each word in sentence
s = input("enter a sentence:")
for word in s.split():
    print(word[::-1],end='')

#sort string alphabetically
s=input("enter a sentence:")
sorted_str=''.join(sorted(s))
print(sorted_str)

#sort strings with alphabets first , digits next
s = input("Enter string:")
sorted_s = sorted(s)
alpha=''
digit=''
fro ch in sorted_s:
    if ch.alpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
print(alpha + digit)
'''
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a) #['15:36:48']
# Find  outputs  (Home  work)
#a = 'Hyd\nis green\tcity'
#print(a . split(' '))
#print(a . split())
#print(a . split('green'))
#print(a . split(''))
# Find  outputs  (Home  work)
#a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
#print(a . split('\t'))
#print(a . split())
#print(a . split(' '))
# Find  outputs (Home  work)
#a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
#print(a . split())
#print(a . split(' '))
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
#print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))
d = ['www' , 'gmail', 'com']
print('.' . join(d))
e = [15 , 36 , 48]
#print(':' . join(e))
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g = range(5)
#print('-' . join(g))
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha())
print('Hyd$'  . isalpha())
print('9247'  .  isalpha())
print('+-$'    .  isalpha())
print('A2#'  .   isalpha())
print(''  .  isalpha())
print(' '  .  isalpha())



'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  non-alphabet(i.e. digit (or) special  character)
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit())
print(' ' . isdigit())
#print(9247 . isdigit()) #error 


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper()) #False
print('HYD123' . isupper()) #True
print('HYD+-$' . isupper()) #True
print('' . isupper()) #False
print('A2#' . isupper()) #True


'''
isupper()  method
----------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  lowercase  alphabet
																								(or)
															                  When  there  are  no  uppercase  alphabets  in  the  string

2) When  does  it  return  True ?  ---> When  there  are  no  lowercase  alphabets  in  the  string
																						and
															at  least  one  character  is  an  uppercase  alphabet
'''
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())  #True
print('+-$' . islower()) #False 
print('hyd+-$' . islower()) #True
print('abc123' . islower()) #True
print('' . islower())#False
print('a2#' . islower()) #True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			  When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and

                                                                                                                             at  least  one  character  is  an  lowercase  alphabet
'''
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum()) #False
print('hyd' . isalnum()) #True
print('hYd' . isalnum()) #True
print('9247' . isalnum()) #True
print('' . isalnum()) #False
print('A7g9'  . isalnum()) #True


'''
isalnum()  method
----------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  speical  character
																						(or)
															 when  there  are  no  alphabets  and  digits

2) When  does  it  return  True ?  ---> When  there  are  no  special  characters  in  the  string
																						and
															 at  least  one  char  should  be  alphabet  (or)  digit

3) What  is  isalpha()  +  isdigit()  called ?  ---> isalnum()
'''
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())#False
print('\n' . isspace()) #True
print('\n  $\t' . isspace()) #false
print('\t' . isspace()) #True
print('' . isspace()) #False
print(' ' . isspace()) #False


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a:25 b:10.8 c=''Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))# 
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
