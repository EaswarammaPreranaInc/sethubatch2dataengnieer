# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  __init__(pq):
		pq.list = [] #How  to  create  an  empty  list  in  object  pq
	def  isempty(pq):
		return  pq.list == [] #True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		pq.list.append(x) #How  to  insert  'x'  into  the  list  held  by  object  pq
		pq.list.sort() #How  to  sort  the  list  held  by  object  pq
	def  delete(pq):
		try:
			return pq.list.pop() #How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return  None  #when  deletion  is  not  possible
	def  highest_priority(pq):
		try:
			return pq.list[0] #How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return  None  #when  the  list  is  empty
	def  smallest_priority(pq):
		try:
			return pq.list[-1] #How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return  None  #when  the  list  is  empty
	def  disp(pq):
		print('Priority Queue : ',pq.list)#How  to  print  the  list  held  by  object  pq
	def   size(pq):
		return len(pq.list) #How  to  return  number   of  elements  in  the  list  held  by  object  pq
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
	pq = priority_queue() #How  to  create  priority_queue  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						pq.insert(x) #How  to  insert  'x'  into  priority  queue
						pq.disp() #How  to  print  priority  queue
			case  2:
						x=pq.delete() #How  to  delete  highest  priority  element  from  priority  queue  and  print
						if  x == None:
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , x)
						pq.disp() #How  to  print  priority  queue
			case  3:
						pq.disp() #How  to  print  priority  queue
			case  4:
						x=pq.highest_priority() #How  to  obtain  highest  priority  element
						if  x == None:
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' ,  x)
			case  5:
						x=pq.smallest_priority() #How  to  obtain  smallest  priority  element
						if  x == None:
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  x)
			case  6:
						print('Number  of  elements  :  ' ,  pq.size())
			case  7:  exit()
		# End  of  match
#Object  'pq'   --->  list = []

# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
#end  of  the  class
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
print(p . name) # Error
del   p
'''Output:
Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method
'''

# Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them
# Emp  number  and  salary  can  not  be  -ve
# Emp  name  can  not  be  empty  string
# class  name   is  Emp
# 3  getter  and  3  setter  methods
# Constructor  initializes  empno , ename  and  sal
# Outside  the  class
    # ----------------------
    # a) Create  Emp  class  object
    # b) Print  empno , ename  and  sal
# Program to validate emp number, emp name and salary using getter, setter and deleter methods
# Keeps asking until valid inputs are entered
class emp:
    def __init__(self):
        while True:
            try:
                self.empno = int(input('Enter employee no: '))
                break
            except ValueError:
                print('Invalid input. Enter a valid number.')
            except Exception as msg:
                print(msg)
        while True:
            try:
                self.ename = input('Enter employee name: ')
                break
            except Exception as msg:
                print(msg)
        while True:
            try:
                self.sal = float(input('Enter employee salary: '))
                break
            except ValueError:
                print('Invalid input. Enter a valid salary.')
            except Exception as msg:
                print(msg)
    @property
    def empno(self):
        return self._empno
    @property
    def ename(self):
        return self._ename
    @property
    def sal(self):
        return self._sal
    @empno.setter
    def empno(self, x):
        if x < 0:
            raise ValueError('Empno cannot be negative')
        self._empno = x
    @ename.setter
    def ename(self, x):
        if x.strip() == '':
            raise ValueError('Ename cannot be empty')
        self._ename = x
    @sal.setter
    def sal(self, x):
        if x < 0:
            raise ValueError('Salary cannot be negative')
        self._sal = x
e = emp()
print('Employee number :', e.empno)
print('Employee name   :', e.ename)
print('Salary          :', e.sal)

'''#output:
Enter employee no: -25
Invalid input. Enter a valid number.
Enter employee no: 20
Enter employee name: 
Ename cannot be empty
Enter employee name: Pari
Enter employee salary: -3
Invalid input. Enter a valid salary.
Enter employee salary: 60000
Employee number : 20
Employee name   : Pari
Salary          : 60000.0'''

#  Write  functions  to  create  and  print  linked  list
class  node:
	def __init__(self , x):
		self . data = x
		self . link = None
		#   new  = node(25)
class  linked_list:
	def __init__(a):
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
if  __name__ == '__main__':
	a = linked_list()
	a . create()
	print('Linked  List  :  ' , end = '')
	a . disp()
'''Output:
Enter  values  terminated  by  ctrl+z
25
35
45
55
65
^Z
Linked  List  :  25     35      45      55      65'''