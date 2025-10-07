# In Deque  elements can be inserted and deleted from both ends

# List object is used to perform Deque operations

# Write  a  program  to  implement  deque  using  list
class  deque:
	def   __init__(self):
		self.items = []

	def isempty(self):
		return len(self.items) == 0
        
	def  ins_rear(self , x):
		self.items.append(x)

	def  ins_front(self , x):
		self.items.insert(0, x)

	def  del_front(self):
		if not self.isempty():
			return self.items.pop(0)
		return None

	def  del_rear(self):
		if not self.isempty():
			return self.items.pop()
		return None

	def disp(self):
		for item in self.items:
			print(item, end=' ')
		print()

	def size(self):
		return len(self.items)
#End of the class
def  menu():
      print('1. Insert  element  at  the  end  of  deque')
      print('2. Insert  element  at  the  begining  of  deque')
      print('3. Delete  left  most  element')
      print('4. Delete  right  most  element')
      print('5. Print  Deque')
      print('6. Print  left  most  element')
      print('7. Print  right  most  element')
      print('8. Number  of  elements  in  deque')
      print('9. Exit')
#end of  the  function
a = deque() # How  to  create  deque  class  object
while True:
	menu()
	ch = int(input('Enter Choice :   '))
	match ch:
		case 1:
			x = input('Enter  element  to  be  inserted : ')
			a.ins_rear(x)     # How  to  insert  'x'  at  the  end  of  deque
			a.disp() # How  to  print  deque
		case 2:
			x = input('Enter  element  to  be  inserted : ')
			a.ins_front(x) # How  to  insert  'x'  at  the  begining  of  deque
			a.disp() # How  to  print  deque
		case 3:
			x = a.del_front()  # How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
			a.disp() # How  to  print  queue
		case 4:
			x = a.del_rear() # How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
			a.disp() # How  to  print  queue
		case 5:
			a.disp() # How  to  print  the  queue
		case 6:
			x = a.items[0] if not a.isempty() else None # How  to  print  left  most  element  of  deque
			print(x)
		case 7:
			x = a.items[-1] if not a.isempty() else None # How  to  print  right  most  element  of  deque
			print(x)
		case 8:
			print(a.size()) # How  to  print  number  of  elements  in  deque
		case 9:
			print('Exiting...')
			exit() # How  to  stop  execution
	# End  of  match
