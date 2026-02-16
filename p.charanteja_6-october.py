# 1. Operator Overloading for Rational Class

import math

class Rat:
    def get(self):
        self.nr = int(input('Enter numerator : '))
        self.dr = int(input('Enter denominator : '))
        self.test()
    
    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator can not be zero, re-enter: '))
    
    def __str__(self):
        return f'{self.nr} / {self.dr}'

    def add(self, a, b):
        self.nr = a.nr * b.dr + a.dr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()
    
    def sub(self, a, b):
        self.nr = a.nr * b.dr - a.dr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()
    
    def mul(self, a, b):
        self.nr = a.nr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()

    def div(self, a, b):
        self.nr = a.nr * b.dr
        self.dr = a.dr * b.nr
        self.simplify()

    def simplify(self):
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g

    # Operator overloading
    def __add__(self, b):
        c = Rat()
        c.add(self, b)
        return c
    
    def __sub__(self, b):
        c = Rat()
        c.sub(self, b)
        return c
    
    def __mul__(self, b):
        c = Rat()
        c.mul(self, b)
        return c
    
    def __truediv__(self, b):
        if b.nr == 0:
            print("Division is not permitted.")
            return None
        c = Rat()
        c.div(self, b)
        return c
'''
# Usage example:
a = Rat()
b = Rat()
# a.get() and b.get() should be called in a full program for user input.
# For demonstration, set directly:
a.nr, a.dr = 2, 3
b.nr, b.dr = 5, 9

c = a + b
d = a - b
e = a * b
print('Sum : ', c)
print('Difference : ', d)
print('Product : ', e)
if b.nr != 0:
    f = a / b
    print('Division :', f)
else:
    print('Division is not permitted.')
```




# 2. Comparison Operator Overloading for Rational Class

class Rat:
    def get(self):
        self.nr = int(input('Enter numerator : '))
        self.dr = int(input('Enter denominator : '))
        self.test()
    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero, re-enter : '))
    def __str__(self):
        return f'{self.nr} / {self.dr}'
    
    # Comparison operator overloads using cross multiplication
    def __gt__(self, b):
        return self.nr * b.dr > self.dr * b.nr
    def __lt__(self, b):
        return self.nr * b.dr < self.dr * b.nr
    def __eq__(self, b):
        return self.nr * b.dr == self.dr * b.nr
    def __ge__(self, b):
        return self.nr * b.dr >= self.dr * b.nr
    def __le__(self, b):
        return self.nr * b.dr <= self.dr * b.nr
    def __ne__(self, b):
        return self.nr * b.dr != self.dr * b.nr
'''
# Example usage:
a = Rat()
b = Rat()
# a.get() and b.get() for input, set directly here
a.nr, a.dr = 2, 3
b.nr, b.dr = 5, 9
print('a > b:', a > b)
print('a < b:', a < b)
print('a == b:', a == b)
print('a >= b:', a >= b)
print('a <= b:', a <= b)
print('a != b:', a != b)
```






# 3. Operator Overloading for Complex Class (without using built-in complex type)

class Complex:
    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imag part: "))
    
    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __add__(self, other):
        c = Complex()
        c.real = self.real + other.real
        c.imag = self.imag + other.imag
        return c

    def __sub__(self, other):
        c = Complex()
        c.real = self.real - other.real
        c.imag = self.imag - other.imag
        return c

    def __mul__(self, other):
        c = Complex()
        c.real = self.real * other.real - self.imag * other.imag
        c.imag = self.real * other.imag + self.imag * other.real
        return c

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        c = Complex()
        c.real = (self.real * other.real + self.imag * other.imag) // denom
        c.imag = (self.imag * other.real - self.real * other.imag) // denom
        return c
'''
# Usage :
a = Complex()
b = Complex()
a.real, a.imag = 3, 4
b.real, b.imag = 5, 6
print('Sum :', a + b)
print('Difference :', a - b)
print('Product :', a * b)
print('Division :', a / b)
```





# 4. Output and Recursion Examples

## a. Is 10 + 20 a recursion?

class c1:
    def __add__(a, b):
        print(10 + 20)
a = c1()
b = c1()
print(a + b)  # Prints 30, returns None. This is not recursion.


## b. Is x + y a recursion?

class c1:
    def __add__(a, b):
        x = c1()
        y = c1()
        print(x + y)  # This is recursive, and will cause RecursionError.
a = c1()
b = c1()
print(a + b)






# 5. Queue Implementation using List

class queue:
    def __init__(self):
        self.q = []
    def isempty(self):
        return len(self.q) == 0
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        return self.q.pop(0) if not self.isempty() else -1
    def first(self):
        return self.q[0] if not self.isempty() else -1
    def last(self):
        return self.q[-1] if not self.isempty() else -1
    def disp(self):
        print("Queue Contents:", self.q)
    def size(self):
        return len(self.q)

def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print queue')
    print('4. First element of queue')
    print('5. Last element of queue')
    print('6. Number of elements in the queue')
    print('7. Exit')

q = queue()
menu()
ch = int(input('Enter choice : ' ))
while ch != 7:
    if ch == 1:
        x = eval(input('Enter element to be inserted : '))
        q.enqueue(x)
        q.disp()
    elif ch == 2:
        print('Deleted :', q.dequeue())
        q.disp()
    elif ch == 3:
        q.disp()
    elif ch == 4:
        print('First element:', q.first())
    elif ch == 5:
        print('Last element:', q.last())
    elif ch == 6:
        print('Size:', q.size())
    menu()
    ch = int(input('Enter choice : '))






# 6. String Reversal Using Stack (Reuse stack class from prog1b)

from prog1b import stack  # Assuming stack has push, pop, isempty methods

s = input("Enter string: ")
st = stack()
for ch in s:
    st.push(ch)
print("Reverse String : ", end='')
while not st.isempty():
    print(st.pop(), end='')
print()







# 7. Parentheses Matching Using Stack (Reuse stack class from prog1b)

from prog1b import stack

expr = input("Enter expression: ")
st = stack()
valid = True
for ch in expr:
    if ch == '(':
        st.push(ch)
    elif ch == ')':
        if st.pop() is None:
            print("Invalid: More closing ')'")
            valid = False
            break
if valid:
    if st.isempty():
        print("Valid!")
    else:





# 8. Comparison Overloading: `__ge__` Example

class c1:
    def __init__(self , y):
        self.x = y
    def __ge__(m , n):
        print('_ge_ method : ', m.x, n.x)
        return m.x > n.x
# End of the class
a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)
'''
output:
_ge_ method :  10 20
False
_ge_ method :  20 10
False
'''





# 9. Equality Overloading: `__eq__` Example

class c1:
    def __init__(self , y):
        self.x = y
    def __eq__(m,n):
        print('_eq_ method  :', m.x, n.x)
        return m.x == n.x
#end of the class
a = c1(10)
b = c1(20)
print(a != b)
print(a == b)

'''
output:
_eq_ method  : 10 20
True
_eq_ method  : 10 20
False
'''





# 10. Equality Overloading, No Return (Tricky Case)

class c1:
    def __init__(self , y):
        self.x = y
    def __eq__(m, n):
        print('_eq_ method  : ', m.x, n.x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a.x != b.x)
'''
output:
_eq_ method  : 25 25
False
_eq_ method  : 25 25
True
False
'''





# 11. Not Equal Overloading, Reference Example

class c1:
    def __init__(self , y):
        self.x = y
    def __ne__(m , n):
        print('_ne_ method  : ', m.x, n.x)
        return m.x != n.x
#end of the class
a = c1(10)
b = a
print(a != b)
print(a == b)
'''
output:
_ne_ method  : 10 10
False
True
'''




# 12. Greater Than Overloading Across Classes

class c1:
    def __init__(self , y):
        self.x = y
    def __gt__(p , q):
        print('c1  class  __gt__  method : ', p.x, q.x)
class c2:
    def __init__(self , y):
        self.x = y
    def __gt__(p , q):
        print('c2  class  __gt__  method : ', p.x, q.x)
#end of the class
a = c1(10)
b = c1(20)
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
'''
output:
c1  class  __gt__  method : 10 20
c1  class  __gt__  method : 20 10
c2  class  __gt__  method : 30 10
c1  class  __gt__  method : 20 40
'''





# 13. Multiply Across Classes

class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 250
    def __mul__(x , y):
        print('__mul__  method  of  class   c1')
        return 25 * 8
class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8
    def __mul__(x , y):
        print('__mul__  method  of  class   c2')
        return 8 * 25
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)
'''
output:
__mul__  method  of  class   c1
200
__mul__  method  of  class   c2
200
'''





# 14. Various Addition With Fallbacks

class c1:
    def __add__(x , y):
        return '__add__ method  of  class   c1'
class c2:
    pass
#end of the class
a = c1()
b = c1()
print('a + b : ', a + b)
print('a + 7 : ', a + 7)
print(7 + a)
print('7 + 8 : ', 7 + 8)
m = c2()
n = c2()
print(m + n)
print('a + m : ', a + m)
print(m + a)
```
Output:
a + b :  __add__ method  of  class   c1
a + 7 :  __add__ method  of  class   c1
TypeError: unsupported operand type(s) for +: 'int' and 'c1'
7 + 8 : 15
TypeError: unsupported operand type(s) for +: 'c2' and 'c2'
a + m :  __add__ method  of  class   c1
TypeError: unsupported operand type(s) for +: 'c2' and 'c1'
'''

# 15. Custom + for number/sum and string/join

class c1:
    def __init__(self , y):
        self.x = y
    def __add__(p , q):
        if isinstance(p.x, int) and isinstance(q.x, int):
            return p.x + q.x
        else:
            return str(p.x) + str(q.x)
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ', a + b)
print('Join : ', m + n)
'''
output:
Sum : 30
Join : 1020
'''




