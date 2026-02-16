# Calling Parent Instance Method

class parent:
    def m1(self):
        print('parent Method')

class child(parent):
    def m1(self):
        super().m1()  # Calls parent's m1 method
        print('child Method')
'''

Output:
parent Method
child Method
'''





# Calling Parent Class Method

class parent:
    @classmethod
    def m1(cls):
        print('parent Method')

class child(parent):
    @classmethod
    def m2(cls):
        super().m1()  # Calls parent's class method
        print('child Method')
'''

Output:
parent Method
child Method
'''






# Calling Parent Static Method

class parent:
    @staticmethod
    def m1():
        print('parent method')

class child(parent):
    @staticmethod
    def m2():
        parent.m1()  # Calls parent's static method
        print('child method')
'''

Output:
parent method
child method
'''





# Parent and Child Classes with Different Static Methods

class parent:
    @staticmethod
    def m1():
        print('parent method')

class child(parent):
    @staticmethod
    def m2():
        parent.m1()          # Call parent static method directly
        super(child, child).m1()  # Call parent static method via super()
        super().m1()         # Call parent static method via super()
        print('child method')

# Outputs
child.m2()
child.m1()
'''

Output:
parent method
parent method
parent method
child method
parent method
'''






# Parent and Child Classes with Same Static Method Name

class parent:
    @staticmethod
    def m1():
        print('parent method')

class child(parent):
    @staticmethod
    def m1():
        super(child, child).m1()  # Call parent's method via super
        print('child method')

# Outputs
child.m1()
parent.m1()
'''

Output:
parent method
child method
parent method
'''







# Parent and Child Classes with Static Variables with Different Names

class parent:
    x = 10
    def m1(self):
        print(parent.x)    # Access parent's variable x

class child(parent):
    y = 20
    def m2(self):
        print(super().x)   # Access parent's x via super()
        print(parent.x)    # Access parent's x via class name
        print(self.x)      # Access parent's x (inherited variable)
        print(child.y)     # Access child's variable y
        print(self.y)      # Access child's variable y also

p = parent()
c = child()

p.m1()
c.m2()
'''

Output:
10
10
10
10
20
20
'''






# Parent and Child Classes with Static Variables with Same Name

class parent:
    x = 10
    def m1(self):
        print(parent.x)    # Parent variable x
        print(super(child, self).x)  # Another way to access parent's x

class child(parent):
    x = 20
    def m1(self):
        print(super().x)   # Access parent's x via super()
        print(parent.x)    # Access parent's x via class name
        print(child.x)     # Access child's x
        print(self.x)      # Access child's x too

p = parent()
c = child()

p.m1()
c.m1()
'''

Output:
10
Traceback (since super(child, self) won't work here)
10
10
20
20
'''






# Reading Inputs and Printing for Parent and Child Objects

class parent:
    def get(self):
        self.a, self.b = map(int, input().split())
    def disp(self):
        print(f"{self.a}\t{self.b}")

class child(parent):
    def get(self):
        self.a, self.b, self.c, self.d = map(int, input().split())
    def disp(self):
        print(f"{self.a}\t{self.b}")
        print(f"{self.c}\t{self.d}")
    def total(self):
        return self.a + self.b + self.c + self.d

# Create objects
p = parent()
c = child()

print('parent object')
p.get()   # Input example: 10 20

print('child object')
c.get()   # Input example: 30 40 50 60

print('parent object :', end='\t')
p.disp()
print('child object :')
c.disp()
print('Sum of the values in child object :', c.total())
'''
Sample Inputs:

10 20
30 40 50 60

Output:

parent object
child object
parent object : 10	20
child object :
30	40
50	60
Sum of the values in child object : 180
'''







# Program for circle and cylinder calculations

import math
class circle:
    def get(self):
        self.r = float(input('Enter radius of circle: '))
    def area(self):
        return math.pi * self.r ** 2
    def cir(self):
        return 2 * math.pi * self.r

class cylinder(circle):
    def get(self):
        self.r = float(input('Enter radius of cylinder: '))
        self.h = float(input('Enter height of cylinder: '))
    def area(self):
        # Surface area of cylinder
        return 2 * math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h
    def volume(self):
        return math.pi * self.r ** 2 * self.h

def menu():
    print('1 . Circle')
    print('2 . Cylinder')
    print('3 . Exit')

while True:
    menu()
    ch = int(input('Enter choice: '))
    if ch == 1:
        c = circle()
        c.get()
        print('Area:', c.area())
        print('Circumference:', c.cir())
    elif ch == 2:
        cyl = cylinder()
        cyl.get()
        print('Surface Area of Cylinder:', cyl.area())
        print('Volume of Cylinder:', cyl.volume())
    elif ch == 3:
        break
    else:
        print('Invalid choice')
'''
 Output:

Enter choice: 1
Enter radius of circle: 5
Area: 78.53981633974483
Circumference: 31.41592653589793
Enter choice: 2
Enter radius of cylinder: 3
Enter height of cylinder: 10
Surface Area of Cylinder: 188.49555921538757
Volume of Cylinder: 282.7433388230814
Enter choice: 3
'''





# Program for rectangle, square, cube calculations

class square:
    def get(self):
        self.a = float(input('Enter side of square: '))
    def area(self):
        return self.a ** 2
    def peri(self):
        return 4 * self.a

class rectangle(square):
    def get(self):
        self.a, self.b = map(float, input('Enter length and breadth: ').split())
    def area(self):
        return self.a * self.b
    def peri(self):
        return 2 * (self.a + self.b)

class cube(square):
    def get(self):
        self.a = float(input('Enter side of cube: '))
    def area(self):
        return 6 * self.a ** 2
    def volume(self):
        return self.a ** 3

def menu():
    print('1 . Square')
    print('2 . Rectangle')
    print('3 . Cube')
    print('4 . Exit')

while True:
    menu()
    ch = int(input('Enter choice: '))
    if ch == 1:
        s = square()
        s.get()
        print('Area:', s.area())
        print('Perimeter:', s.peri())
    elif ch == 2:
        r = rectangle()
        r.get()
        print('Area:', r.area())
        print('Perimeter:', r.peri())
    elif ch == 3:
        c = cube()
        c.get()
        print('Surface Area:', c.area())
        print('Volume:', c.volume())
    elif ch == 4:
        break
    else:
        print('Invalid choice')
'''

output:

Enter choice: 1
Enter side of square: 4
Area: 16
Perimeter: 16
Enter choice: 2
Enter length and breadth: 5 10
Area: 50
Perimeter: 30
Enter choice: 3
Enter side of cube: 3
Surface Area: 54
Volume: 27
Enter choice: 4
'''





# Program for class inheritance and type checks

class c1:
    pass
class c2(c1):
    pass
class c3(c2):
    pass
class c4(c3):
    pass

print(issubclass(c2, c1))  # True
print(issubclass(c4, c3))  # True
print(issubclass(c4, c2))  # True
print(issubclass(c4, c1))  # True
print(issubclass(c4, object))  # True
print(issubclass(c4, (int, float, str, bool)))  # False

# For isinstance:
obj = c3()
print(isinstance(25, int))  # True
print(isinstance(10.8, float))  # True
print(isinstance('Hyd', str))  # True
print(isinstance(3+4j, complex))  # True
print(isinstance(True, bool))  # True
print(isinstance(True, int))  # True
print(isinstance('True', str))  # True
print(isinstance(True, str))  # False
print(isinstance(obj, c3))  # True
print(isinstance(obj, c2))  # True
print(isinstance(obj, c1))  # True
print(isinstance(obj, object))  # True







# Linked List Implementation

## Node and List Structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)





## Insertion and Deletion

def add_first(self, node):
    node.next = self.head
    self.head = node

def remove_node(self, target_data):
    if self.head is None:
        raise Exception("List is empty")
    if self.head.data == target_data:
        self.head = self.head.next
        return
    previous_node = self.head
    for node in self:
        if node.data == target_data:
            previous_node.next = node.next
            return
        previous_node = node





## Traversal and Search

def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next



