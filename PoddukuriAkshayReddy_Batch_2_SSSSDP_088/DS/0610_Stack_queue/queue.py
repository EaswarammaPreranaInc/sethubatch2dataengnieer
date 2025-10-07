


# Write  a  program  to  implement  queue  using  list
class  queue:
        def  __init__(q):
            q.items = [] # How  to  create  an  empty  queue
        def  isempty(q):
            return len(q.items) == 0 # return  True  when  queue  is  empty  and  False  otherwise
        def  enqueue(q , x):
            q.items.append(x) # How  to  insert  'x'  into  the  queue
        def dequeue(q):
            if q.isempty():
                return -1
            else:
                return q.items.pop(0)  
					# How  to  remove  first  element  of  the  queue  and  return  the  deleted  element
			   # (return  -1  when  deletion  is  not  possible)
        def  first(q):
            if q.isempty():
                return -1
            else:
                return q.items[0]
        def  last(q):
            if q.isempty():
                return -1
            else:
                return q.items[-1]
        def  disp(q):
                print(q.items)
        def  size(q):
                return len(q.items)
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  queue')
        print('4. First  element of queue')
        print('5. Last  element of queue')
        print('6. Number  of  elements  in  the  queue')
        print('7. Exit')
# End of  the  function

if __name__ == '__main__':
    
	q = queue() # How  to  create  queue  class  object
	menu()
	ch = int(input('Enter  choice : ' ))
	while ch != 7:
		match  ch:
			case  1:
				x = input('Enter  element  to  be  inserted : ')
				q.enqueue(x)
				q.disp()
			case  2:
				deleted_element = q.dequeue()
				if deleted_element != -1:
					print('Deleted element : ' , deleted_element)
				else:print('Queue is empty')
				q.disp()
			case  3:
					q.disp()
			case  4:
					first_element = q.first()
					if first_element != -1:
						print('First element : ' , first_element)
					else:
						print('Queue is empty')
			case  5:
					last_element = q.last()
					if last_element != -1:
						print('Last element : ' , last_element)
					else:
						print('Queue is empty')
			case  6:
					print('Number of elements in the queue : ' , q.size())
		# End  of  match
		menu()
		ch = int(input('Enter  choice : ' ))
	print('Exiting...')

    
    
