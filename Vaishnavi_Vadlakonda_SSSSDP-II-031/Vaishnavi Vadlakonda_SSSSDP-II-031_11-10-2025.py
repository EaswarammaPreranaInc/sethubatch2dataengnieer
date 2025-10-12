# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def __init__(pq):
		pq.list = [] #How  to  create  an  empty  list  in  object  pq
	def isempty(pq):
		return pq.list == [] #return  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def insert(pq , x):
		pq.list.append(x) # How  to  insert  'x'  into  the  list  held  by  object  pq
		pq.list.sort() #How  to  sort  the  list  held  by  object  pq
	def delete(pq):
		try:
			return pq.list.pop(0) # How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return None	# (return  None  when  deletion  is  not  possible)
	def highest_priority(pq):
		try:
			return pq.list[0] # How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return None # (return  None  when  the  list  is  empty)
	def smallest_priority(pq):
		try:
			return pq.list[-1] #How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		except:
			return None #(return  None  when  the  list  is  empty)
	def disp(pq):
		print(pq.list) # How  to  print  the  list  held  by  object  pq
	def size(pq):
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
if  _name_  ==  '_main_':
	pq = priority_queue() # How  to  create  priority_queue  class  object
	while True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match ch:
			case 1:
				x = eval(input('Enter  element  to  be  inserted : '))
				pq.insert(x) # How  to  insert  'x'  into  priority  queue
				pq.disp() # How  to  print  priority  queue
			case 2:
				x = pq.delete() # How  to  delete  highest  priority  element  from  priority  queue  and  print
				if  x == None:
					print('Priority  queue  is  empty  , deletion  is  not  permitted')
				else:
					print('Deleted  element : '  , x)
				p.disp() # How  to  print  priority  queue
			case 3:
				pq.disp() #How  to  print  priority  queue
			case 4:
				x = pq.highest_priority() #How  to  obtain  highest  priority  element
				if x == None:
					print('Priority  queue  is  empty')
				else:
					print('Highest  priority  element :  ' ,  x)
			case 5:
				x = pq.lowest_priority() #How  to  obtain  smallest  priority  element
				if x == None:
					print('priority  queue  is  empty')
				else:
					print('Smallest  priority  element :  ' ,  x)
			case 6:
				print('Number  of  elements  :  ' ,  pq.size())
			case 7:  
				exit()
		# End  of  match









# Find  outputs (Home work)
class Person:
	def __init__(self):
		self . name  =  ''
	@property
	def name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def name(self , value):
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
print(p . name) # Error in return statement in getter method because _name is already deleted
del p 
'''
Outputs
Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method
'''









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
    b) Print  empno , ename  and  sal
Enter  employee  number :  -25
Empno cannot be negative
Enter  employee  number :  25
Enter  employee  name :
Emp  name cannot be empty  string
Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  -20
Salary cannot be negative
Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  10000.0
Employee number  :  25
Employee name  :  Vamsi
Employee salary :   10000.0
'''
class Person:
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
            raise ValueError
        self._empno = value
    @empno.deleter
    def empno(self):
        del self._empno
    @property
    def ename(self):
        return self._ename
    @ename.setter
    def ename(self, value):
        if value.strip() == '':
            raise ValueError
        self._ename = value  
    @ename.deleter
    def ename(self):
        del self._ename
    @property
    def sal(self):
        return self._sal
    @sal.setter
    def sal(self, value):
        if value < 0:
            raise ValueError
        self._sal = value
    @sal.deleter   
    def sal(self):
        del self._sal
while True:
    empno = int(input("Enter  employee  number :  "))
    if empno < 0:
        print("Empno cannot be negative")
        break 
    ename = input("Enter  employee  name : ")
    if ename.strip() == '':
        print("Emp name cannot be empty string")
        break
    sal = float(input("Enter  salary :  "))
    if sal < 0:
        print("Salary cannot be negative")
        break