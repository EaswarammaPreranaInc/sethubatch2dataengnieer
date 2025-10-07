# Write  a  program  to  implement  deque  using  list
class Deque:
	def __init__(dq):
		dq.list = []
			#How  to  create  an  empty  queue
	def isempty(dq):
		return dq.list == []
            # return  True  when  deque  is  empty  and  False  otherwise
	def ins_rear(dq , x):
		dq.list.append(x)
			#How  to  insert  'x'  at  the  end  of  deque
	def ins_front(dq , x):
		dq.list.insert(0,x)
			#How  to  insert  'x'  at  the  begining  of  deque
	def del_front(dq):
		try:
			return dq.list.pop(0)
		except:
			return None
			#How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
			#(return  None  when  deletion  is  not  possible)
	def del_rear(dq):
		try:
			return dq.list.pop()
		except:
			return None
			#How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
			#(return  None  when  deletion  is  not  possible)
	def disp(dq):
		print("Dque :", dq.list)
			#How  to  print  deque
	def size(dq):
		return len(dq.list)
			#return  number  of  elements  in  the  deque
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
q = Deque() #How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
			x = eval(input('Enter  element  to  be  inserted : '))
			q.ins_rear(x) # How  to  insert  'x'  at  the  end  of  deque
			q.disp() # How  to  print  deque
		case  2:
			x = eval(input('Enter  element  to  be  inserted : '))
			q.ins_front(x) # How  to  insert  'x'  at  the  begining  of  deque
			q.disp() # How  to  print  deque
		case  3:
			x = q.del_front()
			print("Deleted (leftmost):", x)
			q.disp() # How  to  print  queue
		case  4:
			x = q.del_rear()
			print("Deleted (rightmost):", x)
			q.disp() # How  to  print  queue
		case  5:
			q.disp() # How  to  print  the  queue
		case 6:
			if not q.isempty():
				print("Leftmost element:", q.list[0])
			else:
				print("Deque is empty") # How  to  print  left  most  element  of  deque
		case  7:
			if not q.isempty():
				print("Rightmost element:", q.list[-1])
			else:
				print("Deque is empty") # How  to  print  right  most  element  of  deque
		case  8:
			print("Number of elements in deque:", q.size()) # How  to  print  number  of  elements  in  deque
		case  9:
			exit() # How  to  stop  execution
	# End  of  match