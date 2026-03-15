# Write  a  program  to  implement  deque  using  list
class  deque:
	def   __init__(dq):
			dq.list=[] # How  to  create  an  empty  queue
	def  isempty(q):
    if dq.list==[]:
      return  True 
    else:
      return False  #when  deque  is  empty  and  False  otherwise
	def  ins_rear(dq , x):
		        dq.list.append(x)	#How  to  insert  'x'  at  the  end  of  deque
	def  ins_front(dq , x):
					  dq.list.insert(0,x)	#How  to  insert  'x'  at  the  begining  of  deque
	def  del_front(dq):
    if dq.list==[]:
      print("Deletion not permitted")
else:
      dq.list.pop(0) #How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  elemen (return  None  when  deletion  is  not  possible)
	
  def  del_rear(dq):
			 if dq.list==[]:
         print("Deletion not permitted") #How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
      else:
        dq.list.pop() #(return  None  when  deletion  is  not  possible)
	def  disp(dq):
			print("Deque List :,dq.list")#How  to  print  deque
	def  size(dq):
			print("Length of Deque :",len(dq.list))return  number  of  elements  in  the  deque
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
dq=deque#How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_rear(x) #How  to  insert  'x'  at  the  end  of  deque
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
