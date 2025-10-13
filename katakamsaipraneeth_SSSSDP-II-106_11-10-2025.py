# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  __init__(pq):
		pq.list = [] #How  to  create  an  empty  list  in  object  pq
	def  isempty(pq):
		return  pq.list == [] # True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		pq.list.append(x) # How  to  insert  'x'  into  the  list  held  by  object  pq
		pq.list.sort() # How  to  sort  the  list  held  by  object  pq
	def  delete(pq):
		try:
			return pq.list.pop(0) # How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return None # (return  None  when  deletion  is  not  possible)
	def  highest_priority(pq):
		try:
			return pq.list[0] # How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return None # (return  None  when  the  list  is  empty)
	def  smallest_priority(pq):
		try:
			return pq.list[-1] # How  to  return  the  smallest  priority  element  from  the  list  held  by  object  pq
		except:
			return None # (return  None  when  the  list  is  empty)
	def  disp(pq):
		print('Priority_Que:', pq.list) # How  to  print  the  list  held  by  object  pq
	def   size(pq):
		return len(pq.list) # How  to  return  number   of  elements  in  the  list  held  by  object  pq
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
if  __name__  ==  '__main__':
	pq = priority_queue() # How  to  create  priority_queue  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						pq.insert(x) # How  to  insert  'x'  into  priority  queue
						pq.disp() # How  to  print  priority  queue
			case  2:
						x = pq.delete() # How  to  delete  highest  priority  element  from  priority  queue  and  print
						if  pq.isempty():
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						pq.disp() # How  to  print  priority  queue
			case  3:
						print('priority_queue:',pq.disp()) # How  to  print  priority  queue
			case  4:
						x = pq.highest_priority() # How  to  obtain  highest  priority  element
						if  pq.isempty():
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' ,  x)
			case  5:
						x = pq.smallest_priority() # How  to  obtain  smallest  priority  element
						if  pq.isempty():
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  x)
			case  6:
						print('Number  of  elements  :  ' ,  pq.size() )
			case  7:  exit()
		# End  of  match




#Object  'pq'   --->  list = []




# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method') # getter method
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method') # setter method
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ') # deleter method
		del  self .  _name
#end  of  the  class
p = Person() # setter method   getter method
print(p . name) # ''
p . name = 'Vamsi' 
print(p . name) # setter method    getter method  Vamsi
del   p . name # name is deleted 
#print(p . name) 
del   p # instance is deleted


'''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
	
'''
class Emp:
	def __init__(self):
		self.empno = eval(input('Enter employee number:'))
		self.empname = input('Enter employee name:')
		self.sal = eval(input('Enter employee salary:'))
		
	@property
	def empno(self):
		return self._empno
		
	@empno . setter
	def empno(self, value):
		if value < 0 :
			raise ValueError('Employee number should not be negative')
		self._empno = value
		
	@property
	def empname(self):
		return self._empname
		
	@empname . setter
	def empname(self, value):
		if value == '' :
			raise ValueError('Employee name should not empty')
		self._empname = value
	@property
	def sal(self):
		return self._sal
		
	@sal . setter
	def sal(self, value):
		if value < 0 :
			raise ValueError('Employee salary should not be negative')
		self._sal = value
		
try:
	e = Emp()
	print('employee number: ',e.empno)
	print('employee name :',e.empname)
	print('employee salary:',e.sal)
except ValueError as msg:
	print(msg)




#  Write  functions  to  create  and  print  linked  list
class  node:
		def   _init_(self , x):
				self . data = x
				self . link = None
		#   new  = node(25)
class  linked_list:
		def   _init_(a):
				a . first = None
		#  a = linked_list()
		def  isempty(a):
				return  a . first == None
		# a . isempty()  --->  True / False
		def  disp(a):
				if  a . isempty():
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p  !=  None:
								print(p . data , end = '\t')
								p = p . link
						print()
		def  append(a , new):
				if   a . isempty():
						a . first = new
				else:
						last = a . first
						while  last . link != None:
								last = last . link
						last . link = new
		def  create(a):
				try:
						a . first = None
						print('Enter  values  terminated  by  ctrl+z')
						while  True:
								x = eval(input())
								new = node(x)
								a . append(new)
				except:
						pass
# End  of  the  class
if  _name_ == '_main_':
	a = linked_list()
	a . create()
	print('Linked  List  :  ' , end = '')
	a . disp()