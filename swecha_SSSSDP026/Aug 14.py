'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')



'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.index('is')  
    while True:
        print(index)
        index = a.index('is', index + 1)  
except ValueError:
    print('End')

4
23
42
46
End

'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' ,index + 1 )
print('End')


'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->   Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1
														                  i.e.  left  to  right

4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2

5) What  is  the  issue  with  two  arguments ?  --->  Method  searches  from  left  to  right  even  though  it  is  rfind()  method

6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  --->  +ve  index  even  though  search  is  from  right  to  left

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')  # Find from right to left
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)  # Search again to the left of the previous index
print('End')
46
42
23
4
End


'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''

Demo of rindex() method with try and except

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.rindex('is')  # Find last occurrence first
    while index != -1:
        print(index)
        # Find the next occurrence moving backwards
        index = a.rindex('is', 0, index)
except ValueError:
    # When substring is not found, this block runs
    print('No more occurrences found.')

print('End')

# 46
# 42
# 23
# 4
# No more occurrences found.
# End


'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le

s = 'babble'
first_char = s[0]
rest = s[1:] . replace(first_char, '*')
result = first_char + rest
print(result)

ba**le

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''
a = input("enter expression:")
numbers = a.split('+')
total = 0
for num in numbers:
   total += int(num)
   print("sum =",total)

enter expression:123+45+6+789
sum = 123
sum = 168
sum = 174
sum = 963



Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''
a = input("enter a word:")
if len(a) < 3:
    result = a
elif a.endswith("ing"):
    result = a + "ly"
else:
    result = a + "ing"
print(result)        

enter a word:interest
interesting

enter a word:interesting
interestingly

enter a word:hi
hi


'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''
Take a single character input from the user
char = input("Enter a single character: ")

if char.isalnum():  
    print("Alphanumeric character")
    if char.isalpha():  # Check if it is alphabet
        print("Alphabet character")
        if char.isupper():  # Check uppercase
            print("Upper case alphabet")
        else:  # If not uppercase, it must be lowercase
            print("Lower case alphabet")
    else:  # If not alphabet, it must be a digit
        print("Digit character")
elif char.isspace(): 
    print("White space")
else:  
    print("Special character")

Enter a single character: A
Alphanumeric character
Alphabet character
Upper case alphabet

Enter a single character: a
Alphanumeric character
Alphabet character
Lower case alphabet

Enter a single character: $
Special character


'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'
     2       'y'             'd' + 'y' = 'dy'
     3       'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''
a = input("Enter a string: ")
b = ''
for i in range(1, len(a)+1):
    b = b + a[-i]  
print("Reversed string:", b)

Enter a string: Hyd
Reversed string: dyH

Enter a string: Rama Rao
Reversed string: oaR amaR


'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
   1        'city'         '' + 'city' + ' '=  'city '
   2        'green'     'city ' + 'green' + ' ' = 'city green '
   3        'is'            'city green ' + 'is' + ' ' =  'city green is '
   4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ''
for i in range(1, len(words) + 1):
    reversed_sentence += words[-i] + ' '
reversed_sentence = reversed_sentence.strip()
print("'" + reversed_sentence + "'")

Enter a sentence: Hyd  is  green  city
'city green is Hyd'

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
a = input("enter a sentence:")
b = a.split()
c = ''

for word in b:
    c = c + word[::-1] + " "

print(c.strip())  

enter a sentence:Hyd is green city
dyH si neerg ytic


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
s = "RAJESH"
char = list(s)
char.sort()
result = ''.join(char)
print(result)

AEHJRS


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
s = "Z9K3PA7D51"
sorted_s = sorted(s)
alpha = ''.join(ch for ch in sorted_s if ch.isalpha())
digit = ''.join(ch for ch in sorted_s if ch.isdigit())
result = alpha + digit
print(result)  # Output: ADKPZ13579
