#postfix to prefix
from stack import stack

def postfix_to_prefix(a):
    s = stack()
    for i in a:
        if i.isdigit():
            s.push(i)
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.push(i + op2 + op1)
    return s.peek()

post = input('Enter postfix expression: ')
x = postfix_to_prefix(post)
print('Prefix expression:', x)

#prefix to posfix

from stack import stack

def prefix_to_posfix(a):
    s = stack()
    for i in a[::-1]:
        if i.isdigit():
            s.push(i)
        else:
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 + op2+i)
    return s.peek()

post = input('Enter prefix expression: ')
x = prefix_to_posfix(post)
print('Postfix expression:', x)


class  priority:
	def  __init__(s):  #  's'  is  stack  class  object
		s . list = []   #  Appends  variable  list  to  object  's'  which  is  an  empty  list
	def  isempty(s):  #  's'  is  stack  class  object
		return  s . list ==  []   #  True  when  list  is  empty  and  False  otherwise
	def  push(s , x):   #  's'  is  stack  class  object  and  'x'  is  element  to  be  inserted
		s . list . append(x)  #  Appends  'x'  to  the  list  held  by  stack  object  's'
		s.list.sort()
	def  pop(s):  #  's'  is  stack  class  object
		try:
			return  s . list . pop(0)  #   Removes  last  element  of  the  list  held  by  stack  object  's' and  returns  the  deleted  element
		except:
			return  None  #  Executed  when  s . list  is  empty
	def  peek(s):
		try:
			return  s . list[-1]  #   Last  element  of  the  list  held  by  stack  object  's'
		except:
			return  None  #  Executed  when  s . list  is  empty
	def  disp(s):
		print('Priority  Queue :  ' , s . list)  #  prints   the  list  held  by   stack  object  's'
	def   size(s):
		return  len(s . list) #   Number  of  elements  in  the  list  held  by   stack  object  's'
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Priority  Queue')
        print('4. Last  element of Priority  Queue')
        print('5. Number  of  elements  in  the  Priority  Queue')
        print('6. Exit')
# End of  the  function
if  __name__  ==  '__main__': 
	
	s = priority()  #   Constructor  initializes  object  with  list = []
while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						s . push(x)   #  Inserts  'x'  into  the  list  held  by  stack  object  's'
						s . disp()  #  Prints   the  list  held  by   stack  object  's'
						
			case  2:
						x = s . pop() #  Removes  the  last  element  of  the  list  held  by  stack  object  's'
						if  x  ==  None:
							print('Priority  Queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						s . disp()     #  Prints   the  list  held  by   stack  object  's'
			case  3:
						s . disp()      #  Prints   the  list  held  by   stack  object  's'
			case  4:
						x = s . peek()  #   Last  element  of   the  list  held  by  stack  object  's'
						if  x == None:
							print('Priority  Queue  is  empty')
						else:
							print('Last  element :  ' , x)
			case  5:
						print('Number  of  elements  :  ' ,  s . size())   #  Number  of  elements  in  the  list  held  by  stack  object  's'
			case  6:  exit()

