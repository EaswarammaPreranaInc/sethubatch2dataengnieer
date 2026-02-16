1.
print(chr(65)) # A print(chr(90)) # Z print(chr(97)) # a print(chr(122)) # z print(chr(48)) print(chr(57)) # 9 print(chr(36)) print(chr(32)) #
# 0
(Unicode for uppercase 'A') (Unicode for uppercase 'Z') (Unicode for lowercase 'a') (Unicode for lowercase 'z') (Unicode for digit '0') (Unicode for digit '9')
# $ (Unicode for dollar sign)
(Unicode for space character)




2.
print(len('Hyd'))
# 3
print(len('Rama Rao'))
# 8
(number of characters) (including space)
print(len('9247'))
# 4
print(len('+-$'))
# 3
print(len(''))
# 0
(empty string)
print(len(' '))
# 1
(space is a character)
print (len('A2#'))
# 3
# The next line will cause an error because 3456 is an int, not a string # print(len(3456)) # TypeError: object of type 'int' has no len()
# Correct way would be to convert the integer to string first:
print(len(str(3456)))
# The syntax below is # print('Sec'. len())
# Correct way to call print (len('Sec'))
# 4
invalid in Python ('.' is not used like this) # SyntaxError
len on a string literal:
# 3





3.
a =
'Rama Rao'
print(a[:7:2]) print(a[:7]) print(a[2:4]) print(a[2:])
# Rm a
# Rama Ra
# ma
# ma Rao
print(a[:4])
# Rama
print(a[::2])
# Rm a
print(a[-6-1]) # ma Ra
print(a[-6:])
# ma Rao
print(a[:-4:-1]) # oaR
print(a[-3:-1])
print(a[-3:])
print(a[:]) print(a[::]) print(a[::-1]) print(a[:: -2]) print(a[-2:-2]) print (a[2:8]) print(a[2:8:-1]) print(a[:-6: -1])
print(a[2:-3])
print(a[1:6:2])
print(a[:-5: -5])
print(a[2: -5])
print (a[2:-5:2])
print(a[:0: -1])
print(a[-5:0:-2])
# Ra
# Rao
# Rama Rao
# Rama Rao # oar am aR
# oRaa # a mR
# ma Rao
#
# oaR a
# ma
# aaR
#0
#m
#
# oaR am
# aa





4.
import sys
argv sys.argv
if len(argv) != 2:
else:
print("Pls send an integer input")
try:
num = int(argv[1]) if num % 2 == 0:
else:
print("Even number")
print("Odd number")
except ValueError:
print("Pls send an integer input")




5.
s = input("Enter any string with alternate character and digit: ")
# Check length of input is even (pairs of char & digit)
if len(s) % 2 != 0:
else:
print("string should have alternate character and digit")
result =
valid = True
for i in range(0, len(s), 2):
char = s[i]
digit = s[i+1]
# Check char is alphabetic or symbol (not digit), and digit is numeric
if not char.isalpha() and not (33 <= ord (char) <= 47 or 58 <= ord (char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126):
# char is neither alphabet nor common symbols (just a generic check for symbol range)
valid = False
break
if not digit.isdigit():
valid = False
break
result += char int(digit)
if valid:
else:
print("Result : ", result)
print("string should have alternate character and digit")




6.
# Input two strings from the user a = input("Enter first string : ") b = input("Enter second string : ")
C =
UT
i
# Result string
= 0 # Index for iteration
# Loop until the end of the shorter string while i<len (a) and i < len(b):
c += a[i] + b[i]
i += 1
# Append remaining characters of the longer string if i < len(a):
c += a[i:]
elif i < len(b): c += b[i:]
print("Result : ", c)



7.
import sys
argv sys.argv
if len(argv) == 1:
else:
print("Pls send number inputs")
inputs = argv[1:]
a = []
try:
for item in inputs:
if item == 'True': a.append(True)
elif item == 'False':
a.append(False)
else:
a.append(float(item))
print("argv ", argv)
print("List 'a' =", a)
average = sum(a) / len(a)
print("Average is:", round(average, 2))
except ValueError:
print("Pls send number inputs")



8.
print('green' in 'Hyd is green city') print('day' in 'Sankar dayal sarma') print('Green' in 'Hyd is green city') print('d is' in 'Hyd is green city') print('dis' in 'Hyd is green city') print('iniv' in 'Srinivas') print('iniv' not in 'Srinivas')
# True
# True
# False # True # False # True
# False




9.
import sys
argv sys.argv
if len(argv) == 1:
else:
print("Pls send number inputs")
inputs = argv[1:]
a = []
all_numbers = True
for item in inputs:
try:
num = float(item)
a.append(num)
except ValueError:
all_numbers = False
break
if not all numbers:
else:
print("Pls don't send number and string inputs together")
print("argv =", argv)
print("List 'a' =", a)
print("Sorted list (ascending):", sorted(a))
print("Sorted list (descending):", sorted(a, reverse=True))



10.
# Input string from user
s = input("Enter any string : ")
even_chars = "" odd_chars = "*
# to hold chars at even indexes # to hold chars at odd indexes
# Loop over all indexes and characters for i in range(len(s)):
if i % 2 == 0:
else:
even_chars += s[i]
odd_chars += s[i]
print("string at even indexes : + even_chars) print("string at odd indexes : " + odd_chars)





11.
s = input("Enter a string: ")
if len(s) < 4:
else:
print("") # empty string
result = s[:2] + s[-2:] print(result)



12.
import sys
argv sys.argv
if len(argv) == 1:
else:
print("Pls send inputs")
inputs = argv[1:]
# Try to convert all inputs to float
all numbers = True all_strings = True
a = []
for item in inputs:
try:
num = float(item) a.append(num)
all_strings = False
except ValueError:
a.append(item)
all_numbers = False
if all numbers:
print (f"argv = {argv}")
print (f"List 'a' = {a}")
print(f"Largest command line input is: {max(a)}")
print (f"max(argv[1:]) = {max(argv[1:])}") # Shows string comparison
print("Issue with max(argv[1:])? ---> Largest string is obtained but not largest number") elif all_strings:
else:
print (f"Largest command line input is: '{max(a)}'")
print("Inputs can not be number and string mixed")





13.
# Program to concatenate two strings swapping their first two characters
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) < 2 or len(str2) < 2:
print("Input should be a min of 2-char string")
else:
# Swap first two characters
# New first string = first two chars of str2 + rest of str1 from index 2 new_str1 = str2[:2] + str1[2:]
-
# New second string first two chars of str1 + rest of str2 from index 2 new_str2 = str1[:2] + str2[2:]
# Concatenate with a space
result = new_str1 + " " + new_str2
print("Result : ", result)




14.
S
input("Enter any string with alternate character and digit : ")
# Validate that input length is even (pairs of char and digit) if len(s) % 2 != 0:
print("Pls enter string with alternate char and digit")
else:
result =
valid = True # Flag to check validity
for i in range(0, len(s), 2):
char = s[i] digits[i+1]
# Validate char is a letter or allowed symbol (not digit) if not char.isalpha():
valid = False
break
# Validate digit is numeric
if not digit.isdigit():
valid = False
break
# Calculate shifted character code
# ord (char) + int(digit)
shifted_code = ord (char) + int(digit)
# If shifted_code goes beyond 'Z' (assuming uppercase letters),
# you may want to wrap or just keep as is - your example leaves 'Z' + 5 as
# chr(90 + 5) = chr(95) = '_', so this fits the example.
result + char + chr(shifted_code)
if valid:
else:
print("Result : ", result)
print("Pls enter string with alternate char and digit")




15.
print (ord('A')) # 65 print (ord('Z')) # 90 print (ord('a')) # 97 print(ord('z')) # 122 print (ord('0')) # 48 print (ord('9')) # 57 print (ord('$')) # 36 print(ord('')) # 32
(Unicode/ASCII for uppercase 'A') (Unicode/ASCII for uppercase 'Z') (Unicode/ASCII for lowercase 'a') (Unicode/ASCII for lowercase 'z') (Unicode/ASCII for digit '0') (Unicode/ASCII for digit '9') (Unicode/ASCII for dollar sign) (Unicode/ASCII for space character)




16.
# Input string from user
s = input("Enter any string: ")
out = "" # To store characters without duplicates
for char in s:
if char not in out:
out += char # Concatenate if char not already in out
print("String without duplicates : ", out)





17.
# Input string
s = input("Enter a string: ")
# Print characters in forward direction with positive indices for i in range(len(s)):
print (f"Character at index {i} : {s[i]}")
print() # Blank line
# Print characters in reverse direction with negative indices for i in range(1, len(s) + 1):
print(f"Character at index {-i} : {s[-i]}")
