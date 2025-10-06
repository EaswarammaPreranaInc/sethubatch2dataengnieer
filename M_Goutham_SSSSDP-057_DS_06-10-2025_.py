# Stack Program
class stack:
    def __init__(s):
        s.list = []

    def isempty(s):
        return s.list == []

    def push(s, x):
        s.list.append(x)

    def pop(s):
        try:
            return s.list.pop()
        except:
            return None

    def peek(s):
        try:
            return s.list[-1]
        except:
            return None

    def issize(s):
        return len(s.list)

    def disp(s):
        return s.list

# Stack object
s = stack()

# Menu function
def menu():
    print('\n1. Insertion')
    print('2. Deletion')
    print('3. Print stack')
    print('4. Last element of stack')
    print('5. Number of elements in the stack')
    print('6. Exit')

# Menu loop
while True:
    menu()
    ch = int(input("Enter the choice: "))
    match ch:
        case 1:
            x = eval(input("Enter the element you want to insert: "))
            s.push(x)
            print(f"Stack: {s.disp()}")

        case 2:
            deleted = s.pop()
            if deleted is None:
                print("Stack is empty. Deletion not possible.")
            else:
                print(f"Deleted element: {deleted}")
            print(f"Stack: {s.disp()}")

        case 3:
            print(f"Stack elements: {s.disp()}")

        case 4:
            top = s.peek()
            if top is None:
                print("Stack is empty.")
            else:
                print(f"Top-most element: {top}")

        case 5:
            print(f"Length of stack: {s.issize()}")

        case 6:exit()
        





# Write  a  program  to  implement  queue  using  list
class queue:
    def __init__(q):
        q.list = []  # How to create an empty queue

    def isempty(q):
        return q.list == []  # True when queue is empty and False otherwise

    def enqueue(q, x):
        q.list.append(x)  # How to insert 'x' into the queue

    def dequeue(q):
        try:
            return q.list.pop(0)  # Remove and return the first element
        except:
            return None  # Return None when deletion is not possible

    def first(q):
        try:
            return q.list[0]  # Return the first element
        except:
            return None  # Return None when queue is empty

    def last(q):
        try:
            return q.list[-1]  # Return the last element
        except:
            return None  # Return None when queue is empty

    def disp(q):
        return q.list  # Print queue

    def size(q):
        return len(q.list)  # Return number of elements in the queue

# End of the class

def menu():
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print queue')
    print('4. First element of queue')
    print('5. Last element of queue')
    print('6. Number of elements in the queue')
    print('7. Exit')
# End of the function

q = queue()  # Create queue class object
while True:
    menu()
    ch = int(input('Enter choice : '))
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            q.enqueue(x)  # Insert 'x' into the queue
            print("Queue:", q.disp())

        case 2:
            deleted = q.dequeue()
            if deleted is None:
                print("Queue is empty. Nothing to delete.")
            else:
                print("Deleted element:", deleted)
            print("Queue:", q.disp())

        case 3:
            print("Queue:", q.disp())

        case 4:
            first = q.first()
            if first is None:
                print("Queue is empty.")
            else:
                print("First element:", first)

        case 5:
            last = q.last()
            if last is None:
                print("Queue is empty.")
            else:
                print("Last element:", last)

        case 6:
            print("Number of elements in queue:", q.size())

        case 7:
            exit()

'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from mod1 import * #How  to  import  stack  class  from  prog1b  module
s = stack() #How  to  create  stack  class  object
n = input("Enter the string: " ) #How  to  read  a  string  into  a  str  object
for i in n:
    s.list.append(i)    #How  to  push  each  char  of  string  into  the  stack
print(f"String: {n}")
print("Reverse  String :  ")
for i in n:
    print(s.pop(),end='') #How  to  remove  each  char  of  stack  and  print  until   stack  is  empty



#Write  a  program  to  perform  parentheses  match
from mod1 import *
s = stack()
exp = input("Enter the expression: ")
for i in exp:
    if i == '(':
        s.push('(')
    elif i == ')':
        if s.pop() is None:
            print("Invalid")
            exit()
'''
1) Is  ((3 + 4)  valid ?  ---> No  due  to  excess  (

2) Is  (3 * (4 + 5))  valid ?  --->  Yes

3) Is  (3 * (4 + 5))) + 6 valid ? --->No  due  to  excess  ')'

4) Is  3 + 4  valid ? --->  Yes

5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (

6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack

7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack

8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  invalid  msg  and  stop  execution

9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->
																						Print  valid  msg  when  stack  is   empty  and  invalid  otherwise

10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''


# Write  a  program  to  implement  stack  using  list
class  stack:
	def  _init_(s):
		s . list = []   #  How  to  create  an  empty  stack
	def  isempty(s):
		return  s . list ==  []   #  return  True  when  stack  is  empty  and  False  otherwise
	def  push(s , x):
		s . list . append(x)  #  How  to  insert  'x'  into  the  stack
	def  pop(s):
		try:
			return  s . list . pop()  #  How  to  delete  last  element  of  the  stack  and  return  the  deleted  element
		except:
			return  None  #  return  None  when  deletion  is  not  possible
	def  peek(s):
		try:
			return  s . list[-1]  #   How  to  return  the  last  element  of  the  stack
		except:
			return  None
	def  disp(s):
		print('Stack :  ' , s . list)  #  How  to  print  stack
	def   size(s):
		return  len(s . list) #   How  to  return  number   of  elements  in  the  stack
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Stack')
        print('4. Last  element of stack')
        print('5. Number  of  elements  in  the  stack')
        print('6. Exit')
# End of  the  function
if  _name_  ==  '_main_':
	s = stack()   #  How  to  create  stack  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						s . push(x)   #  How  to  insert  'x'  into  the  stack
						s . disp()   #  How  to  print  stack
			case  2:
						x = s . pop() #  How  to  delete  stack  element  and  print  the  deleted  element
						if  x  ==  None:
							print('Stack  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						s . disp()  #   How  to  print  stack
			case  3:
						s . disp() #   How  to  print  the  stack
			case  4:
						x = s . peek()  #  How  to  print  last  element  of  the  stack
						if  x == None:
							print('Stack  is  empty')
						else:
							print('Last  element :  ' , x)
			case  5:
						print('Number  of  elements  :  ' ,  s . size())   #  How  to  print  number  of  elements  in  the  stack
			case  6:  exit()
		# End  of  match




#Object  's'   --->  list = [25 , 10.8 , 'Hyd']


'''
What  is  the  difference  between  's'  and  s . list ?  --->


's'  is  the  stack  object  and  s . list  is   the  list  held  by  stack  object
'''