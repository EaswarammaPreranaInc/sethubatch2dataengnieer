# Write  a  program  to  implement  queue  using  list
class  queue:
    def  _init_(q):
        q.list = []
    def  isempty(q):
        return  q.list == []#True  when  queue  is  empty  and  False  otherwise
    def  enqueue(q , x):
        q.list.append(x)#How  to  insert  'x'  into  the  queue
    def  dequeue(q):
        try:
            return q.list.pop(0)#How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
        except:
            return -1 #(return  -1  when  deletion  is  not  possible)
    def  first(q):
        try:
            return q.list[0]#How  to  return  the  first  element  of  the  queue
        except:
            return -1 #(return  -1  when  queue  is  empty)
    def  last(q):
        try:
            return q.list[-1] #How  to  return  the  first  element  of  the  queue
        except:
            return -1#(return   -1  when  queue  is  empty)
    def  disp(q):
            print(q.list)#How  to  print  queue
    def  size(q):
            return len(q.list)#How  to  return  number   of  elements  in  the  queue
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  queue')
        print('4. First  element of queue')
        print('5. Last  element of queue')
        print('6. Number  of  elements  in  the  queue')
        print('7. Exit')
# End of  the  function
q = queue() # How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while ch<7: #repeat  until  user  input  is  7
	match  ch:
		case  1:
				x = eval(input('Enter  element  to  be  inserted : '))
				q.enqueue(x)#How  to  insert  'x'  into  the  queue
				q.disp() #How  to  print  queue
		case  2:
				x = q.dequeue()#How  to  delete  queue  element  and  print  the  deleted  element
				if x == -1:
				    print("Queue is Empty")
				else:
					print("Deleted element: ",x)
				q.disp()#How  to  print  queue
		case  3:
				q.disp()#How  to  print  the  queue
		case  4:
				x = q.first()
				if x == -1:
				    print("Queue is empty")
				else:
					print("First Element is ", x)#How  to  print  first  element  of  the  queue
		case  5:
				x = q.last()
				if x == -1:
				    print("Queue is empty")
				else:
					print("Last element is ",x)#How  to  print  last  element  of  the  queue
		case  6:
				print("Number of elements: ",q.size())#How  to  print  number  of  elements  in  the  queue
				
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))



from prog1b import stack #How  to  import  stack  class  from  prog1b  module
s = stack()#How  to  create  stack  class  object
st = input("Enter your string: ")#How  to  read  a  string  into  a  str  object
for ch in st:
    s.push(ch)#How  to  push  each  char  of  string  into  the  stack
print("Reverse  String :  ")
for i in range(s.size()):
    print(s.pop(), end = " ")#How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
print()




from prog import stack 
s = stack()
expr = input("Enter your Expression: ")
balanced = True
for ch in expr:
    if ch == '(':
        s.push(ch)
    elif ch == ')':
        if s.isempty():  
            balanced = False
            break
        else:
            s.pop()
    else:
        pass
if balanced and s.isempty():
    print("Valid expression")
else:
    print("Not valid expression")




import math
class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter: '))

    def _str_(self):
        return f'{self.nr} / {self.dr}'

    def simplify(self):
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr //= g
            self.dr //= g

    def _add_(self, b):
        r = Rat()
        r.nr = self.nr * b.dr + self.dr * b.nr
        r.dr = self.dr * b.dr
        r.simplify()
        return r

    def _sub_(self, b):
        r = Rat()
        r.nr = self.nr * b.dr - self.dr * b.nr
        r.dr = self.dr * b.dr
        r.simplify()
        return r

    def _mul_(self, b):
        r = Rat()
        r.nr = self.nr * b.nr
        r.dr = self.dr * b.dr
        r.simplify()
        return r

    def _truediv_(self, b):
        if b.nr == 0:
            print('Division not permitted because second numerator is 0.')
            return None
        r = Rat()
        r.nr = self.nr * b.dr
        r.dr = self.dr * b.nr
        r.simplify()
        return r


a = Rat()
b = Rat()
a.get()
b.get()
print('Sum:', a + b)
print('Difference:', a - b)
print('Product:', a * b)
res = a / b
if res:
    print('Division:', res)

'''
OUTPUT:
Enter numerator: 2
Enter denominator: 3
Enter numerator: 5
Enter denominator: 9
Sum: 11 / 9
Difference: 1 / 9
Product: 10 / 27
Division: 6 / 5
'''

class Complex:
    def get(self):
        self.real = int(input('Enter real part: '))
        self.imag = int(input('Enter imaginary part: '))

    def _str_(self):
        if self.imag >= 0:
            return f'{self.real} + {self.imag}i'
        else:
            return f'{self.real} - {abs(self.imag)}i'

    def _add_(self, b):
        r = Complex()
        r.real = self.real + b.real
        r.imag = self.imag + b.imag
        return r

    def _sub_(self, b):
        r = Complex()
        r.real = self.real - b.real
        r.imag = self.imag - b.imag
        return r

    def _mul_(self, b):
        r = Complex()
        r.real = self.real * b.real - self.imag * b.imag
        r.imag = self.real * b.imag + self.imag * b.real
        return r

    def _truediv_(self, b):
        r = Complex()
        denom = b.real ** 2 + b.imag ** 2
        r.real = (self.real * b.real + self.imag * b.imag) / denom
        r.imag = (self.imag * b.real - self.real * b.imag) / denom
        return r

a = Complex()
b = Complex()
print('Enter 1st complex number:')
a.get()
print('Enter 2nd complex number:')
b.get()
print('Sum:', a + b)
print('Difference:', a - b)
print('Product:', a * b)
print('Division:', a / b)

'''
OUTPUT:
Enter 1st complex number:
Enter real part: 3
Enter imaginary part: 4
Enter 2nd complex number:
Enter real part: 5
Enter imaginary part: 6
Sum: 8 + 10i
Difference: -2 - 2i
Product: -9 + 38i
Division: 0.639344262295082 + 0.03278688524590164i
'''

class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter: '))

    def _gt_(self, b):
        return self.nr * b.dr > self.dr * b.nr

    def _lt_(self, b):
        return self.nr * b.dr < self.dr * b.nr

    def _eq_(self, b):
        return self.nr * b.dr == self.dr * b.nr

    def _ge_(self, b):
        return self.nr * b.dr >= self.dr * b.nr

    def _le_(self, b):
        return self.nr * b.dr <= self.dr * b.nr

    def _ne_(self, b):
        return self.nr * b.dr != self.dr * b.nr

a = Rat()
b = Rat()
a.get()
b.get()

if a > b: print('>')
if a < b: print('<')
if a == b: print('==')
if a >= b: print('>=')
if a <= b: print('<=')
if a != b: print('!=')

'''
OUTPUT:
Enter numerator: 2
Enter denominator: 3
Enter numerator: 5
Enter denominator: 9
>
>=
!=
'''

class c1:
    def _add_(a, b):
        print(10 + 20)

a = c1()
b = c1()
print(a + b)

'''
OUTPUT:
30
None
'''

class c1:
    def _add_(a, b):
        x = c1()
        y = c1()
        print(x + y)

a = c1()
b = c1()
print(a + b)

'''
OUTPUT:
This causes infinite recursion!
'''

class c1:
    def _init_(self, y):
        self.x = y
    def _ge_(m, n):
        print('_ge_ method :', m.x, n.x)
        return m.x > n.x

a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)

'''
OUTPUT:
_ge_ method : 10 20
False
True
'''

class c1:
    def _init_(self, y):
        self.x = y
    def _eq_(m, n):
        print('_eq_ method :', m.x, n.x)
        return m.x == n.x

a = c1(10)
b = c1(20)
print(a != b)  # not (a == b)
print(a == b)

'''
OUTPUT:
_eq_ method : 10 20
True
_eq_ method : 10 20
False
'''

class c1:
    def _init_(self, y):
        self.x = y
    def _eq_(m, n):
        print('_eq_ method :', m.x, n.x)

a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a.x != b.x)

'''
OUTPUT:
_eq_ method : 25 25
None
True
False
'''


class c1:
    def _init_(self, y):
        self.x = y
    def _ne_(m, n):
        print('_ne_ method :', m.x, n.x)
        return m.x != n.x

a = c1(10)
b = a
print(a != b)
print(a == b)

'''
OUTPUT:
_ne_ method : 10 10
False
True
'''

class c1:
    def _gt_(a, b):
        print(10 > 20)
        print(a > b)

a = c1()
b = c1()
print(a > b)

'''
OUTPUT:
True
RecursionError
'''

class c1:
    def _init_(self, y):
        self.x = y
    def _gt_(p, q):
        print('c1 class _gt_ method :', p.x, q.x)

class c2:
    def _init_(self, y):
        self.x = y
    def _gt_(p, q):
        print('c2 class _gt_ method :', p.x, q.x)

a = c1(10)
b = c1(20)
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b

'''
OUTPUT:
c1 class _gt_ method : 10 20
c1 class _gt_ method : 20 10
c2 class _gt_ method : 40 10
'''

class c1:
    def _init_(self):
        self.empno = 25
        self.hr = 250
    def _mul_(x, y):
        print('_mul_ method of class c1')
        return x.hr * y.noh

class c2:
    def _init_(self):
        self.empno = 25
        self.noh = 8
    def _mul_(x, y):
        print('_mul_ method of class c2')
        return x.noh * y.hr

a = c1()
b = c2()
print(a * b)
print(b * a)

'''
OUTPUT:
_mul_ method of class c1
2000
_mul_ method of class c2
2000
'''

class c1:
    def _add_(x, y):
        return '_add_ method of class c1'

class c2:
    pass

a = c1()
b = c1()
print('a + b:', a + b)
print('a + 7:', a + 7)
try:
    print(7 + a)
except TypeError:
    print('7 + a: Not supported')
print('7 + 8:', 7 + 8)
m = c2()
n = c2()
try:
    print(m + n)
except TypeError:
    print('m + n: Not supported')
print('a + m:', a + m)
try:
    print(m + a)
except TypeError:
    print('m + a: Not supported')

'''
OUTPUT:
a + b: _add_ method of class c1
a + 7: _add_ method of class c1
7 + a: Not supported
7 + 8: 15
m + n: Not supported
a + m: _add_ method of class c1
m + a: Not supported
'''

class c1:
    def _init_(self, y):
        self.x = y

    def _add_(p, q):
        if isinstance(p.x, str) or isinstance(q.x, str):
            return str(p.x) + str(q.x)
        else:
            return p.x + q.x

a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')

print('Sum:', a + b)
print('Join:', m + n)

'''
OUTPUT:
Sum: 30
Join: 1020
'''
