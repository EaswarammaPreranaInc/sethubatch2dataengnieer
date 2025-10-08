#Nanda Kishore Vemula
class  deque:
	def   __init__(dq):
		dq.list=[]#How  to  create  an  empty  queue
	def  isempty(q):
		return  q.list==[] #True  when  deque  is  empty  and  False  otherwise
	def  ins_rear(dq , x):
		dq.list.append(x) #How  to  insert  'x'  at  the  end  of  deque
	def  ins_front(dq , x):
		dq.list.insert(0,x) #How  to  insert  'x'  at  the  begining  of  deque
	def  del_front(dq):
		try:
			return dq.list.pop(0)
		except:
			return None #How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
			             #(return  None  when  deletion  is  not  possible)
	def  del_rear(dq):
		try:
			return dq.list.pop()#How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
		except:
			return None         #(return  None  when  deletion  is  not  possible)
	def  disp(dq):
		print('Deque : ',dq.list)#How  to  print  deque
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

dq=deque()#How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
			x = eval(input('Enter  element  to  be  inserted : '))
			dq.ins_rear(x)#How  to  insert  'x'  at  the  end  of  deque
			dq.disp()#How  to  print  deque
		case  2:
			x = eval(input('Enter  element  to  be  inserted : '))
			dq.ins_front(x)#How  to  insert  'x'  at  the  begining  of  deque
			dq.disp()#How  to  print  deque
		case  3:
			print('Left Most Element : ',dq.del_front())#How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
			dq.disp()#How  to  print  queue
		case  4:
			print('Right Most Element : ',dq.del_rear())#How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
			dq.disp()#How  to  print  queue
		case  5:
			dq.disp()#How  to  print  the  queue
		case  6:
			print('Left Most Element :',dq.list[0])#How  to  print  left  most  element  of  deque
		case  7:
			print('Right Most Element : ',dq.list[-1])#How  to  print  right  most  element  of  deque
		case  8:
			print('Number of Elements : ',dq.size())#How  to  print  number  of  elements  in  deque
		case  9:
			exit()#How  to  stop  execution
	# End  of  match
