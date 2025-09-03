1.
print('\n A\t'.isspace())
# False → contains alphabet 'A' (non-whitespace)
print('\n \t'.isspace()) # True → contains only whitespace characters (newline, spaces, tab) → contains digit '7' (non-whitespace)
print('\n \t'.isspace()) # False
print('\n'.isspace())
# True
→ contains only newline (whitespace)
print('\n $\t'.isspace()) # False
print('\t'.isspace())
# True
print(''.isspace())
# False
print(' '.isspace())
# True
→ contains special character '$' (non-whitespace)
→ contains only tab (whitespace)
→ empty string (no characters at all)
→ contains only a space (whitespace)




2.
print('Hyd'.isalpha())
# True → all characters are alphabets (H, y, d)
print('Rama Rao'.isalpha()) # False → contains a space, which is not an alphabet
print('Hyd4'.isalpha())
print('Hyd$'.isalpha()) print('9247'.isalpha()) print('+-$'.isalpha()) print('A2#'.isalpha()) print(''.isalpha())
print(' '.isalpha())
# False → contains digit '4'
# False
→ contains special character '$'
# False → all are digits, no alphabets
# False → all are special characters
# False → contains digit '2' and symbol
# False → empty string (no alphabets at all)
# False contains a space, no alphabets
→



3.
print('HYd'.isupper())
# False → contains lowercase 'd'
# True
all alphabets are uppercase
# False
print('HYD'.isupper())
print('9247'.isupper())
print('RAMA RAO'.isupper()) # True # False print('HYD123'.isupper()) # True print('HYD+-$'.isupper()) # True print(''.isupper())
print('+-'.isupper())
print('A2# '.isupper())
# False
# True
→ no alphabets at all
all alphabets are uppercase; spaces are ignored → no alphabets at all
→ all alphabets are uppercase; digits are ignored
→ all alphabets are uppercase; symbols are ignored → empty string (no alphabets at all)
→ 'A' is uppercase; digits/symbols are ignored



4.
a = 'Hyd\nis green\tcity' print(a.split(' ')) print (a.split())
print (a.split('green'))
print(a.split(''))
output:
['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city'] ['Hyd\nis', '\tcity'] ValueError: empty separator




5.
print('A7$g'.isalnum()) # False print('HYD'.isalnum()) # True
→ contains special character '$'
→ all are alphabets (no special chars)
print('+-'.isalnum()) # False → all special characters, no alphabet/digit
print('hyd'.isalnum()) # True print('hYd'.isalnum()) # True print('9247'.isalnum()) # True print(''.isalnum())
→ all are alphabets (lowercase)
all are alphabets (mixed case is allowed)
→ all characters are digits
# False → empty string (no alphabet/digit at all)
print('A7g9'.isalnum()) # True
→ contains only alphabets and digits (no special chars)



6.
a, b, c = 25, 10.8, 'Hyd'
print('a : {} \t b: {} \t_c : {} '.format(a, b, c)) c: Hyd
# a : 25
b: 10.8
# → {} placeholders are filled in order with a, b, c.
print('a {0} \t b: {1} \t c : {2}'.format(a, b, c)) # a : 25
b: 10.8
c: Hyd
# → Numbered placeholders {0}{1}{2} refer to positional arguments.
print('a : {2} \t b {1} :
# a: Hyd
b: 10.8
# → Index 2 → c, Index 1b,
print('a : {2} \t b: {2} # a: Hyd b : Hyd
\t c : {0} .format(a, b, c))
C : 25
Index 0 → a.
\t c : {2} .format(a, b, c)) C: Hyd
# → All placeholders use index 2 → c.
print('a {x} \t b: {y} \t_c : {z}'.format(x-a, y=b, z=c)) # a : 25
b: 10.8
c: Hyd
# → Named placeholders mapped to variables x, y, z.
print('a : {x} \t b {y} :
# a: Hyd
b : 10.8
\t c : {z}'.format(z=a, y=b, x=c))
C : 25
# → x=c ('Hyd'), y=b (10.8), z=a (25).
print('a
# a : 25
{z} \t b: {z} \t c :
b: 25
C : 25
{z}'.format(z=a, y=b, x=c))
# → All placeholders use named variable z which is a=25.




7.
# Take input from user
s = input("Enter any string: ")
# e.g., RAJESH
# sorted() returns a list of characters in alphabetical order sorted_chars = sorted(s)
# join() combines them into a single string result = ''.join(sorted_chars)
print("sorted string:", result)



8.
# Take input from user s = input("Enter a string: ")
if len(s) < 3: result = s
elif s.endswith("ing"): result = s + "ly"
else:
results + "ing"
print(result)




9.
S = 'babble'
first_char
s[0]
# get the first character ('b')
# replace all occurrences of first_char with
s = first_char + s[1:].replace(first_char, '*')
**
print(s)



10.
S = input("Enter any string: ") # e.g., Z9K3PA7D51
# Step 1: Sort the string
sorted_s = sorted(s) # list of characters
# Step 2: Separate alphabets and digits alpha = ''
digit =
for ch in sorted_s:
if ch.isalpha(): alpha += ch
elif ch.isdigit():
digit += ch
# Step 3: Concatenate alphabets first, then digits result = alpha + digit
print("Sorted output:", result)





11.
print('9247'.isdigit()) # True all characters are digits (9, 2, 4, 7) print('92847'.isdigit()) # False → contains the alphabet 'a' print('92$47'.isdigit()) # False → contains special character print('Hyd.isdigit()) print('+-$'.isdigit()) print('A2#.isdigit())
print(''.isdigit()) print(''.isdigit())
print(9247.isdigit())
# False → all characters are alphabets, no digits
# False → all are special characters, no digits
# False
contains alphabet 'A' and special character '#'
# False → empty string (no digits at all)
# False → contains a space, no digits
# ERROR → AttributeError: 'int' object has no attribute 'isdigit'
# Reason: isdigit() works only on strings, not integers → use str(9247).isdigit() instead



12.
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city' # 4
print(a.count('is')) print(a.count('is', 19, 48))
print (a.count('was'))




13.
a = 'Hyd\tis\tgreen\tcity' # There is a tab between the words
print (a.split('\t'))
print (a.split()) print(a.split(' ')) output:
['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']




14.
# Take input from user
expr = input("Enter the expression: ")
# e.g. 123+45+6+789
# Split by '+' and convert each part to integer, then add them numbers = expr.split('+') # ['123', '45', '6', '789']
total = sum(int(num) for num in numbers) # 123 + 45 + 6 + 789
# Print result
print("Sum: ", total)




15.
is
green city' # There are 3 spaces between each word
a = 'Hyd print(a.split()) print(a.split(' '))
output:
['Hyd', 'is', 'green', 'city']
['Hyd',
..
'is',
'green',
'', 'city']




16.
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
while (index := a.find('is', (index + 1) if 'index' in locals() else 0)) != -1:
print(index)
print('End')



17.
print('hyD'.islower())
# False → contains uppercase 'D'
print('hyd'.islower())
print('9247'.islower())
# True → all alphabets are lowercase
# False → no alphabets at all
print('rama rao'.islower()) # True
all alphabets are lowercase; spaces are ignored
print('+-$'.islower())
# False → no alphabets at all
print('hyd+-$'.islower()) # True → all alphabets are lowercase; symbols are ignored
print('abc123'.islower()) # True
→ all alphabets are lowercase; digits are ignored
print(''.islower())
# False
→ empty string (no alphabets at all)
print("
print('a2#' .islower())
# True
→ 'a' is lowercase; digits/symbols are ignored





18.
a = 'www.gmail.com' print(a.split('.'))
output:
['www', 'gmail', 'com']




19.
a = 'Hyd is green city'
print(a.endswith('city')) print(a.endswith("town"))
print(a.endswith('green', 3, 12)) print(a.endswith('green', 3, 13)) print(a.endswith('', 3, 13))
# True → String ends with "city"
# False → String does not end with "town"
# True → a[3:12] = " is green" → ends with "green"
# False → a[3:13] = " is green" (note trailing space) does NOT end with "green"
# True → a[3:13] = is green → ends with a space





20.
# Take input from the user
s = input("Enter any sentence : ") # e.g. "Hyd is green city"
result =
# to store the final output
# For-each word in the split list
for word in s.split():
result += word[::-1] + ' ' # reverse the word and add a space
# Remove extra trailing space and print print("Reversed each word:", result.strip())




21.
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index= a.rfind('is')
while index != -1:
print(index)
# start from the rightmost occurrence
# next search ends just before the current match index= a.rfind('is', 0, index)
print('End')



22.
a =
'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
start = 0
while True:
try:
index = a.index('is', start) # same syntax as find() print(index)
start = index + 1 # move to next position # when 'is' is not found
except ValueError:
break
print('End')




23.
# Take input
s = input("Enter any string: ")
rev =
length = len(s)
# to store reversed version
# Loop from last character to first for i in range(1, length + 1):
rev += s[-i]
# accessing characters from −1, −2,
print("Reverse String :", rev)




24.
# Take sentence input
s = input("Enter any sentence : ")
# Step 1: Convert sentence into list of words
b = s.split()
# e.g. ['Hyd', 'is', 'green', 'city']
c = '' # to store reversed sentence
# Step 2: Append each word from end to start for i in range(1, len(b) + 1):
c += b[i] +
# Step 3: Print without the extra trailing space print("Reversed word order:", c.strip())




25.
a = 15:36:48' print(a.split(':'))
print(a) output:
['15', '36', '48']
15:36:48




26.
# Take input
S
=
input("Enter any sentence: ")
# Step 1: Split into words list
b = s.split()
# e.g., ['Hyd', 'is', 'green', 'city']
C =
# to store reversed word order
# Step 2: Loop through list from last to first using negative index for i in range(1, len(b) + 1):
c += b[-i] +
# Step 3: Print result (strip to remove extra space at end) print("Reversed word order:", c.strip())




27.
a = ['15', '36', '48']
print(':'.join(a))
b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))
c = {'10' print(','.join(c))
'20' '15' '25'
'52'}
d = ['www', 'gmail', 'com'] print('.'.join(d))
e = [15, 36, 48]
print(':'.join(e))
f = ['Sankar', 'Dayal', 'Sarma'] print(''.join(f))
g = range(5) print('-'.join(g))
# 15:36:48
# Hyd is green city
# Order not fixed, e.g. 25,15,20,10,52
# www.gmail.com
# TypeError: sequence item 0: expected str instance, int found
# SankarDayalSarma
# TypeError: sequence item 0: expected str instance, int found





28.
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
index = a.rindex('is') # first search from the rightmost match while True:
print(index)
# search again, ending just before the current match index= a.rindex('is', 0, index)
except ValueError:
print('End')
