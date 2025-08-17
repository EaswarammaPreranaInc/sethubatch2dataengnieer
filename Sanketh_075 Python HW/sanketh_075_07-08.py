#07/08 Homework 
#Largest Command line input
import sys
if len(sys.argv) == 1:
    print("Pls send inputs")
else:
    try:
        a = [float(i) for i in sys.argv[1:]]
        print("Largest command line input :", max(a))
    except ValueError:
        # If all inputs are strings (non-numeric)
        if all(i.isalpha() for i in sys.argv[1:]):
            print("Largest command line input :", max(sys.argv[1:]))
        else:
            print("Inputs can not be number and string")

#Even or Odd Command line input
import sys

if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        n = int(sys.argv[1])
        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Pls send an integer input")

#Average Command line input
import sys

if len(sys.argv) == 1:
    print("Pls send number inputs")
else:
    try:
        a = [float(i) for i in sys.argv[1:]]
        print("Average of command line inputs:", sum(a) / len(a))
    except ValueError:
        print("Pls send number inputs")

#Sort Command line input
import sys

if len(sys.argv) == 1:
    print("Pls send inputs")
else:
    try:
        a = [float(i) for i in sys.argv[1:]]
        print("Ascending order :", sorted(a))
        print("Descending order:", sorted(a, reverse=True))
    except ValueError:
        print("Pls don't send number and string inputs together")

#Swap first ts1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) < 2 or len(s2) < 2:
    print("Input should be a min of 2-char string")
else:
    result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
    print("Result :", result)

#First two and last two characters
s = input("Enter any string: ")

if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])

#Characters in Forward and Reverse order
s = input("Enter any string: ")

for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")

#Characters at even and odd indexes
s = input("Enter any string: ")

even = ""
odd = ""

for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]

print("String at even indexes :", even)
print("String at odd indexes  :", odd)

#Repeat characters by following digit 

s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("String should have alternate character and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] * int(s[i+1])
    print("Result :", out)

#Merge two strings alternatively 
a = input("Enter first string: ")
b = input("Enter second string: ")

c = ""
i = 0
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1

c += a[i:] + b[i:]
print("Result :", c)

#Remove duplicates in characters without set
s = input("Enter any string: ")

out = ""
for ch in s:
    if ch not in out:
        out += ch

print("String without duplicates :", out)

#Alternate character and digit 

s = input("Enter any string with alternate character and digit: ")

if len(s) % 2 != 0 or not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s), 2)):
    print("Pls enter string with alternate char and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        out += s[i] + chr(ord(s[i]) + int(s[i+1]))
    print("Result :", out)
