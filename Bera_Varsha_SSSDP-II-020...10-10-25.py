#  Write  a  program  to  convert  postfix  to  prefix
from  infix_postfix  import  *  #   In  view  of   convert()  function  and  stack  class
def   postfix_prefix(postfix):
	s = stack()  #   Constructor  initilaizes  s . list =[]
	for  ch  in  postfix:  #  ch  is  each  char  of  postfix  expression
		if  ch . isalnum():  #  Is  ch  is  an  operand
			s . push(ch)  #  Push  the  operand  into  the  stack
		else:  #  ch  is  an  operator
			op2 = s . pop()  #   1st  deleted  element  is  the  2nd  operand
			op1 = s . pop()   #  2nd  deleted  element  is  the  1st  operand
			new_expr = ch + op1 + op2  #   Concatenates  ch , op2   and  op1  to  form a  string
			s . push(new_expr)  # Pushes  the  concatenated  string  into  the  stack
	# End  of  for  loop
	return  s . pop()   #  Prefix  expression
#  End  of  the  function
infix = input('Enter  Infix  expression : ')  #   Reads  infix  expression
postfix = convert(infix)  #  Converts  infix  to  postfix
print('Prefix  expression : ' , postfix_prefix(postfix)) #   Converts  postfix  to  prefix

#  Write  a  program  to  convert  prefix  to  postfix
from  infix_prefix  import  *  #   In  view  of   convert()  function  and  stack  class
def   prefix_postfix(prefix):
	s = stack()  #   Constructor  initilaizes  s . list =[]
	prefix = prefix[::-1]  #  Reverses  prefix  expression
	for  ch  in  prefix:  #  ch  is  each  char  of   reverse  prefix  expression
		if  ch . isalnum():  #  Is  ch  is  an  operand
			s . push(ch)  #  Push  the  operand  into  the  stack
		else:  #  ch  is  an  operator
			op1 = s . pop()  #   1st  deleted  element  is  the  1st  operand
			op2 = s . pop()   #  2nd  deleted  element  is  the  2nd  operand
			new_expr = op1 + op2 + ch  #   Concatenates  op1 , op2  and  ch   to  form a  string
			s . push(new_expr)  # Pushes  the  concatenated  string  into  the  stack
	# End  of  for  loop
	return  s . pop()   #  Postfix  expression
#  End  of  the  function
infix = input('Enter  Infix  expression : ')  #   Reads  infix  expression
prefix = convert(infix)  #  Converts  infix  to  prefix
print('Prefix  expression : ' , prefix_postfix(prefix)) #   Converts  prefix  to  postfix

# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  _init_(pq):
		pq . list = []  #  Adds  variable  list  to  object  pq  which  is  an  empty  list
	def  isempty(pq):
		return  pq . list ==  []   #  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		pq . list . append(x)  #  Appends  'x'  to  the  list  held  by  object  pq
		pq . list . sort()   #  Sort  the  list  to  make  deletion  simple
	def  delete(pq):
		try:
			return  pq . list . pop(0)  #  Removes  highest  priority  element  of  the  list  held  by  object  pq  and  returns  the  deleted  element
		except:  #  Executed  when  the  list  held  by  object  pq  is  empty
			return  None
	def  highest_priority(pq):
		try:
			return   pq . list[0]  #   Returns  the  smallest  element  (i.e. highest  priority  element)  of  the  list  held  by  object  pq
		except:  #  Executed  when  the  list  held  by  object  pq  is  empty
			return  None
	def  smallest_priority(pq):
		try:
			return   pq . list[-1]  #  Returns  the  largest  element  (i.e. smallest  priority  element)  of  the  list  held  by  object  pq
		except:   #  Executed  when  the  list  held  by  object  pq  is  empty
			return  None
	def  disp(pq):
		print('Priority  Queue :  ' , pq . list)  #  Prints  the  list  held  by  object  pq
	def   size(pq):
		return  len(pq . list)  #   Number  of  elements  in  the  list  held  by  object  pq
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  priority  queue')
        print('4. Highest  priority  element of  priority  queue')
        print('5. Smallest  priority  element of  priority  queue')
        print('6. Number  of  elements  in  the  priority  queue')
        print('7. Exit')
# End of  the  function
if  __name__ ==  '__main__':
	pq = priority_queue()  #  Constructor  initializes   object  with  list  = []
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						pq . insert(x)  #   Inserts  'x'  into  priority  queue
						pq . disp()   #  Prints  priority  queue
			case  2:
						x = pq . delete()  #  Deletes  highest  priority  element  of  priority  queue
						if  x == None:
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						pq . disp()   #  Prints  priority  queue
			case  3:
						pq . disp()  #   Prints  priority  queue
			case  4:
						x = pq . highest_priority()  #  Returns  highest  priority  element  of  priority  queue
						if  x == None:
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' ,  x)
			case  5:
						x = pq . smallest_priority()  #  Returns  smallest  priority  element  of  priority  queue
						if  x == None:
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  x)
			case  6:
						print('Number  of  elements  :  ' ,  pq . size())
			case  7:
						exit()
		# End  of  match
# Object  'pq'   --->  list = []


'''
What  is  the  difference  between  pq   and  pq . list ?  --->
															pq  is  priority_queue  object  and  pq . list  is   the  list  held  by  object  pq
'''