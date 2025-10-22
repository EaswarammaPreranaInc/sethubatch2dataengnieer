class parent:
    def m1(self):
        print('Overridden  Method')
class child(parent):
    def m1(self):
        print('Overriding  Method')
#end of the class
x = parent()
x.m1()    # Overridden  Method
x = child()
x.m1()    # Overriding  Method

class parent:
    def m1(self):
        print('m1  method  of  parent  class')
    def m2(self):
        print('m2  method  of  parent class')
class child(parent):
    def m1(self):
        print('m1  method  of  child  class')
    def m3(self):
        print('m3  method  of  child  class')
#end of the class
x = parent()
x.m1()    # m1  method  of  parent  class
x.m2()    # m2  method  of  parent class
x.m3()    # Error: parent class object has no method named m3
x = child()
x.m1()    # m1  method  of  child  class
x.m2()    # m2  method  of  parent class
x.m3()    # m3  method  of  child  class

class parent:
    def marriage(self):
        print('Arranged Marriage')
    def property(self):
        print('One  Crore')
    def study(self):
        print('Studies only', end='\t')
class child(parent):
    def marriage(self):
        print('Love Marriage')
    def study(self):
        super().study()
        print('+ Entertainment')
#end of the class
c = child()
c.marriage()   # Love Marriage
c.property()   # One  Crore
c.study()      # Studies only	+ Entertainment

class parent:
    def add(self, x, y):
        return x + y
class child(parent):
    def add(self, x, y, z):
        return x + y + z
# End of the class
c = child()
print(c.add(10, 20, 30))      # 60
print(c.add(10, 20))          # Error: missing 1 required positional argument 'z'
print(super(child, c).add(40, 50))  # 90 

class parent:
    def add(self, x, y):
        print('parent  method')
        return x + y
class child(parent):
    def add(self, x, y, z = 3):
        print('child  method')
        return x + y + z
#End of the class
c = child()
print(c.add(10, 20, 30))   # child  method  
# 60
print(c.add(10, 20))       # child  method 
            # 33
class parent:
    def m1(self, a, b, /):
        print(f'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class child(parent):
    def m1(self, x, y):
        print(f'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c.m1(x=10, y=20)   # child  method  --->  x  :  10     y  :  20
c.m1(30, 40)       # child  method  --->  x  :  30	y  :  40

from abc import *
class c1(ABC):
    @abstractmethod
    def m1(self):
        pass
    def __init__(self):
        print('c1  class  constructor')
class c2(ABC):
    def m1(self):
        pass
    def __init__(self):
        print('c2  class  constructor')
class c3:
    @abstractmethod
    def m1(self):
        pass
    def __init__(self):
        print('c3  class  constructor')
class c4(c1):
    def m1(self):
        pass
    def __init__(self):
        print('c4  class  constructor')
class c5(c1):
    def __init__(self):
        print('c1  class  constructor')
# End  of  the  class
c1()  #  Error: Can't instantiate abstract class c1 with abstract method m1
c2()  #  c2  class  constructor
c3()  #  c3  class  constructor
c4()  #  c4  class  constructor
c5()  #  Error: Can't instantiate abstract class c5 with abstract method m1

Q) Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square
Ans)  import math
from abc import *
class shape(ABC):
    def get(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def peri(self):
        pass
    @abstractmethod
    def test(self):
        pass
class triangle(shape):
    def get(self):
        print('Enter 3 sides of triangle')
        self.a = float(input('Enter side a: '))
        self.b = float(input('Enter side b: '))
        self.c = float(input('Enter side c: '))
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
    def test(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            pass
        else:
            print('Not a triangle')
            exit()
class circle(shape):
    def get(self):
        print('Enter radius of circle : ', end='\t')
        self.a = float(input())
    def area(self):
        return 3.14159 * self.a ** 2
    def peri(self):
        return 2 * 3.14159 * self.a
    def test(self):
        if self.a < 0:
            print('Radius can not be -ve')
            exit()
class rectangle(shape):
    def get(self):
        print('Enter length and breadth of rectangle')
        self.a = float(input('Enter length: '))
        self.b = float(input('Enter breadth: '))
    def area(self):
        return self.a * self.b
    def peri(self):
        return 2 * (self.a + self.b)
    def test(self):
        if self.a == self.b:
            print('Not a rectangle')
            exit()
class square(shape):
    def get(self):
        print('Enter any side of square : ', end='\t')
        self.a = float(input())
    def area(self):
        return self.a ** 2
    def peri(self):
        return 4 * self.a
    def test(self):
        pass
def menu():
    print('1. Triangle')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Exit')
# End of menu function
def operation(s):
    s.get()               
    s.test()              
    print('Area  : ', s.area())
    print('Perimeter  : ', s.peri())
# End of the function
while True:
    menu()
    ch = eval(input('Enter choice : '))
    match ch:
        case 1:
            operation(triangle())
        case 2:
            operation(circle())
        case 3:
            operation(rectangle())
        case 4:
            operation(square())
        case 5:
            exit()
    # End of match
# End of while loop
print('Good Bye') 


from abc import *
class parent(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
class child(parent):
    def m1(self):
        print('m1  method  of  child  class')
class gc(child):
    def m2(self):
        print('m2  method  of  gc  class')
class ggc(gc):
    def m3(self):
        print('m3  method  of  ggc  class')
# End of the class
a = ggc()
a.m1()   # m1  method  of  child  class
a.m2()   # m2  method  of  gc  class
a.m3()   # m3  method  of  ggc  class
parent() # Error: can't instantiate abstract class (m1, m2, m3 not implemented)
child()  # Error: still abstract (m2, m3 not implemented)
gc()     # Error: still abstract (m3 not implemented)

#  Write  a  method  to  determine  length  of  circular  linked  list
from Linkedlist import linkedlist
class  cll(linkedlist):
	def  length(a):
		if a.isempty():
			return 0
		count = 0
		temp = a.first
		while True:
			count += 1
			temp = temp.next
			if temp == a.first:
				break
		return count
if __name__ == '__main__':
    obj = cll()           
    obj.create()          
    print('Number of nodes:', obj.length())

from Lengthoflinkedlist import cll
class circular_linked_list(cll):
    def find(self, i):
        if self.isempty():
            return None
        count = 1
        temp = self.first
        while True:
            if count == i:
                return temp.data
            temp = temp.next
            count += 1
            if temp == self.first:
                break
        return None  
if __name__ == '__main__':
    obj = circular_linked_list()
    obj.create()   
    while True:
        i = int(input("Enter value of 'i': "))
        x = obj.find(i)   
        if x is None:
            print(f'Node {i} does not exist')
        else:
            print(f'Data of node {i} is: {x}')
        ch = input('Do you wish to continue (y / n): ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

# Write  a  method  to  search  for  a  value  in  the  linked  list.
from Linkedlist import linkedlist
class circular_linked_list(linkedlist):
    def search(self, x):
        if self.isempty():
            return None
        temp = self.first
        while True:
            if temp.data == x:
                return temp         
            temp = temp.next
            if temp == self.first:  
                break
        return None
if __name__ == '__main__':
    obj = circular_linked_list()
    obj.create()  
    while True:
        x = eval(input("Enter value to be searched: "))
        node = obj.search(x)     
        if node is None:
            print(f'{x} is not found')
        else:
            print(f'Found at address: {id(node)}')  
        ch = input('Do you wish to continue (y / n): ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

#  Write  a  method  to  insert  a  node  in  the  linked  list
from Lengthoflinkedlist import cll
class circular_linked_list(cll):
    def insert(self, i, x):
        n = self.length()  
        if i < 0 or i > n:
            print(f'Node {i} does not exist')
            return
        from Linkedlist import node
        new_node = node(x)
        if self.isempty():
            self.first = new_node
            new_node.next = self.first
            return
        if i == 0:
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.first
            self.first = new_node
            return
        temp = self.first
        count = 1
        while count < i and temp.next != self.first:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
if __name__ == '__main__':
    obj = circular_linked_list()
    obj.create()   
    while True:
        i = int(input("Enter value of 'i': "))
        x = eval(input('Enter value to be inserted: '))
        obj.insert(i, x)   
        print('Updated circular linked list:')
        obj.disp()         
        ch = input('Would you like to insert another node (Y or N)? : ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

# Write  a  method  to  delete  ith  node  of  linked  list
from Lengthoflinkedlist import cll
class circular_linked_list(cll):
    def delete(self, i):
        n = self.length()
        if i <= 0 or i > n:
            return None
        if n == 1:
            data = self.first.data
            self.first = None
            return data
        if i == 1:
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            data = self.first.data
            self.first = self.first.next
            temp.next = self.first
            return data
        prev = self.first
        count = 1
        while count < i - 1 and prev.next != self.first:
            prev = prev.next
            count += 1
        to_delete = prev.next
        data = to_delete.data
        prev.next = to_delete.next
        return data
if __name__ == '__main__':
    obj = circular_linked_list()
    obj.create()   
    while True:
        i = int(input('Enter value of i: '))
        x = obj.delete(i)  
        if x is None:
            print(f'Node {i} does not exist')
        else:
            print('Data of deleted node is:', x)
        print('Updated circular linked list:')
        obj.disp()
        ch = input('Would you like to delete another node (Y or N)? : ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

#  Write  destructor  to  delete  whole  linked  list
from Linkedlist import linkedlist
class circular_linked_list(linkedlist):
    def __del__(self):
        if self.isempty():
            print('Linked list is already empty')
            return
        temp = self.first
        while True:
            next_node = temp.next
            temp.next = None
            print(f'Deleting node with data: {temp.data}')
            del temp
            if next_node == self.first:
                break
            temp = next_node
        self.first = None
        print('Linked list is empty')
if __name__ == '__main__':
    obj = circular_linked_list()
    obj.create()   
    print('Circular linked list elements:')
    obj.disp()
    print('\nDeleting entire linked list...')
    del obj

#  Write  a  method  to  copy  a  linked  list
from Linkedlist import linkedlist, node  
class circular_linked_list(linkedlist):
    def copy(self):
        b = circular_linked_list()
        if self.isempty():
            print("Input linked list is empty — copy will also be empty.")
            return b
        temp_a = self.first
        b.first = node(temp_a.data)  
        temp_b = b.first
        temp_a = temp_a.next
        while temp_a != self.first:
            new_node = node(temp_a.data)
            temp_b.next = new_node
            temp_b = new_node
            temp_a = temp_a.next
        temp_b.next = b.first
        return b
if __name__ == '__main__':
    cll1 = circular_linked_list()
    cll1.create()
    print("Original Circular Linked List:")
    cll1.disp()
    cll2 = cll1.copy()
    print("\nCopied Circular Linked List:")
    cll2.disp()

#  Write  methods  to  create  and  print  linked  list
class Node:
    def __init__(self, x):
        self.data = x
        self.l = None
        self.r = None
class LinkedList:
    def __init__(self):
        self.l = None  
        self.r = None  

    def isempty(self):
        return self.l is None
    def disp_left_right(self):
        if self.isempty():
            print('Linked List is empty')
        else:
            current = self.l
            while current:
                print(current.data, end=' ')
                current = current.r
            print()
    def disp_right_left(self):
        if self.isempty():
            print('Linked List is empty')
        else:
            current = self.r
            while current:
                print(current.data, end=' ')
                current = current.l
            print()
    def append(self, new_node):
        if self.isempty():
            self.l = self.r = new_node
        else:
            self.r.r = new_node
            new_node.l = self.r
            self.r = new_node
    def create_from_input(self):
        n = int(input("Enter the number of nodes: "))
        for i in range(n):
            data = int(input(f"Enter data for node {i+1}: "))
            new_node = Node(data)
            self.append(new_node)
if __name__ == '__main__':
    a = LinkedList()                   
    a.create_from_input()
    print('Linked List from left to right:', end=' ')
    a.disp_left_right()
    print('Linked List from right to left:', end=' ')
    a.disp_right_left()
