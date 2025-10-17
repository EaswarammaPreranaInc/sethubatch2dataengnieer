# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  _init_(pq):
		pq.first=[]			# How  to  create  an  empty  list  in  object  pq
	def  isempty(pq):
		return pq.list==[]		# return  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		 pq.list.append(x)		# How  to  insert  'x'  into  the  list  held  by  object  pq
		 pq.list.sort()			# How  to  sort  the  list  held  by  object  pq
	def  delete(pq):
		if pq.isEmpty():		# How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
			return None		# (return  None  when  deletion  is  not  possible)
		return pq.list.pop(0)
	def  highest_priority(pq):
		if pq.isEmpty():		# How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
			return None				# (return  None  when  the  list  is  empty)
		return pq.list[0]
	def  smallest_priority(pq):
		if pq.isEmpty():				# How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
			return None				# (return  None  when  the  list  is  empty)
		return pq.list[-1]
	def  disp(pq):
		print('list of elements: ',pq.list)		# How  to  print  the  list  held  by  object  pq
	def   size(pq):
		return len(pq.list)				# How  to  return  number   of  elements  in  the  list  held  by  object  pq
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
	pq = priority_queue()				# How  to  create  priority_queue  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						pq.insert(x)			# How  to  insert  'x'  into  priority  queue
						pq.disp()			# How  to  print  priority  queue
			case  2:
						deleted = pq.delete(x)			# How  to  delete  highest  priority  element  from  priority  queue  and  print
						if  deleted is None:
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , deleted)
						pq.disp()				# How  to  print  priority  queue
			case  3:
						pq.disp()				# How  to  print  priority  queue
			case  4:
						hp=pq.higest_priority(x)		# How  to  obtain  highest  priority  element
						if  hp is None:
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' ,  hp)
			case  5:
						sm=pq.smallest_priority()		# How  to  obtain  smallest  priority  element
						if  sm is None:
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  sm)
			case  6:
						print('Number  of  elements  :  ' ,  pq.size())
			case  7:  exit()
		# End  of  match


#Object  'pq'   --->  list = []
 Here  is  the  blueprint  of  priority  queue
