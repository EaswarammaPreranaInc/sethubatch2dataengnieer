: # Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  _init_(pq):
		How  to  create  an  empty  list  in  object  pq
	def  isempty(pq):
		return  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		 How  to  insert  'x'  into  the  list  held  by  object  pq
		 How  to  sort  the  list  held  by  object  pq
	def  delete(pq):
		How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
		(return  None  when  deletion  is  not  possible)
	def  highest_priority(pq):
		How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		(return  None  when  the  list  is  empty)
	def  smallest_priority(pq):
		How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		(return  None  when  the  list  is  empty)
	def  disp(pq):
		How  to  print  the  list  held  by  object  pq
	def   size(pq):
		How  to  return  number   of  elements  in  the  list  held  by  object  pq
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
if  _name_  ==  '_main_':
	How  to  create  priority_queue  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						How  to  insert  'x'  into  priority  queue
						How  to  print  priority  queue
			case  2:
						How  to  delete  highest  priority  element  from  priority  queue  and  print
						if  ???:
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , ???)
						How  to  print  priority  queue
			case  3:
						How  to  print  priority  queue
			case  4:
						How  to  obtain  highest  priority  element
						if  ???
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' ,  ???)
			case  5:
						How  to  obtain  smallest  priority  element
						if  ???
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  ???)
			case  6:
						print('Number  of  elements  :  ' ,  ???)
			case  7:  exit()
		# End  of  match




#Object  'pq'   --->  list = []

#####################################################
# Program to implement Min Priority Queue using List
class priority_queue:
    def __init__(pq):
        pq.items = []   # create empty list in object pq

    def isempty(pq):
        return pq.items == []   # True if empty else False

    def insert(pq, x):
        pq.items.append(x)      # insert element
        pq.items.sort()         # sort ascending (min priority queue)

    def delete(pq):
        if pq.isempty():
            return None
        else:
            return pq.items.pop(0)   # delete smallest (highest priority)

    def highest_priority(pq):
        if pq.isempty():
            return None
        else:
            return pq.items[0]       # smallest element

    def smallest_priority(pq):
        if pq.isempty():
            return None
        else:
            return pq.items[-1]      # largest element

    def disp(pq):
        print(pq.items)

    def size(pq):
        return len(pq.items)

# ---------------------------------------------
def menu():
    print('\n1. Insertion')
    print('2. Deletion')
    print('3. Print priority queue')
    print('4. Highest priority element')
    print('5. Smallest priority element')
    print('6. Number of elements')
    print('7. Exit')
# ---------------------------------------------
if __name__ == '__main__':
    pq = priority_queue()     # create object

    while True:
        menu()
        ch = int(input('Enter choice : '))

        match ch:
            case 1:
                x = eval(input('Enter element to be inserted : '))
                pq.insert(x)
                print('Priority Queue : ', end='')
                pq.disp()

            case 2:
                d = pq.delete()
                if d is None:
                    print('Priority Queue is empty, deletion not permitted')
                else:
                    print('Deleted element :', d)
                print('Priority Queue : ', end='')
                pq.disp()

            case 3:
                print('Priority Queue : ', end='')
                pq.disp()

            case 4:
                h = pq.highest_priority()
                if h is None:
                    print('Priority Queue is empty')
                else:
                    print('Highest priority element :', h)

            case 5:
                s = pq.smallest_priority()
                if s is None:
                    print('Priority Queue is empty')
                else:
                    print('Smallest priority element :', s)

            case 6:
                print('Number of elements :', pq.size())

            case 7:
                exit()








: # Find  outputs (Home work)
class  Person:
	def  _init_(self):
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
#print(p . name)
del   p
###########################
Getter method

Setter method
Getter method
Vamsi
Deleter method




: '''
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
: Enter  employee  number :  -25
Empno cannot be negative
: Enter  employee  number :  25
Enter  employee  name :
Emp  name cannot be empty  string
: Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  -20
Salary cannot be negative
: Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  10000.0
Employee number  :  25
Employee name  :  Vamsi
Employee salary :   10000.0
###################################
class Emp:
    def __init__(self, empno, ename, sal):
        self.empno = empno
        self.ename = ename
        self.sal = sal

    @property
    def empno(self):
        return self._empno

    @empno.setter
    def empno(self, value):
        if value < 0:
            raise ValueError('Empno cannot be negative')
        self._empno = value

    @property
    def ename(self):
        return self._ename

    @ename.setter
    def ename(self, value):
        if value.strip() == '':
            raise ValueError('Emp name cannot be empty string')
        self._ename = value

    @property
    def sal(self):
        return self._sal

    @sal.setter
    def sal(self, value):
        if value < 0:
            raise ValueError('Salary cannot be negative')
        self._sal = value

# -----------------------------
try:
    eno = int(input('Enter employee number : '))
    ename = input('Enter employee name : ')
    sal = float(input('Enter salary : '))

    e = Emp(eno, ename, sal)

    print('Employee number :', e.empno)
    print('Employee name   :', e.ename)
    print('Employee salary :', e.sal)

except ValueError as v:
    print(v)








: #  Write  functions  to  create  and  print  linked  list
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


###############################
class node:
    def __init__(self, x):
        self.data = x
        self.link = None

class linked_list:
    def __init__(a):
        a.first = None

    def isempty(a):
        return a.first == None

    def disp(a):
        if a.isempty():
            print('Linked List is empty')
        else:
            p = a.first
            while p != None:
                print(p.data, end='\t')
                p = p.link
            print()

    def append(a, new):
        if a.isempty():
            a.first = new
        else:
            last = a.first
            while last.link != None:
                last = last.link
            last.link = new

    def create(a):
        try:
            a.first = None
            print('Enter values terminated by ctrl+z')
            while True:
                x = eval(input())
                new = node(x)
                a.append(new)
        except:
            pass

# ---- main ----
if __name__ == '__main__':
    a = linked_list()
    a.create()
    print('Linked List : ', end='')
    a.disp()
$$$$$$$$$$$$$$$$$$$$
Enter values terminated by ctrl+z
10
20
30
^Z
Linked List : 10    20    30

