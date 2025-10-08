# Write  a  program  to  implement  deque  using  list
class  deque:
	def   _init_(dq):
			#How  to  create  an  empty  queue
			dq.list = []
	def  isempty(q):
            return  dq.list  == [] # when  deque  is  empty  and  False  otherwise
	
	def ins_rear(dq , x):
			#How  to  insert  'x'  at  the  end  of  deque
			dq.list.append(x)
	def  ins_front(dq , x):
			#How  to  insert  'x'  at  the  begining  of  deque
			dq.list.insert(0,x)
	def  del_front(dq):
			#How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
			#(return  None  when  deletion  is  not  possible)
			try:
				return dq.list.pop(0)
			except:
				return None
	def  del_rear(dq):
			#How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
			#(return  None  when  deletion  is  not  possible)
			try:
				return dq.list.pop()
			except:
				return None			              
	def  disp(dq):
			#How  to  print  deque
			print(dq.list)
	def  size(dq):
			return  len(dq.list)#number  of  elements  in  the  deque
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
#How  to  create  deque  class  object
dq = deque()
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					#How  to  insert  'x'  at  the  end  of  deque
					dq.ins_rear(x)
					#How  to  print  deque
					dq.disp()
		case  2:
					x = eval(input('Enter  element  to  be  inserted : '))
					#How  to  insert  'x'  at  the  begining  of  deque
					dq.ins_front(0,x)
					#How  to  print  deque
					dq.disp()
		case  3:
					#How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
					dq.del_front()
					#How  to  print  queue
					dq.disp()
		case  4:
					#How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
					dq.del_rear()
					#How  to  print  queue
					dq.disp()
		case  5:
					#How  to  print  the  queue
					dq.disp()
		case  6:
					#How  to  print  left  most  element  of  deque
					print(dq.list[0])
		case  7:
					#How  to  print  right  most  element  of  deque
					print(dq.list[-1])
		case  8:
					#How  to  print  number  of  elements  in  deque
					print(dq.size())
		case  9:
					#How  to  stop  execution
					exit()
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))