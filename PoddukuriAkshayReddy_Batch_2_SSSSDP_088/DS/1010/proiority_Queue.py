# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  _init_(pq):
		pq.list = [] # How  to  create  an  empty  list  in  object  pq
	def  isempty(pq):
      return pq.list == [] # return  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		pq.list.append(x) # How  to  insert  'x'  into  the  list  held  by  object  pq
		pq.list.sort() # How  to  sort  the  list  held  by  object  pq
	def  delete(pq):
		try:
			return pq.list.pop(0) # How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
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



















# class priority_Queue:
#     def __init__(self):
#         # self.queue = []
#         self.list = []

#     def is_empty(self):
#         return len(self.queue) == 0

#     def insert(self, data, priority):
#         self.queue.append((data, priority))

#     def delete(self):
#         if self.is_empty():
#             return None
#         max_priority_index = 0
#         for i in range(1, len(self.queue)):
#             if self.queue[i][1] > self.queue[max_priority_index][1]:
#                 max_priority_index = i
#         return self.queue.pop(max_priority_index)

#     def peek(self):
#         if self.is_empty():
#             return None
#         max_priority_index = 0
#         for i in range(1, len(self.queue)):
#             if self.queue[i][1] > self.queue[max_priority_index][1]:
#                 max_priority_index = i
#         return self.queue[max_priority_index]

#     def display(self):
#         if self.is_empty():
#             print("Priority Queue is empty")
#         else:
#             for item in self.queue:
#                 print(f"Data: {item[0]}, Priority: {item[1]}")


# def menu():
#     print("1. Insert")
#     print("2. Delete")
#     print("3. Peek")
#     print("4. Display")
#     print("5. Exit")
#     print('6. Priority Queue ')



