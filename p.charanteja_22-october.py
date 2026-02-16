# 1 Find Outputs (Method Overriding and Inheritance)

class parent:
	def m1(self):
		print('Overridden Method')
class child(parent):
	def m1(self):
		print('Overriding Method')
#end of the class
x = parent()
x . m1()
x = child()
x . m1()
'''
The output will be:
Overridden Method
Overriding Method
'''




# Program 2 (Method Overriding and Inheritance)

class parent:
	def m1(self):
		print('m1 method of parent class')
	def m2(self):
		print('m2 method of parent class')
class child(parent):
	def m1(self):
		print('m1 method of child class')
	def m3(self):
		print('m3 method of child class')
#end of the class
x = parent()
x . m1()
x . m2()
x . m3() # Error
x = child()
x . m1()
x . m2()
x . m3()
'''
The output will be:

m1 method of parent class
m2 method of parent class
Error: 'parent' object has no attribute 'm3'
'''





# Program 3 (Using `super()`)

class parent:
	def marriage(self):
		print('Arranged Marriage')
	def property(self):
		print('One Crore')
	def study(self):
		print('Studies only' , end = '\t')
class child(parent):
	def marriage(self):
		print('Love Marriage')
	def study(self):
		super() . study()
		print(' + Entertainment')
#end of the class
c = child()
c . marriage()
c . property()
c . study()
'''
The output will be:

Love Marriage
One Crore
Studies only	 + Entertainment
'''




# Program 4 (Method Overloading/Signature Change)

class parent:
	def add(self , x , y):
		return x + y
class child(parent):
	def add(self , x , y , z): 
		return x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30))
print(c . add(10 , 20)) 
print(super(child , c) . add(40,50))
'''
The output will be:

60
Traceback (most recent call last):
  ...
TypeError: child.add() missing 1 required positional argument: 'z'
'''





# Program 5 (Method Overriding with Default Arguments)

class parent:
	def add(self , x , y):
		print('parent method')
		return x + y
class child(parent):
	def add(self , x , y , z = 3):
		print('child method')
		return x + y + z
#End of the class
c = child()
print(c . add(10 , 20 , 30))
print(c . add(10 , 20))
'''
The output will be:

child method
60
child method
33
'''




# Program 6 (Positional-Only Arguments)

class parent:
	def m1(self , a , b , /):
		print(F'parent method ---> a : {a} \t b : {b}')
class child(parent):
	def m1(self , x , y):
		print(F'child method ---> x : {x} \t y : {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)
c . m1(30 , 40)
'''
The output will be:
child method ---> x : 10 	 y : 20
child method ---> x : 30 	 y : 40
'''




# Program 7 (Abstract Base Classes - Instantiation Errors)

from abc import *
class c1(ABC):
	@abstractmethod
	def m1(self):
		pass
	def __init__(self):
		print('c1 class constructor')
class c2(ABC): # c2 is an Abstract Base Class but has no abstract methods
	def m1(self):
		pass
	def __init__(self):
		print('c2 class constructor')
class c3: # c3 is not an ABC, so @abstractmethod does nothing
	@abstractmethod
	def m1(self):
		pass
	def __init__(self):
		print('c3 class constructor')
class c4(c1): # c4 implements the abstract method m1
	def m1(self):
		pass
	def __init__(self):
		print('c4 class constructor')
class c5(c1): # c5 is an ABC because it inherits from c1 but doesn't implement m1
	def __init__(self):
		print('c1 class constructor')
# End of the class
c1() # Error: Cannot instantiate c1 (Abstract)
c2()
c3()
c4()
c5() # Error: Cannot instantiate c5 (Abstract)





# 8. Shape Calculations (OOP with ABCs)

import math
from abc import *
import sys

# Constants
PI = 3.14159

class shape(ABC):
	def __init__(self):
		# Default members, to be potentially overridden or set in child's get()
		self.a = None
		self.b = None
		self.c = None

	@abstractmethod
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
		print('Enter 3 sides of triangle:')
		try:
			self.a = float(input('Side a: '))
			self.b = float(input('Side b: '))
			self.c = float(input('Side c: '))
		except ValueError:
			print("Invalid input. Sides must be numbers.")
			self.a = self.b = self.c = 0 # Invalidate inputs

	def test(self):
		# Check for non-positive sides
		if self.a <= 0 or self.b <= 0 or self.c <= 0:
			print('Not a valid triangle: Sides must be positive.')
			return False
		# Check triangle inequality theorem
		if (self.a + self.b <= self.c) or \
		   (self.a + self.c <= self.b) or \
		   (self.b + self.c <= self.a):
			print('Not a valid triangle: Sum of any 2 sides must be greater than the 3rd side.')
			return False
		return True
	
	def area(self):
		s = (self.a + self.b + self.c) / 2
		# Heron's formula: sqrt(s * (s - a) * (s - b) * (s - c))
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
	
	def peri(self):
		return self.a + self.b + self.c

class circle(shape):
	def get(self):
		try:
			self.a = float(input('Enter radius of circle : '))
		except ValueError:
			print("Invalid input. Radius must be a number.")
			self.a = 0 # Invalidate input
	
	def test(self):
		if self.a < 0:
			print('Radius can not be negative.')
			return False
		return True
	
	def area(self):
		# Area of circle: PI * r^2
		return PI * self.a ** 2
	
	def peri(self):
		# Circumference of circle: 2 * PI * r
		return 2 * PI * self.a

class rectangle(shape):
	def get(self):
		print('Enter length and breadth of rectangle:')
		try:
			self.a = float(input('Length: ')) # 'a' is length
			self.b = float(input('Breadth: ')) # 'b' is breadth
		except ValueError:
			print("Invalid input. Dimensions must be numbers.")
			self.a = self.b = 0 # Invalidate inputs

	def test(self):
		if self.a <= 0 or self.b <= 0:
			print('Not a valid rectangle: Length and breadth must be positive.')
			return False
		# A proper rectangle has different length and breadth (excluding square)
		# The check 'if length and breadth same' is often meant to enforce
		# that it's *not* a square, though a square is a type of rectangle.
		# For this specific homework, we will enforce the non-square check.
		if self.a == self.b:
			print('Not a rectangle (it\'s a square). Please use the Square option.')
			return False
		return True

	def area(self):
		# Area of rectangle: length * breadth
		return self.a * self.b
	
	def peri(self):
		# Perimeter of rectangle: 2 * (length + breadth)
		return 2 * (self.a + self.b)

class square(shape):
	def get(self):
		try:
			self.a = float(input('Enter any side of square : '))
		except ValueError:
			print("Invalid input. Side must be a number.")
			self.a = 0 # Invalidate input

	def test(self):
		if self.a <= 0:
			print('Side can not be negative or zero.')
			return False
		return True

	def area(self):
		# Area of square: side^2
		return self.a ** 2
	
	def peri(self):
		# Perimeter of square: 4 * side
		return 4 * self.a

def menu():
	print('\n--- Shape Calculator ---')
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End of menu function

def operation(s):
	s.get() # Read inputs
	
	if not s.test():
		return # Stop execution if test fails

	print(f'Area : {s.area():.2f}') # Call s.area()
	print(f'Perimeter : {s.peri():.2f}') # Call s.peri()
# End of the function

while True:
	menu()
	try:
	
		ch = int(input('Enter choice : ')) 
	except ValueError:
		print("Invalid choice. Please enter a number between 1 and 5.")
		continue
	
	s = None
	match ch:
		case 1:
				s = triangle()
				operation(s)
		case 2:
				s = circle()
				operation(s)
		case 3:
				s = rectangle()
				operation(s)
		case 4:
				s = square()
				operation(s)
		case 5:
				sys.exit(0) # How to stop execution
		case _:
				print("Invalid choice. Please enter a number between 1 and 5.")
	# End of match
# End of while loop
print('Good Bye')





#9. Abstract Base Classes (Inheritance Chain)

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
		print('m1 method of child class')
class gc(child):
	def m2(self):
		print('m2 method of gc class')
class ggc(gc):
	def m3(self):
		print('m3 method of ggc class')
# End of the class
a = ggc()
a . m1()
a . m2()
a . m3()
parent() # Error
child() # Error
gc() # Error
'''
The output will be:

m1 method of child class
m2 method of gc class
m3 method of ggc class
Traceback (most recent call last):
  ...
TypeError: Can't instantiate abstract class parent with abstract methods m1, m2, m3
'''






# 10. Circular Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    def length(self):
        if self.head is None:
            return 0
        
        count = 0
        current = self.head
        
        # Traverse until we return to the head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

if __name__ == '__main__':
    # How to create circular linked list
    a = cll()
    # Create nodes: 10 -> 20 -> 30 -> (back to 10)
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    
    a.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n1  # Make it circular
    
    print('Number of nodes : ' , a.length())
    # Output: Number of nodes : 3




# 11. Method to find data of the $i$-th node

class Node:
    pass

class circular_linked_list(cll):
	
    def length(self):
        # Implementation from Program 9
        if self.head is None:
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def find(self, i):
        # i is 1-based index
        if self.head is None or i <= 0 or i > self.length():
            return None # Index out of range or empty list
        
        current = self.head
        # Traverse i-1 times
        for _ in range(i - 1):
            current = current.next
        
        return current.data # Return data of ith node

# Example setup for demonstration: 10 -> 20 -> 30 -> (back to 10)
cll_obj = circular_linked_list()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
cll_obj.head = n1
n1.next = n2
n2.next = n3
n3.next = n1

while True:
	try:
		i = int(input("Enter value of 'i': "))
	except ValueError:
		print("Invalid input.")
		continue
        
	x = cll_obj.find(i) # Obtain data of ith node
    
	if x is None: # if x is None
		print(F'Node {i} does not exist')
	else:
		print(F'Data of node {i} is : {x}')
        
	ch = input('Do you wish to continue (y / n) : ')
	if ch.lower() == 'n':
			break
print('Good Bye')





# 12. Method to search for a value

class Node:
    # ... (Node definition)
    pass

class circular_linked_list(cll):
	def search(self, x):
        if self.head is None:
            return None # Empty list
            
        current = self.head
        # Traverse until we complete a full circle
        while True:
            if current.data == x:
                return current # Return the node when 'x' is found
            
            current = current.next
            if current == self.head:
                break # Completed the loop without finding 'x'
                
        return None # Not found

# Example setup (Assuming cll_obj is created and populated as before)
cll_obj = circular_linked_list()
# Populate cll_obj...

while True:
	x = eval(input("Enter value to be searched : "))
	found_node = cll_obj.search(x) # Search for 'x' in the linked list
    
	if found_node is None: # if found_node is None
		print(F'{x} is not found')
	else:
		print(F'Found at address : {hex(id(found_node))} ') # Address of the node
        
	ch = input('Do you wish to continue (y / n) : ')
	if ch.lower() == 'n':
			break
print('Good Bye')





# 13. Method to insert a node

class Node:
    pass

class circular_linked_list(cll):
    def length(self): 
        # ... (length implementation)
        return 3 # Placeholder for a realistic length check
        
    def get_node_at(self, i):
        # Helper to get the actual node at index i (1-based)
        if self.head is None or i <= 0 or i > self.length():
            return None
        current = self.head
        for _ in range(i - 1):
            current = current.next
        return current

    def insert(self, i, x):
        new_node = Node(x) # How to create a new node
        list_length = self.length()

        if i < 0 or i > list_length + 1:
             # invalid node number: i must be between 0 (for beginning) and length+1 (for end/after last)
             print(F'Node {i} is an invalid insertion point.')
             return
             
        elif self.head is None: # cll is empty
            self.head = new_node
            new_node.next = self.head # Insert a node into empty cll
            return
            
        elif i == 1: # insertion at the beginning (before head)
            current = self.head
            # Find the last node (the one pointing to head)
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node # New node becomes the head
            return
            
        else: # Insertion after a node (i-th node means after the node at position i)
            # Find the node just before the insertion point (node at i-1)
            prev_node = self.get_node_at(i-1) # get_node_at is a helper
            
            if prev_node is None:
                 print(F'Node {i-1} does not exist to insert after.')
                 return # Should not happen if i is validated properly
            
            new_node.next = prev_node.next
            prev_node.next = new_node
            return

    def print_list(self):
        if self.head is None:
            print("[]")
            return
        
        current = self.head
        print("[", end="")
        while True:
            print(f"{current.data}", end="")
            current = current.next
            if current == self.head:
                break
            print(" -> ", end="")
        print("]")

# Example setup (initial list: 10 -> 20 -> 30)
cll_obj = circular_linked_list()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
cll_obj.head = n1
n1.next = n2
n2.next = n3
n3.next = n1

while True:
	try:
		i = int(input("Enter value of 'i' (position to insert *before*): "))
		x = eval(input('Enter value to be inserted : '))
	except ValueError:
		print("Invalid input.")
		continue
        
	cll_obj.insert(i, x) # Insert 'x' at position i
    
	cll_obj.print_list() # Print linked list
    
	ch = input('Would you like to insert another node (Y or N) ? : ')
	if ch.lower() == 'n':
		break




# 14. Method to delete $i$-th node

class Node:
    # ... (Node definition)
    pass

class circular_linked_list(cll):
    # Assume length() and get_node_at() are implemented
    def length(self):
        # ... (length implementation)
        return 3 # Placeholder
    
    def delete(self, i):
        list_length = self.length()
        
        if self.head is None or i <= 0 or i > list_length:
            return None # 'i' is an invalid node number
            
        deleted_data = None

        if list_length == 1: # cll has single node
            deleted_data = self.head.data
            self.head.next = None
            self.head = None # Delete the single node and return data
            return deleted_data

        elif i == 1: # deletion of first node
            deleted_data = self.head.data
            current = self.head
            # Find the last node
            while current.next != self.head:
                current = current.next
                
            current.next = self.head.next
            self.head = self.head.next # Delete the fist node and return data
            return deleted_data

        else: # Deletion of the i-th node
            # Find the node just before the i-th node
            prev_node = self.head
            for _ in range(i - 2):
                prev_node = prev_node.next
                
            node_to_delete = prev_node.next
            deleted_data = node_to_delete.data
            
            prev_node.next = node_to_delete.next # Bypass and delete ith node
            return deleted_data


# Example setup (initial list: 10 -> 20 -> 30)
cll_obj = circular_linked_list()
# Populate cll_obj...

while True:
	try:
		i = int(input('Enter value of i (position to delete) : '))
	except ValueError:
		print("Invalid input.")
		continue
        
	x = cll_obj.delete(i) # Delete ith node
    
	if x is None: # if x is None
			print(F'Node {i} does not exist')
	else:
			print('Data of deleted node is ' , x)
            
	cll_obj.print_list() # Print linked list
    
	ch = input('Would you like to delete another node (Y or N) ? : ')
	if ch.lower() == 'n':
		break





# 15. Destructor to delete whole linked list

class Node:
    # ... (Node definition)
    pass

class circular_linked_list(cll):
    def __init__(self):
        self.head = None

    def __del__(self): # Write destructor to delete whole linked list
        if self.head is None:
            print('Linked list is already empty')
        else:
            
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = None # Break the circular link
            self.head = None # Delete each node of cll (by making them garbage collectable)
            print('Linked list is empty')

# Example setup
cll_obj = circular_linked_list()
del cll_obj 





# 16. Method to copy a linked list

class Node:
    pass

class circular_linked_list(cll):
    def __init__(self):
        self.head = None

    def copy(self):
        b = circular_linked_list() 
        
        if self.head is None: # if input cll is empty
            # output cll is empty (b.head is already None)
            return b 
        
        # 1. Create the first node
        new_head = Node(self.head.data)
        b.head = new_head
        b.head.next = b.head # Make it circular initially
        
        # Use tail pointer for efficient appending
        tail = b.head 
        
        current = self.head.next
        

        while current != self.head:
            new_node = Node(current.data)

            tail.next = new_node
            new_node.next = b.head 
            tail = new_node 
            
            current = current.next
        
        return b # return output cll

    # Assume print_list() is available

# Example setup 
cll_input = circular_linked_list()
# Populate cll_input...
cll_output = cll_input.copy() # How to copy linked list

print('Input cll : ', end='')
cll_input.print_list() # How to print input cll
print('Output cll : ', end='')
cll_output.print_list() # How to print output cll





# 17. Doubly Linked List Implementation

class node:
	def __init__(self, x): 
		self.data = x
		self.prev = None # Left pointer
		self.next = None # Right pointer

class linkedlist: # Assuming this class manages the DLL
	def __init__(self): # How to add 'l' and 'r' to object 'a'
		self.l = None # Leftmost node (head)
		self.r = None # Rightmost node (tail)

	def isempty(self): # return True when dll is empty and False otherwise
		return self.l is None # or self.r is None

	def disp_left_right(self): # print data field of each node from left to right
		if self.isempty():
			print('Linked List is empty')
			return
		
		current = self.l
		while current is not None:
			print(current.data, end=' ')
			current = current.next
		print()

	def disp_right_left(self): # print data field of each node from right to left
		if self.isempty():
			print('Linked List is empty')
			return
			
		current = self.r
		while current is not None:
			print(current.data, end=' ')
			current = current.prev
		print()

	def append(self, new_node):
		if self.isempty(): # dll is empty
			self.l = new_node
			self.r = new_node # Append new node to empty dll
		else:
			self.r.next = new_node
			new_node.prev = self.r
			self.r = new_node # Append new node to existing dll

	def create(self): # How to create dll i.e. Append each node to dll
		while True:
			try:
				x = eval(input('Enter data to append (or type "0" to stop): '))
			except:
				print("Invalid input.")
				continue
				
			if x == 0:
				break
			
			new_node = node(x)
			self.append(new_node)

if __name__ == '__main__':
	dll = linkedlist() # How to create dll
	print('Creating DLL...')
	dll.create()
    
	print('Linked List from left to right : ' , end = '')
	dll.disp_left_right()     
	print('Linked List from right to left : ' , end = '')
	dll.disp_right_left()



0
