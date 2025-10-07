# Write  a  program  to  implement  deque  using  list
class  deque:
	def   __init__(dq):
		self.dq=[]          #How  to  create  an  empty  queue
	def  isempty(q):
		return len(self.dq) == 0  #True  when  deque  is  empty  and  False  otherwise
	def  ins_rear(dq , x):
			self.dq.append(x)       #How  to  insert  'x'  at  the  end  of  deque
	def  ins_front(dq , x):
			self.dq.insert(0,x)     #How  to  insert  'x'  at  the  begining  of  deque
	def  del_front(dq):
			if self.isempty():#How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
			    return  None  #when  deletion  is  not  possible
			return self.dq.pop()
	def  del_rear(dq):
			if self.isempty():   #How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
				return  None  #when  deletion  is  not  possible
			return self.dq.pop()
    
	def  disp(dq):
			print('Deque:',self.dq) #How  to  print  deque
	def  size(dq):
			return len(self.dq) # number  of  elements  in  the  deque
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
dq=deque()      #How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_rear(x)      #How  to  insert  'x'  at  the  end  of  deque
					dq.disp()           #How  to  print  deque
		case  2:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_front(x)     #How  to  insert  'x'  at  the  begining  of  deque
					dq.disp()           #How  to  print  deque
		case  3:
					deleted = dq.del.front()        #How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
					print('Deleted element:',deleted)
					dq.disp()                       #How  to  print  queue
		case  4:
					deleted = dq.del.rear()        #How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
					print('Deleted element:',deleted)
					dq.disp()                       #How  to  print  queue
		case  5:
					dq.disp()               #How  to  print  the  queue
		case  6:
					print('left most element:',dq.front())          #How  to  print  left  most  element  of  deque
		case  7:
					print('left most element:',dq.rear())           #How  to  print  right  most  element  of  deque
		case  8:
					print('Number of elements in deque:',dq.size())     #How  to  print  number  of  elements  in  deque
		case  9:
					print('Exit')               #How  to  stop  execution
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))