: #  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1()    ### Overridden Method
x = child()
x . m1()  ### Overriding Method







: # Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
#end of the class
x = parent()
x . m1()
x . m2()
x . m3() ### AttributeError: 'parent' object has no attribute 'm3'
x = child()
x . m1()
x . m2()
x . m3()









: # Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()
		print(' + Entertainment')
#end of the class
c = child()
c . marriage()
c . property()
c . study()

######################
Love Marriage
One  Crore
Studies only	 + Entertainment






: # Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30))    ########### 60
print(c . add(10 , 20))         ########### Error
print(super(child , c) . add(40,50)) ###### Error





: # Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
#End  of  the  class
c = child()
print(c . add(10 , 20 , 30))  ### 60
print(c . add(10 , 20))       ### 33





: #Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)
c . m1(30 , 40)
#######################
child  method  --->  x  :  10  	y  :  20
child  method  --->  x  :  30  	y  :  40





: # Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  _init_(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  _init_(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  _init_(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  _init_(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  _init_(slef):
		print('c1  class  constructor')
# End  of  the  class
c1()
c2()
c3()
c4()
c5()

###########################
| Object | Result  | Reason                                            |
| :----- | :------ | :------------------------------------------------ |
| `c1()` |  Error | Abstract class (has unimplemented `m1`)           |
| `c2()` |  Works | Not abstract, constructor misspelled → no message |
| `c3()` |  Works | Not subclass of ABC, `_init_` misspelled          |
| `c4()` |  Works | Implements `m1()`, `_init_` misspelled            |
| `c5()` |  Error | Still abstract (no `m1()` implementation)         |





: '''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  ---> sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  ---> a * b  where  'a'  is  length and  'b'  is  breadth
     What  is  the  perimter  of  rectangle ?  --->2 * (a + b)

5) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square  ?  ---> 4 * a
'''
import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		 How  to  read  value  of  'a'
	@abstractmethod
	def   area(self):
		pass
	@abstractmethod
	def  peri(self):
		pass
	@abstractmethod
	def  test(self):
		pass
class  triangle(shape):
	def   get(self):
		print('Enter  3  sides  of  triangle')
		How  to  read  the  3  sides  of  triangle
	def   area(self):
		return   area  of  triangle
	def   peri(self):
		return  perimeter  of  triangle
	def   test(self):
		if  sum  of  every  2  sides  should  be  >   3rd   side
				do  nothing
		else:
			print('Not    a  triangle')
			How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		How  to  read  radius
	def   area(self):
		return  area  of  circle
	def   peri(self):
		return  circumference  of circle
	def  test(self):
		if  side  is  -ve
		    print('Radius  can  not  be  -ve')
		    How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		How  to  read  length  and  breadt
	def   area(self):
		return  area  of  rectangle
	def   peri(self):
		return  perimeter  of  triangle
	def  test(self):
		if  length  and   breadth  same
		    print('Not  a rectangle')
		    How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		How  to  read  the  side
	def   area(self):
		return  area  of  square
	def   peri(self):
		return  perimeter  of  square
	def  test(self):
		pass
def   menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End  of  menu  function
def   operation(s):
	How  to  read  inputs  to  object  's'
	How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  ???)
	print('Perimeter  :  ' ,  ???)
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				How  to  call  operation()  function
		case  2:
				How  to  call  operation()  function
		case  3:
				How  to  call  operation()  function
		case  4:
				How  to  call  operation()  function
		case  5:
				How  to  stop  execution
	# End  of  match
# End of while  loop
print('Good  Bye')

########################

import math
from abc import *

# ---------- Abstract Parent Class ----------
class shape(ABC):
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


# ---------- Child Class: Triangle ----------
class triangle(shape):
    def get(self):
        print('Enter 3 sides of triangle:')
        self.a = float(input('a : '))
        self.b = float(input('b : '))
        self.c = float(input('c : '))

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c

    def test(self):
        # Triangle validity check
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass
        else:
            print('Not a valid triangle')
            exit()


# ---------- Child Class: Circle ----------
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
            print('Radius cannot be negative')
            exit()


# ---------- Child Class: Rectangle ----------
class rectangle(shape):
    def get(self):
        print('Enter length and breadth of rectangle:')
        self.a = float(input('Length : '))
        self.b = float(input('Breadth : '))

    def area(self):
        return self.a * self.b

    def peri(self):
        return 2 * (self.a + self.b)

    def test(self):
        if self.a == self.b:
            print('Not a rectangle (both sides are same)')
            exit()


# ---------- Child Class: Square ----------
class square(shape):
    def get(self):
        print('Enter any side of square : ', end='\t')
        self.a = float(input())

    def area(self):
        return self.a ** 2

    def peri(self):
        return 4 * self.a

    def test(self):
        if self.a <= 0:
            print('Side must be positive')
            exit()


# ---------- Menu Function ----------
def menu():
    print('\n1. Triangle')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Exit')


# ---------- Operation Function ----------
def operation(s):
    s.get()          # Read inputs
    s.test()         # Validate inputs
    print('Area       : ', s.area())
    print('Perimeter  : ', s.peri())


# ---------- Main Program ----------
while True:
    menu()
    ch = int(input('Enter choice : '))
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
            print('Good Bye')
            exit()
        case _:
            print('Invalid choice')






: # Find  outputs (Home  work)
from   abc    import    *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m1()
a . m2()
a . m3()
parent()
child()
gc()
################
m1  method  of  child  class
m2  method  of    gc  class
m3  method  of  ggc  class
TypeError: Can't instantiate abstract class parent with abstract methods m1, m2, m3




: #  Write  a  method  to  determine  length  of  circular  linked  list
class  cll(linkedlist):
	def  length(a):
			How  to  return  number  of  nodes  in  circular  linked  list
# End  of  the  class
if  _name_  ==  '_main_':
	How  to   create  circular  linked   list
	print('Number  of  nodes : ' , ???)

#############################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None


class cll(linkedlist):
    def length(self):
        # If list is empty
        if self.head is None:
            return 0

        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count


if __name__ == '__main__':
    # ---------- Create Circular Linked List ----------
    L = cll()
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)

    # Link nodes
    L.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = L.head  # last node points to head

    print('Number of nodes :', L.length())






: class  circular_linked_list(cll):
	def  find(a , i):
			return   data  of  ith  node  and  None  when  ith  node  does  not  exist
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	How  to  obtain  data  of  ith  node
	if  ???
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {x}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

############################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class cll:
    def __init__(self):
        self.head = None


class circular_linked_list(cll):
    def find(self, i):
        # if list empty
        if self.head is None:
            return None

        temp = self.head
        count = 1

        # Traverse until we reach ith node or come back to head
        while True:
            if count == i:
                return temp.data
            temp = temp.next
            count += 1
            if temp == self.head:     # came full circle
                break

        # if i exceeds length
        return None


# ---------- Create circular linked list ----------
L = circular_linked_list()

# create nodes manually
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

L.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = L.head    # last node connects back to head


# ---------- Main Loop ----------
while True:
    i = int(input("Enter value of 'i':  "))
    x = L.find(i)  # get data of ith node
    if x is None:
        print(f'Node {i} does not exist')
    else:
        print(f'Data of node {i} is : {x}')

    ch = input('Do you wish to continue (y / n):  ')
    if ch in ('n', 'N'):
        break

print('Good Bye')




: # Write  a  method  to  search  for  a  value  in  the  linked  list.
class  circular_linked_list(linkedlist):
	def  search(a , x):
			How  to   return  the  node  when  'x'  is   found  in  the  linked  list  and  None  otherwise
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	How  to  search  for  'x'  in  the  linked  list
	if ??
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  ??? ')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

#############################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None


class circular_linked_list(linkedlist):
    def search(self, x):
        # If list is empty
        if self.head is None:
            return None

        temp = self.head
        while True:
            if temp.data == x:
                return temp          # return node address
            temp = temp.next
            if temp == self.head:    # came back to start
                break

        return None


# ---------- Create circular linked list ----------
L = circular_linked_list()

# Create nodes manually
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

L.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = L.head   # make circular


# ---------- Main loop ----------
while True:
    x = eval(input("Enter value to be searched: "))
    node = L.search(x)

    if node is None:
        print(f'{x} is not found')
    else:
        print(f'Found at address: {id(node)}')   # print memory address

    ch = input('Do you wish to continue (y / n): ')
    if ch in ('n', 'N'):
        break

print('Good Bye')







: #  Write  a  method  to  insert  a  node  in  the  linked  list
class  circular_linked_list(cll):
	def  insert(a , i , x):
		if  'i'  is  an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  cll  is  empty:
				How  to  create  a  new  node
				How  to  insert  a  node  into  empty  cll
		elif  insertion  at  the  begining:
				How  to  create  a  new  node
				How  to  insert  a  node  at  the  begining  of  cll
		else:
			How  to  create  a  new  node
			How  to  insert  a  node  after  ith  node  of  cll
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	How  to  insert  'x'  after  ith  node
	How  to  print linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
##################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class cll:
    def __init__(self):
        self.head = None

    # method to display circular linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")


class circular_linked_list(cll):
    def length(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def insert(self, i, x):
        n = self.length()

        # invalid node number
        if i < 0 or i > n:
            print(f'Node {i} does not exist')
            return

        new_node = Node(x)

        # insertion into empty list
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        # insertion at beginning
        if i == 0:
            temp = self.head
            # go to last node
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        # insertion after ith node
        temp = self.head
        count = 0
        while count < i - 1:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node


# ----------- Create circular linked list -----------
L = circular_linked_list()

# Manually create initial circular linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
L.head = n1
n1.next = n2
n2.next = n3
n3.next = L.head  # make it circular

print("Initial Circular Linked List:")
L.display()

# ----------- Insert Loop -----------
while True:
    i = int(input("Enter value of 'i' : "))
    x = eval(input("Enter value to be inserted : "))
    L.insert(i, x)
    print("Circular Linked List after insertion:")
    L.display()
    ch = input("Would you like to insert another node (Y or N)? : ")
    if ch in ('n', 'N'):
        break

print("Good Bye")






: # Write  a  method  to  delete  ith  node  of  linked  list
class  circular_linked_list(cll):
	def  delete(a , i):
		if  'i'  is  an  invalid  node  number:
				return  None
		elif  cll  has  single  node
				How  to  delete  the  single  node  and  return  data  of  deleted  node
		elif  deletion  of  first  node:
				How  to  delete  the  fist  node  and  return  data  of  deleted  node
		else:
			How  to  delete  ith  node  and  return  data  of  deleted  node
# End  of  the  class
How  to   create  circular  linked   list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	How  to  delete   ith  node
	if  ???
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  x)
	How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break

###################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class cll:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

    def length(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count


class circular_linked_list(cll):
    def delete(self, i):
        n = self.length()

        # Invalid position
        if i <= 0 or i > n:
            return None

        # Case 1: Only one node
        if n == 1:
            x = self.head.data
            self.head = None
            return x

        # Case 2: Delete first node
        if i == 1:
            temp = self.head
            # move to last node
            while temp.next != self.head:
                temp = temp.next
            x = self.head.data
            self.head = self.head.next
            temp.next = self.head
            return x

        # Case 3: Delete ith node (other than first)
        temp = self.head
        count = 1
        while count < i - 1:
            temp = temp.next
            count += 1
        x = temp.next.data
        temp.next = temp.next.next
        return x


# -------- Create circular linked list --------
L = circular_linked_list()

# Manually create initial CLL
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
L.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = L.head  # make it circular

print("Initial Circular Linked List:")
L.display()

# -------- Delete Loop --------
while True:
    i = int(input("Enter value of i : "))
    x = L.delete(i)
    if x is None:
        print(f"Node {i} does not exist")
    else:
        print("Data of deleted node is", x)
    print("Circular Linked List after deletion:")
    L.display()
    ch = input("Would you like to delete another node (Y or N)? : ")
    if ch in ('n', 'N'):
        break

print("Good Bye")





: #  Tricky 
#  Write  destructor  to  delete  whole  linked  list
class  circular_linked_list(linkedlist):
	def    _del_(a):
			if  linked  list  is  empty:
					print('Linked  list  is  already  empty')
			else:
					How  to  delete  each  node  of  cll
					print('Linked  list  is  empty')
#  End  of  the  clas
How  to   create  circular  linked   list

################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None


class circular_linked_list(linkedlist):
    def __del__(self):
        if self.head is None:
            print("Linked list is already empty")
            return

        print("Deleting nodes from circular linked list...")
        temp = self.head
        while True:
            next_node = temp.next        # store next node
            print(f"Deleting node with data: {temp.data}")
            temp.next = None             # break the link
            del temp                     # delete the current node
            if next_node == self.head:   # if we reached back to head, stop
                break
            temp = next_node

        self.head = None
        print("Linked list is empty")

# -------- Create circular linked list --------
L = circular_linked_list()

# Manually create circular linked list
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

L.head = n1
n1.next = n2
n2.next = n3
n3.next = L.head   # make circular

print("Circular linked list created with nodes: 10 -> 20 -> 30 -> (back to head)")

# Delete the linked list manually
del L

print("End of program")








: #  Write  a  method  to  copy  a  linked  list
class  circular_linked_list(linkedlist):
	def  copy(a):
		How  to  create  a  new  cll object  to  hold  the  result
		if  input  cll  is  empty
			output  cll  is   empty
		else:
			How  to  copy  each  node  of  cll  held  by  object  'a'  to 'b'
			# End  of  while  loop
		return  output  cll
#  End  of  the  clas
How  to   create  circular  linked   list
How  to  copy  linked  list
How  to  print  input  cll
How  to  print  output  cll

####################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")


class circular_linked_list(linkedlist):
    def copy(self):
        # Create a new CLL to hold the result
        b = circular_linked_list()

        if self.head is None:
            print("Input circular linked list is empty")
            return b

        # Copy each node
        temp = self.head
        while True:
            # Create a new node and append to b
            new_node = Node(temp.data)

            if b.head is None:
                b.head = new_node
                new_node.next = new_node
                last = new_node
            else:
                last.next = new_node
                new_node.next = b.head
                last = new_node

            temp = temp.next
            if temp == self.head:
                break

        return b


# -------- Create input circular linked list ----------
cll1 = circular_linked_list()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
cll1.head = n1
n1.next = n2
n2.next = n3
n3.next = cll1.head

print("Input circular linked list:")
cll1.display()

# Copy the circular linked list
cll2 = cll1.copy()
print("Copied circular linked list:")
cll2.display()






: #  Write  methods  to  create  and  print  linked  list
class  node:
		def   _init_(new  , x):
				How   to   add  data  field  to   new  node  with  'x'
		# new  = node(25)
class  linkedlist:
		def   _init_(a):
				How  to  add  'l'  and  'r'  to  object  'a'
		# a = linkedlist()
		def  isempty(a):
				return  True  when  dll  is  empty  and  False  otherwise
		# a . isempty()  --->  True / False
		def  disp_left_right(a):
				if  dll  is  empty:
						print('Linked  List  is  empty')
				else:
						How  to  print  data  field  of  each  node  from  left  to  right  in  same  line
		def  disp_right_left(a):
				if  dll  is  empty:
						print('Linked  List  is  empty')
				else:
						How  to  print  data  field  of  each  node  from  right  to  left  in  same  line
		def  append(a , new):
				if  dll  is  empty:
						How  to  append  new  node  to  empty  dll
				else:
						How  to append  new  node  to  existing  dll
		def  create(a):
				How  to   create  dll  i.e.  Append   each  node  to  dll
# End  of  the  class
if  _name_ == '_main_':
	How  to  create  dll
	print('Linked  List   from  left  to  right  :  ' , end = '')
	How  to  print  dll  from  left  to  right
	print('Linked  List   from  right  to  left  :  ' , end = '')
	How  to  print  dll  from  right  to  left


##########################################

class Node:
    def __init__(self, x):
        self.data = x
        self.l = None  # left pointer
        self.r = None  # right pointer


class linkedlist:
    def __init__(self):
        self.head = None

    def isempty(self):
        return self.head is None

    def disp_left_right(self):
        if self.isempty():
            print("Linked List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.r
        print()

    def disp_right_left(self):
        if self.isempty():
            print("Linked List is empty")
            return
        temp = self.head
        # Go to last node
        while temp.r:
            temp = temp.r
        # Traverse backward
        while temp:
            print(temp.data, end=" ")
            temp = temp.l
        print()

    def append(self, new):
        if self.isempty():
            self.head = new
        else:
            temp = self.head
            while temp.r:
                temp = temp.r
            temp.r = new
            new.l = temp

    def create(self, data_list):
        for x in data_list:
            new_node = Node(x)
            self.append(new_node)


# ---------- Main ----------
if __name__ == "__main__":
    dll = linkedlist()
    data = [10, 20, 30, 40]
    dll.create(data)

    print("Linked List from left to right: ", end="")
    dll.disp_left_right()

    print("Linked List from right to left: ", end="")
    dll.disp_right_left()
