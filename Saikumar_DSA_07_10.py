# Write  a  program  to  implement  deque  using  list
class  deque:
	def   __init__(dq):
		dq.list=[]                          # How  to  create  an  empty  queue
	def  isempty(dq):
		return dq.list == []                # return  True  when  deque  is  empty  and  False  otherwise
	def  ins_rear(dq , x):
		return dq.list.append(x)            # How  to  insert  'x'  at  the  end  of  deque
	def  ins_front(dq , x):
		return dq.list.insert(0,x)          # How  to  insert  'x'  at  the  begining  of  deque
	def  del_front(dq):
		try:
			return dq.list.pop(0)           # How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
		except:
			return None                     # How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
			                                # (return  None  when  deletion  is  not  possible)
	def  del_rear(dq):
		try:
			return dq.list.pop()            # How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
		except:
			return None                     # (return  None  when  deletion  is  not  possible)
	def  disp(dq):
		return dq.list                      # How  to  print  deque
	def  size(dq):
		return len(dq.list)                 # return  number  of  elements  in  the  deque
	def  first(dq):
		try:
			return dq.list[0]                # How  to  print  left  most  element
		except:
			return None
	def  last(dq):
		try:
			return dq.list[-1]               # How  to  print  right  most  element
		except:
			return None
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

d = deque()                                      # How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					d.ins_rear(x)                # How  to  insert  'x'  at  the  end  of  deque
					print("Deque : ", d.disp())   # How  to  print  deque
		case  2:
					x = eval(input('Enter  element  to  be  inserted : '))
					d.ins_front(x)               # How  to  insert  'x'  at  the  begining  of  deque
					print("Deque : ", d.disp())   # How  to  print  deque
		case  3:
					h = d.del_front()             # How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
					if h == None:
						print("Deque is empty, deletion not possible")
					else:
						print("Deleted element : ", h)
					print("Deque : ", d.disp())    # How  to  print  queue
		case  4:
					h = d.del_rear()              # How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
					if h == None:
						print("Deque is empty, deletion not possible")
					else:
						print("Deleted element : ", h)
					print("Deque : ", d.disp())    # How  to  print  queue
		case  5:
					print("Deque : ", d.disp())    # How  to  print  the  queue
		case  6:
					h = d.first()                  # How  to  print  left  most  element  of  deque
					if h == None:
						print("Deque is empty")
					else:
						print("Leftmost element : ", h)
		case  7:
					h = d.last()                   # How  to  print  right  most  element  of  deque
					if h == None:
						print("Deque is empty")
					else:
						print("Rightmost element : ", h)
		case  8:
					print("Number of elements in deque : ", d.size())  # How  to  print  number  of  elements  in  deque
		case  9:
					break                          # How  to  stop  execution
	menu()
	ch = int(input('Enter  choice : ' ))
