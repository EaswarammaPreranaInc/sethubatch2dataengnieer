# 1. Print Numbers 0–9 (while loop) and 0–20 (for loop) using `count`

from itertools import count

c1 = count()
print('While loop')
while True:
    x = next(c1)
    if x > 9:
        break
    print(x)

print('For loop')
c2 = count()
for x in c2:
    if x > 20:
        break
    print(x)

c3 = count()
print('Element :', next(c3))  # 0

# WARNING: The following will never end!
# c4 = count()
# print(*c4)  # Infinite output!

# Output: 0 to 9 (while), 0 to 20 (for), next(c3) = 0.





# 2. Demonstrating `count` with different step values

from itertools import count

def disp(cnt):
    for i in range(4):
        print(next(cnt), end='\t')
    print()

a = count(start=10)
disp(a)     # 10 11 12 13

b = count(start=10, step=5)
disp(b)     # 10 15 20 25

c = count(start=10, step=-2.5)
disp(c)     # 10.0 7.5 5.0 2.5

d = count()
disp(d)     # 0 1 2 3





# 3. Zip and Count: Tricky Interactions

from itertools import count

cnt = count()
lst = [10, 20, 15, 18]
z1 = zip(cnt, lst)
print('while loop')
while True:
    try:
        print(next(z1))
    except:
        break

z2 = zip(cnt, lst)
print('for loop')
for x in z2:
    print(x)

z3 = zip(cnt, lst)
print('Next element:', next(z3))
print('*z3:', *z3)

z4 = zip(cnt, lst)
print('Next element:', next(z4))
'''
- Output:
  - while loop: (0,10) (1,20) (2,15) (3,18)
  - for loop: (4,10) (5,20) (6,15) (7,18)
  - Next element: (8,10)
  - *z3: (9,20) (10,15) (11,18)
  - Next element: (12,10)
'''



# 4. Using `zip_longest` vs `zip`

from itertools import zip_longest
import time

def disp(z):
    while True:
        try:
            print(next(z))
            time.sleep(1)
        except:
            break

lst = [10, 20, 30, 40]
z1 = zip(range(7), lst)
print(type(z1))
disp(z1)  # (0,10) (1,20) (2,30) (3,40)

z2 = zip_longest(range(7), lst)
print(type(z2))
disp(z2)  # Fills missing with None: (4,None) (5,None) (6,None)





# 5. Demonstrating `cycle`

from itertools import cycle
import time

lst = [10, 20, 30, 40]
c = cycle(lst)
print(type(c))
while True:
    print(next(c))
    time.sleep(1)

# Infinite cycle through [10,20,30,40,...].






# 6. Demonstrating `repeat`

from itertools import repeat
import time

r = repeat(25, times=3)
print('1st repeat object')
while True:
    try:
        print(next(r))
        time.sleep(1)
    except:
        break

print('2nd repeat object')
r = repeat('Hyd')
while True:
    print(next(r))
    time.sleep(1)

# First: 25 25 25; Second: 'Hyd' forever.





# 7. Map and Pow with Range/Repeat

from itertools import repeat
import time

m = map(pow, range(10), range(2, 3))
while True:
    try:
        print(next(m))
        time.sleep(1)
    except:
        break
# Only one result: pow(0,2)=0, then input exhausted.

m = map(pow, range(10), range(2))
while True:
    try:
        print(next(m))
        time.sleep(1)
    except:
        break
# pow(0, 0)=1, pow(1, 1)=1, then input exhausted.

m = map(pow, repeat(2), range(10))
while True:
    try:
        print(next(m))
        time.sleep(1)
    except:
        break
# pow(2,0)=1; pow(2,1)=2; pow(2,2)=4;...pow(2,9)=512






# 8. Combinations and Permutations

import time
from itertools import combinations, permutations

def disp(itr):
    while True:
        try:
            print(next(itr))
            time.sleep(1)
        except:
            break

lst = ['A', 'B', 'C', 'D']
c = combinations(lst, 3)
print('Different Combinations')
disp(c)
# ('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')

print('Different Permutations')
p = permutations(lst, 3)
disp(p)
# All 24 arrangements of length 3 from 4 items





# 9. Print File Pagewise - For loop

import os
def disp(f):
    count = 0
    for line in f:
        print(line, end='')
        count += 1
        if count % 20 == 0:
            os.system('pause')
# End

fname = input('Enter filename: ')
f = open(fname, 'r')
disp(f)
f.close()





# 10. Print File Pagewise - Using `readlines()`

def disp(f):
    lines = f.readlines()
    for i in range(0, len(lines), 20):
        page = lines[i:i+20]
        for line in page:
            print(line, end='')
        if i + 20 < len(lines):
            input('Press Enter for next page...')
# End

fname = input('Enter filename: ')
f = open(fname, 'r')
disp(f)
f.close()






# 11. Copy Contents from File1 to File2

def copy(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'w') as f2:
        for line in f1:
            f2.write(line)
# Usage: copy('file1.txt', 'file2.txt')






# 12. Append Data from File1 to File2

with open('file1.txt', 'r') as f1, open('file2.txt', 'a') as f2:
    for line in f1:
        f2.write(line)
# File2 is opened in append mode.






# 13. Return Average of Numbers in File

def avg(f):
    sum_, ctr = 0, 0
    for line in f:
        try:
            val = eval(line.strip())
            if isinstance(val, (int, float, bool)):
                sum_ += val
                ctr += 1
        except:
            pass
    return sum_ / ctr if ctr else 0
# Usage:
fname = input('Enter filename: ')
f = open(fname)
print('Average:', avg(f))
f.close()






# 14. Merge Two Files to Form a New One

import os

def merge_two_files(fname1, fname2, fname3):
    exist1 = os.path.exists(fname1)
    exist2 = os.path.exists(fname2)
    if exist1 and exist2:
        with open(fname1) as f1, open(fname2) as f2, open(fname3, 'w') as f3:
            f3.writelines(f1.readlines())
            f3.writelines(f2.readlines())
        print(f'{fname1} and {fname2} are merged to form {fname3}')
    elif exist1:
        with open(fname1) as f1, open(fname3, 'w') as f3:
            f3.writelines(f1.readlines())
        print(f'{fname1} is copied to {fname3}')
    elif exist2:
        with open(fname2) as f2, open(fname3, 'w') as f3:
            f3.writelines(f2.readlines())
        print(f'{fname2} is copied to {fname3}')
    else:
        print('Both the files are not existing.')
        if os.path.exists(fname3):
            os.remove(fname3)






# 15. Count Lines, Chars, Words, Vowels, etc.

def count_all(f):
    data = f.read()
    a = []
    a.append(data.count('\n') + 1)                   # lines
    a.append(len(data))                              # chars
    a.append(len(data.split()))                      # words
    a.append(data.count(' '))                        # spaces
    a.append(data.count('\t'))                       # tabs
    a.append(data.count('.') + data.count('!') + data.count('?'))  # sentences
    vowels = 'aeiouAEIOU'
    a.append(sum(data.count(ch) for ch in vowels))   # vowels
    consonants = [ch for ch in data if ch.isalpha() and ch not in vowels]
    a.append(len(consonants))                        # consonants
    return a

fname = input('Enter filename: ')
b = ['Lines', 'Chars', 'Words', 'Spaces', 'Tabs', 'Sentences', 'Vowels', 'Consonants']
with open(fname) as f:
    result = count_all(f)
print('Names:', b)
print('Counts:', result)






# 16. Search for Word Frequency in File

def search(f, word):
    data = f.read()
    return data.count(word)

fname = input('Enter filename: ')
f = open(fname)
word = input('Enter word to search: ')
print('Occurrences of word:', search(f, word))
f.close()





# 17. Write n! (factorial) to File

import math

def fact(f, n):
    for i in range(n+1):
        f.write(f"{i}! = {math.factorial(i)}\n")

fname = input('Enter filename: ')
f = open(fname, 'w')
n = int(input('Enter n: '))
fact(f, n)
f.close()

