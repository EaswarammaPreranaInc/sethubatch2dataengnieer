#Tarun Banala                    06-10-2025
# Find  outputs  (Home work)
class   c1:
	def   _init_(self , y):  # Incorrect constructor name (should be __init__)
		self . x = y  # Sets instance attribute x to y
	def    _ge_(m , n):  # Incorrect greater than or equal method name
		print('_ge_ method :  ' , m . x , n . x)  # Prints values being compared
		return  m . x > n . x  # Returns True if m.x > n.x (should be >= for _ge_)
# End  of  the  class
a = c1(10)  # Creates object a with x=10 (constructor won't work properly)
b = c1(20)  # Creates object b with x=20 (constructor won't work properly)
print(a >= b)  # Will raise AttributeError due to missing proper constructor
print(a <= b)  # Will raise AttributeError due to missing proper constructor

# Find  outputs  (Home  work)
class   c1:
        def   _init_(self , y):  # Incorrect constructor name
                self . x = y  # Sets instance attribute x
        def    _eq_(m , n):  # Incorrect equality method name
                print('_eq_ method  : ' , m . x , n . x)  # Prints values being compared
                return  m . x == n . x  # Returns True if values are equal
#end of the class
a = c1(10)  # Creates object a (constructor won't work)
b = c1(20)  # Creates object b (constructor won't work)
print(a != b)  # Calls __ne__ which defaults to not __eq__ (will error)
print(a == b)  # Will error due to missing proper constructor

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):  # Incorrect constructor name
		self . x = y  # Sets instance attribute
	def    _eq_(m , n):  # Incorrect equality method name
		print('_eq_ method  :  ' , m . x , n . x)  # Prints compared values
		# Missing return statement - returns None by default
#end of the class
a = c1(25)  # Creates object a
b = c1(25)  # Creates object b
print(a == b)  # Calls _eq_, prints values, returns None (False in boolean context)
print(a != b)  # Returns True (opposite of == result)
print(a . x !=  b . x)  # Compares attribute values directly (False since both 25)

# Find  outputs  (Home  work)
class   c1:
	def   _init_(self , y):  # Incorrect constructor name
		self . x = y  # Sets instance attribute
	def    _ne_(m , n):  # Incorrect not equal method name
		print('_ne_ method  :  ' , m . x , n . x)  # Prints compared values
		return  m . x != n . x  # Returns True if values are not equal
#end of the class
a = c1(10)  # Creates object a
b = a  # b references same object as a
print(a != b)  # Calls _ne_, prints values, returns False (same object)
print(a == b)  # Default equality check, returns True (same object)

#  Is  10 > 20  a  recursion ?
class  c1:
	def   _gt_(a , b):  # Incorrect greater than method name
		print(10 > 20)  # Prints result of 10 > 20 (False)
		print(a > b)  # This will cause recursion (calls _gt_ again)
a = c1()  # Creates object a
b = c1()  # Creates object b
print(a > b)  # Calls _gt_ method, causes recursion error

# Find  outputs  (Home  work)
class  c1:
	def _init_(self , y):  # Incorrect constructor name
		self . x = y  # Sets instance attribute
	def  _gt_(p , q):  # Incorrect greater than method name
		print('c1  class  _gt_  method : ' , p . x , q . x)  # Prints comparison
class  c2:
	def _init_(self , y):  # Incorrect constructor name
		self . x = y  # Sets instance attribute
	def _gt_(p , q):  # Incorrect greater than method name
		print('c2  class  _gt_  method : ' , p . x , q . x)  # Prints comparison
#end of the class
a = c1(10)  # Creates c1 object
b = c1(20)  # Creates c1 object
a > b  # Calls c1's _gt_ method
a < b  # Will error - no _lt_ method defined
m = c2(30)  # Creates c2 object
n = c2(40)  # Creates c2 object
a < m  # Will error - incompatible classes
n < b  # Will error - incompatible classes

# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):  # Incorrect add method name
		return '_add_ method  of  class   c1'  # Returns string
class c2:
	pass  # Empty class
#end of the class
a = c1()  # Creates c1 object
b = c1()  # Creates c1 object
print('a + b : ' , a + b)  # Will error - _add_ not properly defined
print('a + 7 : ' , a + 7)  # Will error
print(7 + a)  # Will error
print('7 + 8 : ' , 7 + 8)  # Normal addition (15)
m = c2()  # Creates c2 object
n = c2()  # Creates c2 object
print(m + n)  # Will error - no add method
print('a + m : ' , a + m)  # Will error
print(m + a)  # Will error

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):  # Incorrect constructor name
		self . x = y  # Sets instance attribute
	def _add_(p , q):  # Incorrect add method name
		return  sum  of  numbers  (or)  join  of  strings  # Incomplete implementation
#end of the class
a = c1(10)  # Creates object with number
b = c1(20)  # Creates object with number
m = c1('10')  # Creates object with string
n = c1('20')  # Creates object with string
print('Sum : ' , a + b)  # Will error due to incomplete implementation
print('Join : ' , m + n)  # Will error due to incomplete implementation

# Write  a  program  to  implement  queue  using  list
class  queue:
        def  _init_(q):  # Incorrect constructor name
                 How  to  create  an  empty  queue  # Incomplete - should be q.items = []
        def  isempty(q):  # Check if queue is empty
                return  True  when  queue  is  empty  and  False  otherwise  # Incomplete
        def  enqueue(q , x):  # Add element to queue
                How  to  insert  'x'  into  the  queue  # Incomplete - should use append()
        def  dequeue(q):  # Remove element from queue
                How  to  remove  first  element  of  the  queue  and  return  the  deleted  element  # Incomplete
				(return  -1  when  deletion  is  not  possible)  # Should use pop(0)
        def  first(q):  # Get first element
                How  to  return  the  first  element  of  the  queue  # Incomplete
				(return  -1  when  queue  is  empty)  # Should check isempty()
		def  last(q):  # Get last element
                How  to  return  the  first  element  of  the  queue  # Incomplete - should return last
				(return   -1  when  queue  is  empty)  # Should check isempty()
        def  disp(q):  # Display queue
                How  to  print  queue  # Incomplete
        def  size(q):  # Get queue size
                How  to  return  number   of  elements  in  the  queue  # Incomplete - len(q.items)
# End  of  the  class
def  menu():  # Display menu
        print('1. Insertion')  # Option 1
        print('2. Deletion')  # Option 2
        print('3. Print  queue')  # Option 3
        print('4. First  element of queue')  # Option 4
        print('5. Last  element of queue')  # Option 5
        print('6. Number  of  elements  in  the  queue')  # Option 6
        print('7. Exit')  # Option 7
# End of  the  function
How  to  create  queue  class  object  # Incomplete - q = queue()
menu()  # Display menu
ch = int(input('Enter  choice : ' ))  # Get user choice
while  repeat  until  user  input  is  7  # Incomplete while condition
	match  ch:  # Switch based on choice
		case  1:  # Insertion case
					x = eval(input('Enter  element  to  be  inserted : '))  # Get element to insert
					How  to  insert  'x'  into  the  queue  # Incomplete
					How  to  print  queue  # Incomplete
		case  2:  # Deletion case
					How  to  delete  queue  element  and  print  the  deleted  element  # Incomplete
					How  to  print  queue  # Incomplete
		case  3:  # Print case
					How  to  print  the  queue  # Incomplete
		case  4:  # First element case
					How  to  print  first  element  of  the  queue  # Incomplete
		case  5:  # Last element case
					How  to  print  last  element  of  the  queue  # Incomplete
		case  6:  # Size case
					How  to  print  number  of  elements  in  the  queue  # Incomplete
	# End  of  match
	menu()  # Show menu again
	ch = int(input('Enter  choice : ' ))  # Get next choice

# Write a program to implement stack using list
class Stack:
    def __init__(self):  # Constructor method to initialize stack object
        self.list = []   # Create an empty list to store stack elements
    
    def isempty(self):  # Method to check if stack is empty
        return self.list == []   # Return True when stack is empty and False otherwise
    
    def push(self, x):  # Method to add element to stack
        self.list.append(x)  # Insert 'x' into the stack at the top
    
    def pop(self):  # Method to remove and return top element
        try:  # Try to pop element
            return self.list.pop()  # Delete last element of the stack and return the deleted element
        except:  # Handle exception if stack is empty
            return None  # Return None when deletion is not possible
    
    def peek(self):  # Method to view top element without removing it
        try:  # Try to access top element
            return self.list[-1]  # Return the last element of the stack
        except:  # Handle exception if stack is empty
            return None  # Return None when stack is empty
    
    def disp(self):  # Method to display stack contents
        print('Stack : ', self.list)  # Print the entire stack
    
    def size(self):  # Method to get stack size
        return len(self.list) # Return number of elements in the stack
# End of the class

def menu():  # Function to display menu options
    print('1. Insertion')  # Option to push element
    print('2. Deletion')   # Option to pop element
    print('3. Print Stack')  # Option to display stack
    print('4. Last element of stack')  # Option to peek at top element
    print('5. Number of elements in the stack')  # Option to get size
    print('6. Exit')  # Option to exit program
# End of the function

if __name__ == '__main__':  # Main program execution block
    s = Stack()   # Create stack class object
    while True:  # Infinite loop until user exits
        menu()  # Display menu options
        ch = int(input('Enter choice : ' ))  # Get user choice
        match ch:  # Process user choice using match-case
            case 1:  # Insertion case
                x = eval(input('Enter element to be inserted : '))  # Get element from user
                s.push(x)   # Insert 'x' into the stack
                s.disp()   # Print current stack state
            
            case 2:  # Deletion case
                x = s.pop() # Delete stack element and get the deleted element
                if x == None:  # Check if stack was empty
                    print('Stack is empty, deletion is not permitted')  # Error message
                else:  # If deletion was successful
                    print('Deleted element : ', x)  # Print deleted element
                s.disp()  # Print current stack state
            
            case 3:  # Display case
                s.disp() # Print the entire stack
            
            case 4:  # Peek case
                x = s.peek()  # Get last element without removing it
                if x == None:  # Check if stack is empty
                    print('Stack is empty')  # Empty stack message
                else:  # If stack has elements
                    print('Last element : ', x)  # Print top element
            
            case 5:  # Size case
                print('Number of elements : ', s.size())   # Print number of elements in the stack
            
            case 6:  # Exit case
                exit()  # Terminate program
        # End of match
