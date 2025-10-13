# Write  a  program  to  implement  queue  using  list
class  queue:
        def  __init__(q):
                q.items=[] #How  to  create  an  empty  queue
        def  isempty(q):
                return  len(q.items)==0
        def  enqueue(q , x):
                q.items.append(x)#How  to  insert  'x'  into  the  queue
        def  dequeue(q):
            if q.isempty():    #How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
                    return -1
            else:
                    return q.items.pop(0)
        def  first(q):
                if q.isempty():
                    return -1
                else:
                    return q.items[0]
        def  last(q):
                if q.isempty():
                        return -1
                else:
                        return q.items[-1]
        def  disp(q):
                print('Queue:',q.items)#How  to  print  queue
        def  size(q):
                return len(q.items)#How  to  return  number   of  elements  in  the  queue
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
q=queue()#How  to  create  queue  class  object
menu()
ch = int(input('Enter  choice : ' ))
while  ch!=7:
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					q.enqueue(x)#How  to  insert  'x'  into  the  queue
					q.disp()#How  to  print  queue
		case  2:
					deleted=q.dequeue()
                    q=disp()#How  to  print  queue
		case  3:
					q.disp()#How  to  print  the  queue
		case  4:
					print('First element :', q.first())#How  to  print  first  element  of  the  queue
		case  5:
					print('Last element :', q.last())#How  to  print  last  element  of  the  queue
		case  6:
					print('Number of elements :', q.size())#How  to  print  number  of  elements  in  the  queue
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))
     

'''
Write  a  program  to  reverse  a  string  using  stack

str  object  --->  R     A      M      A
                           0     1       2       3

Stack   --->

Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from prog1b import stack#How  to  import  stack  class  from  prog1b  module
s=stack()#How  to  create  stack  class  object
str_input=input('Enter a string:')#How  to  read  a  string  into  a  str  object
for ch in str_input:
    s.push(ch) #How  to  push  each  char  of  string  into  the  stack
print("Reverse  String :  ")
while not s.isempty():
    print(s.pop(), end='')#How  to  remove  each  char  of  stack  and  print  until   stack  is  empty
print()
     

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
from prog1b import stack
s = stack()
expr = input('Enter an expression : ')
valid = True
for ch in expr:
    if ch == '(':
        s.push(ch)
    elif ch == ')':
        popped = s.pop()
        if popped is None:
            print('Invalid expression: ")" before "("')
            valid = False
            break
if valid:
    if s.isempty():
        print('Expression is valid')
    else:
        print('Invalid expression: excess "("')

     
# Write  a  program  to  implement  stack  using  list
class  stack:
	def  __init__(s):
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




'