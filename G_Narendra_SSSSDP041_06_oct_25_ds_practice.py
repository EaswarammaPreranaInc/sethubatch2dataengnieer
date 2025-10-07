
# Stack  implementation  using  Python  list
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
if  __name__  ==  '__main__':
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


# Queue implementation using Python list
class queue:
    def __init__(q):
        # Create an empty queue
        q.list = []

    def isempty(q):
        # Return True when queue is empty, otherwise False
        return len(q.list) == 0

    def enqueue(q, x):
        # Insert 'x' into the queue (at the end)
        q.list.append(x)

    def dequeue(q):
        # Remove first element of the queue and return it
        # Return -1 when deletion is not possible (empty queue)
        if q.isempty():
            return -1
        else:
            return q.list.pop(0)

    def first(q):
        # Return first element of queue
        if q.isempty():
            return -1
        else:
            return q.list[0]

    def last(q):
        # Return last element of queue
        if q.isempty():
            return -1
        else:
            return q.list[-1]

    def disp(q):
        # Print the queue
        if q.isempty():
            print("Queue is empty.")
        else:
            print("Queue:", q.list)

    def size(q):
        # Return number of elements in the queue
        return len(q.list)

# End of class

def menu():
    print("\n--- Queue Operations Menu ---")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Print queue")
    print("4. First element of queue")
    print("5. Last element of queue")
    print("6. Number of elements in the queue")
    print("7. Exit")

# Create queue class object
q1 = queue()

# Menu-driven program
menu()
ch = int(input("Enter choice: "))

while ch != 7:
    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            q1.enqueue(x)
            q1.disp()

        case 2:
            deleted = q1.dequeue()
            if deleted == -1:
                print("Queue underflow! Deletion not possible.")
            else:
                print("Deleted element:", deleted)
            q1.disp()

        case 3:
            q1.disp()

        case 4:
            print("First element of queue:", q1.first())

        case 5:
            print("Last element of queue:", q1.last())

        case 6:
            print("Number of elements in the queue:", q1.size())

        case _:
            print("Invalid choice! Please try again.")

    menu()
    ch = int(input("Enter choice: "))

print("Program terminated.")



'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
#How  to  import  stack  class  from  prog1b  module
from stack_implementation import stack
#How  to  create  stack  class  object
s = stack()
#How  to  read  a  string  into  a  str  object
str = input("Enter  a  string  :  ")
#How  to  push  each  char  of  string  into  the  stack
for  ch  in  str:
    s.push(ch)
print("Reverse  String :  ")
#How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
while  not  s.isempty():
    print(s.pop(), end = '')
#End  of  while


'''
Write  a  program  to  perform  parentheses  match

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
from stack_implementation import stack
def paranthesis_match(str):
    s = stack() 
    for ch in str: 
        if ch == '(': 
            s.push(ch) 
        elif ch == ')': 
            if s.pop() == None:  
                print("Invalid: Excess ')' found")
                return
   
    if s.isempty():  
        print("Valid: All parentheses are matched")
    else:
        print("Invalid: Excess '(' found")


str = input("Enter a string with parentheses: ")
paranthesis_match(str)
