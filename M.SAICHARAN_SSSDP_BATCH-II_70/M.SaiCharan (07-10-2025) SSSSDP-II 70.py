                                  NAME:M.SAICHARAN                   HOMEWORK
                                  DATE:07-10-2025

1.# Write  a  program  to  implement  deque  using  list
class  deque:
	def   __init__(dq):
			How  to  create  an  empty  queue
	def  isempty(q):
            return  True  when  deque  is  empty  and  False  otherwise
	def  ins_rear(dq , x):
			How  to  insert  'x'  at  the  end  of  deque
	def  ins_front(dq , x):
			How  to  insert  'x'  at  the  begining  of  deque
	def  del_front(dq):
			How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
			(return  None  when  deletion  is  not  possible)
	def  del_rear(dq):
			How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
			(return  None  when  deletion  is  not  possible)
	def  disp(dq):
			How  to  print  deque
	def  size(dq):
			return  number  of  elements  in  the  deque
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
How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					How  to  insert  'x'  at  the  end  of  deque
					How  to  print  deque
		case  2:
					x = eval(input('Enter  element  to  be  inserted : '))
					How  to  insert  'x'  at  the  begining  of  deque
					How  to  print  deque
		case  3:
					How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
					How  to  print  queue
		case  4:
					How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
					How  to  print  queue
		case  5:
					How  to  print  the  queue
		case  6:
					How  to  print  left  most  element  of  deque
		case  7:
					How  to  print  right  most  element  of  deque
		case  8:
					How  to  print  number  of  elements  in  deque
		case  9:
					How  to  stop  execution
	# End  of  match
	menu()
	ch = int(input('Enter  choice : ' ))

#Program:
class  deque:
        def __init__(dq):
              dq.list = []
        def  isempty(q):
               return q.list == []
        def  ins_rear(dq , x):
               dq.list.append(x)
        def  ins_front(dq , x):
               dq.list.insert(0,x)
        def  del_front(dq):
              try:
                return  dq.list.pop(0)
              except:
                    return  None
        def  del_rear(dq):
              try:
                return  dq.list.pop()
              except:
                    return  None
        def  disp(dq):
              print('Deque :  ' , dq.list)
        def  size(dq):
              return  len(dq.list)
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
dq = deque()
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
            case  1:
                x = eval(input('Enter  element  to  be  inserted : '))
                dq.ins_rear(x)
                dq.disp()
            case  2:
                x = eval(input('Enter  element  to  be  inserted : '))
                dq.ins_front(x)
                dq.disp()
            case  3:
                x = dq.del_front()
                if  x  ==  None:
                    print('Deque  is  empty  , deletion  is  not  permitted')
                else:
                    print('Deleted  element : '  , x)
            case  4:
                x = dq.del_rear()
                if  x  ==  None:
                    print('Deque  is  empty  , deletion  is  not  permitted')
                else:
                    print('Deleted  element : '  , x)
            case  5:
               dq.disp()
            case  6:
                x = dq.list[0]
                if  x == None:
                    print('Deque  is  empty')
                else:
                    print('Last  element :  ' , x)
            case  7:
                x = dq.list[-1]
                if  x == None:
                    print('Deque  is  empty')
                else:
                    print('Last  element :  ' , x)
            case  8:
                print('Number  of  elements  :  ' ,dq.size())
            case  9:
                exit()
menu()
ch = int(input('Enter  choice : ' ))