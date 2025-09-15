# 1. Generator to Divide a String into Words

def word_generator(s):
    for word in s.split():
        yield word

# Example usage:
input_str = input("Enter any string: ")
print("Words of the string")
for word in word_generator(input_str):
    print(word)
'''
Output for input "Hyd is green city":
Words of the string
Hyd
is
green
city
'''






# 2. Output of Generator Yielding Different Types

def f1():
    yield [10, 20]
    yield {30, 40, 50}
    yield 60, 70, 80, 90
    yield 100

g = f1()
for x in g:
    print(x)
    print(type(x))
'''
Output:

[10, 20]
<class 'list'>
{40, 50, 30}
<class 'set'>
(60, 70, 80, 90)
<class 'tuple'>
100
<class 'int'>
'''





# 3. Infinite Generator with `print(*g)`

def f1():
    x = 1
    while x <= 100000000000000000000:
        yield x
        x += 1

g = f1()
print('Begin')
print(*g)
print('End')
'''
output:
Begin
 'print(*g)' tries to print all values from 1 up to a very large number, which takes an extremely long time and will likely cause a MemoryError or hang the system due to its infinite nature.
 "End" is never reached.
'''








# 4. Generator Expression Over Huge Range

g = (x * x for x in range(500000000000000000))
print(*g)
'''
output:
 MemoryError.
'''






# 5. Generator with `list(g)` and Retrieving Next

def f1(begin, end):
    while begin <= end:
        print('Hello')
        yield begin
        begin += 1
    print('End of generator')

g = f1(10, 20)
print('Before')
print(list(g))
print('After')
print(next(g))
'''
Output:

Before
Hello
Hello
Hello
End of generator
[10, 11, 12, ..., 20]
After

StopIteration
'''






# 6. Generator with Unpacking in Loop and Tuple Assignment

def f1():
    print('One')
    yield 1
    print('Two')
    yield 2
    print('Three')
    yield 3
    print('End')

g = f1()
for m in g:
    print(m)
x, y, z = f1()
print(x)
print(y)
print(z)
'''
Output:

One
1
Two
2
Three
3
End
One
Two
Three
1
2
3
'''







# 7. Generator with Incorrect Variables for Unpacking

def f1():
    yield 10
    yield 20
    yield 30
    yield 40

a, b, c = f1()   # Error
p, q, r, s, m = f1()   # Error
'''
output:
- `a, b, c = f1()` --> ValueError
- `p, q, r, s, m = f1()` --> ValueError
'''







# 8. Generator and Indexing/len/multiplication

def f1():
    yield 1
    yield 2
    yield 3

g = f1()
print(len(g))      # Error
print(g * 3)       # Error
print(g)        # Error
print(g[1:3])      # Error
print(*g)          # 1 2 3
'''
Output:
- `len(g)` → TypeError
- `g * 3` → TypeError
- `g` and `g[1:3]` → TypeError
1 2 3

