                                           NAME:M.SAICHARAN             HOMEWORK
                                           DATE:22-10-2025


1)Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1()#overridden
x = child()
x . m1()#overriding


2)Find  outputs   (Home  work)
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
x . m1()#m1 method of parent class
x . m2()#m2 method of parent class
x . m3()#error
x = child()
x . m1()#m1 method of child class
x . m2()#m2 method of parent class
x . m3()#m3 method of child class


3)# Find  outputs  (Home  work)
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
c . marriage()#Arranged marriage
c . property()#one crore
c . study()#studies only + entertainment


4)# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30))#60
print(c . add(10 , 20))#error
print(super(child , c) . add(40,50))#90


5)# Find  outputs  (Home  work)
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
print(c . add(10 , 20 , 30))#33
print(c . add(10 , 20))#33


6)#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)#x:10 y:20
c . m1(30 , 40)#x:30 y:40


7)# Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(slef):
		print('c1  class  constructor')
# End  of  the  class
c1()#error
c2()#c2 class constructor
c3()#c3 class constructor
c4()#c4 class constructor
c5()#c1 class constructor


8)'''
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
#Program:
import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		self.a=float(input('Enter side')) #How  to  read  value  of  'a'
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
		super().get() 	#How  to  read  the  3  sides  of  triangle
		self.b=float(input('Enter side'))
		self.c=float(input('Enter side'))
	def   area(self):
		s = (self.a + self.b + self.c) / 2
		return  math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) #  area  of  triangle
	def   peri(self):
		return self.a + self.b + self.c 	# perimeter  of  triangle
	def   test(self):
		if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
			pass 	# sum  of  every  2  sides  should  be  >   3rd   side do  nothing
		else:
			print('Not    a  triangle')
			exit() 	#How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		super().get() 	#How  to  read  radius
	def   area(self):
		return  math.pi* self.a ** 2 	#area  of  circle
	def   peri(self):
		return 2 * math.pi * self.a		# circumference  of circle
	def  test(self):
		if  self.a < 0:  	#side  is  -ve
			print('Radius  can  not  be  -ve')
			exit() 	#How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		super.get()	 #How  to  read  length  and  breadth
		self.b=float(input('Enter breadth'))
	def   area(self):
		return self.a * self.b		# area  of  rectangle
	def   peri(self):
		return  2 * (self.a + self.b)		#perimeter  of  triangle
	def  test(self):
		if self.a == self.b:	# length  and   breadth  same
			print('Not  a rectangle')
			exit() #How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		super().get()		#How  to  read  the  side
	def   area(self):
		return  self.a**2 #area  of  square
	def   peri(self):
		return  4* self.a  #perimeter  of  square
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
	s.get()  	#How  to  read  inputs  to  object  's'
	s.test()	#How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  s.area())
	print('Perimeter  :  ' , s.peri())
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				operation(triangle()) #How  to  call  operation()  function
		case  2:
				operation(circle()) 	#How  to  call  operation()  function
		case  3:
				operation(rectangle()) 	#How  to  call  operation()  function
		case  4:
				operation(square())	#How  to  call  operation()  function
		case  5:
				break	#How  to  stop  execution
	# End  of  match
# End of while  loop
print('Good  Bye')


9)# Find  outputs (Home  work)
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
a . m1()#m1 method of child class
a . m2()#m2 method of gc class
a . m3()#m3 method of ggc class
parent()#error
child()#error
gc()#error

                                                          
                                                                DATA STRUCTURES

1)#  Write  a  method  to  determine  length  of  circular  linked  list
class  cll(linkedlist):
	def  length(a):
			How  to  return  number  of  nodes  in  circular  linked  list
# End  of  the  class
if  _name_  ==  '_main_':
	How  to   create  circular  linked   list
	print('Number  of  nodes : ' , ???)

#Program:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count
cll = CircularLinkedList()
n = int(input("Enter number of nodes: "))
for i in range(n):
    value = input(f"Enter value for node {i+1}: ")
    cll.append(value)
print("Number of nodes in circular linked list:", cll.length())


2)
class  circular_linked_list(cll):
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

#Program:
class circular_linked_list(cll):
    def find(a, i):
        if not a.head or i <= 0:
            return None
        temp = a.head
        count = 1
        while count < i:
            temp = temp.next
            if temp == a.head:
                return None
            count += 1
        return temp.data
# End of the class
cl = circular_linked_list()
n = int(input("Enter number of nodes: "))
for j in range(n):
    value = input(f"Enter value for node {j+1}: ")
    cl.append(value)
while True:
    i = int(input("Enter value of 'i': "))
    x = cl.find(i)
    if x is None:
        print(f'Node {i} does not exist')
    else:
        print(f'Data of node {i} is : {x}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
# End of while loop
print('Good Bye')


3)
# Write  a  method  to  search  for  a  value  in  the  linked  list.
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

#Program:
class circular_linked_list(linkedlist):
    def search(a, x):
        if not a.head:
            return None
        temp = a.head
        while True:
            if temp.data == x:
                return temp
            temp = temp.next
            if temp == a.head:
                break
        return None
cl = circular_linked_list()
n = int(input("Enter number of nodes: "))
for i in range(n):
    value = eval(input(f"Enter value for node {i+1}: "))
    cl.append(value)
while True:
    x = eval(input("Enter value to be searched : "))
    node = cl.search(x)
    if node is None:
        print(f'{x} is not found')
    else:
        print(f'Found at address : {id(node)}')
    ch = input('Do you wish to continue (y / n) : ')
    if ch == 'N' or ch == 'n':
        break
print('Good Bye')


4)
#  Write  a  method  to  insert  a  node  in  the  linked  list
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

#Program:
class circular_linked_list(cll):
    def insert(a, i, x):
        if i < 0:
            print(F'Node {i} does not exist')
        elif a.head is None:
            new_node = Node(x)
            a.head = new_node
            new_node.next = new_node
        elif i == 0:
            new_node = Node(x)
            temp = a.head
            while temp.next != a.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = a.head
            a.head = new_node
        else:
            new_node = Node(x)
            temp = a.head
            count = 0
            while count < i and temp.next != a.head:
                temp = temp.next
                count += 1
            if count != i:
                print(F'Node {i} does not exist')
                return
            new_node.next = temp.next
            temp.next = new_node
cl = circular_linked_list()
n = int(input("Enter number of nodes: "))
for j in range(n):
    value = eval(input(f"Enter value for node {j+1}: "))
    cl.append(value)
while True:
    i = int(input("Enter value of 'i' : "))
    x = eval(input('Enter value to be inserted : '))
    # --- How to insert 'x' after ith node ---
    cl.insert(i, x)
    temp = cl.head
    if temp is None:
        print("List is empty")
    else:
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == cl.head:
                break
        print("(back to head)")
    ch = input('Would you like to insert another node (Y or N) ? : ')
    if ch == 'n' or ch == 'N':
        break
print('Good Bye')


5)
# Write  a  method  to  delete  ith  node  of  linked  list
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

#Program:
class  circular_linked_list(cll):
	def  delete(a , i):
		if  a.head  is  None  or  i  <  0:
				return  None
		elif  a.head.next  ==  a.head  and  i  ==  0:
				data = a.head.data
				a.head = None
				return data
		elif  i  ==  0:
				temp = a.head
				data = temp.data
				last = a.head
				while  last.next  !=  a.head:
					last = last.next
				last.next = a.head.next
				a.head = a.head.next
				return data
		else:
			temp = a.head
			count = 0
			while  count  <  i - 1  and  temp.next  !=  a.head:
					temp = temp.next
					count += 1
			if  temp.next  ==  a.head:
					return None
			data = temp.next.data
			temp.next = temp.next.next
			return data
cl = circular_linked_list()
n = int(input("Enter number of nodes: "))
for j in range(n):
	value = eval(input(f"Enter value for node {j+1}: "))
	cl.append(value)

while  True:
	i = int(input('Enter  value  of  i  :  '))
	# How  to  delete   ith  node
	x = cl.delete(i)
	if  x  is  None:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  x)
	temp = cl.head
	if  temp  is  None:
		print("List is empty")
	else:
		while  True:
			print(temp.data , end=" -> ")
			temp = temp.next
			if  temp  ==  cl.head:
				break
			print("(back to head)")
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch  ==  'n'  or  ch  ==  'N':
		break

6.#  Tricky program
#  Write  destructor  to  delete  whole  linked  list
class  circular_linked_list(linkedlist):
	def    __del__(a):
			if  linked  list  is  empty:
					print('Linked  list  is  already  empty')
			else:
					How  to  delete  each  node  of  cll
					print('Linked  list  is  empty')
#  End  of  the  clas
How  to   create  circular  linked   list

#Program:
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def __del__(self):
        print("Destructor called: Deleting Circular Linked List")
        if self.head is None:
            print("Linked list is already empty")
            return
        temp = self.head
        while temp.next != self.head:
            next_node = temp.next
            print(f"Deleting node: {temp.data}")
            temp.next = None 
            temp = next_node
        print(f"Deleting last node: {temp.data}")
        temp.next = None
        self.head = None
        print("Linked list is now empty")



7.#  Write  a  method  to  copy  a  linked  list
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

#Program:
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end to build circular linked list
    def insert_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    # Display circular linked list
    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def copy(self):
        copy_cll = CircularLinkedList()  

        if self.head is None:
            return copy_cll 

        temp = self.head
        while True:
            copy_cll.insert_end(temp.data) 
            temp = temp.next
            if temp == self.head:
                break

        return copy_cll



8.#  Write  methods  to  create  and  print  linked  list
#Program:
class node:
    def __init__(new, x):
        new.data = x             
        new.prev = None           
        new.next = None           


class linkedlist:
    def __init__(a):
        a.l = None  
        a.r = None  

    def isempty(a):
        return a.l is None  

    def disp_left_right(a):
        if a.isempty():
            print("Linked List is empty")
        else:
            temp = a.l
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next

    def disp_right_left(a):
        if a.isempty():
            print("Linked List is empty")
        else:
            temp = a.r
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.prev

    def append(a, new):
        if a.isempty():  
            a.l = a.r = new
        else:           
            a.r.next = new
            new.prev = a.r
            a.r = new

    def create(a):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            x = int(input(f"Enter data for node {i+1}: "))
            new = node(x)
            a.append(new)

if __name__ == '__main__':
    dll = linkedlist()   
    dll.create()        

    print("Linked List from left to right: ", end='')
    dll.disp_left_right()

    print("\nLinked List from right to left: ", end='')
    dll.disp_right_left()


