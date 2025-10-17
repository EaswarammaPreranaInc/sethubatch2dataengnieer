
# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  __init__(pq):
		# How  to  create  an  empty  list  in  object  pq
		pq.list = []

	def  isempty(pq):
		# return  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
		return len(pq.list) == 0

	def  insert(pq , x):
		#  How  to  insert  'x'  into  the  list  held  by  object  pq
		pq.list.append(x)
		#  How  to  sort  the  list  held  by  object  pq
		pq.list.sort()

	def  delete(pq):
		#  How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
		#  (return  None  when  deletion  is  not  possible)
		if pq.isempty():
			return None
		else:
			return pq.list.pop(0)

	def  highest_priority(pq):
		#  How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		#  (return  None  when  the  list  is  empty)
		if pq.isempty():
			return None
		else:
			return pq.list[0]

	def  smallest_priority(pq):
		#  How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		#  (return  None  when  the  list  is  empty)
		if pq.isempty():
			return None
		else:
			return pq.list[-1]

	def  disp(pq):
		#  How  to  print  the  list  held  by  object  pq
		print('Priority Queue : ', pq.list)

	def   size(pq):
		#  How  to  return  number   of  elements  in  the  list  held  by  object  pq
		return len(pq.list)
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
	# How  to  create  priority_queue  class  object
	pq = priority_queue()
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
				x = eval(input('Enter  element  to  be  inserted : '))
				#  How  to  insert  'x'  into  priority  queue
				pq.insert(x)
				#  How  to  print  priority  queue
				pq.disp()

			case  2:
				#  How  to  delete  highest  priority  element  from  priority  queue  and  print
				deleted = pq.delete()
				if  deleted == None:
					print('Priority  queue  is  empty  , deletion  is  not  permitted')
				else:
					print('Deleted  element : '  , deleted)
				#  How  to  print  priority  queue
				pq.disp()

			case  3:
				#  How  to  print  priority  queue
				pq.disp()

			case  4:
				#  How  to  obtain  highest  priority  element
				h = pq.highest_priority()
				if  h == None:
					print('Priority  queue  is  empty')
				else:
					print('Highest  priority  element :  ' ,  h)

			case  5:
				#  How  to  obtain  smallest  priority  element
				s = pq.smallest_priority()
				if  s == None:
					print('priority  queue  is  empty')
				else:
					print('Smallest  priority  element :  ' ,  s)

			case  6:
				print('Number  of  elements  :  ' ,  pq.size())

			case  7:
				exit()
		# End  of  match



#Object  'pq'   --->  list = []
