# Write  a  program  to  implement  deque  using  list
class  deque:
    def   _init_(dq):
        list = []
    def  isempty(dq): 
        #return  True  when  deque  is  empty  and  False  otherwise
        return True if len(dq.list) == 0 else False
    def  ins_rear(dq , x):
        #How  to  insert  'x'  at  the  end  of  deque
        dq.list.append(x)
    def  ins_front(dq , x):
        #How  to  insert  'x'  at  the  begining  of  deque
        dq.list.insert(0,x)
    def  del_front(dq):
        # How  to  remove  left  most  element  of  the  deque  and  return  the  deleted  element
        # (return  None  when  deletion  is  not  possible)
        return None if dq.isempty() else deque.list[0]
    def  del_rear(dq):
        # How  to  remove  right  most  element  of  the  deque  and  return  the  deleted  element
        # (return  None  when  deletion  is  not  possible)
        return None if dq.isempty() else deque.list[-1]
    def  disp(dq):
        # How  to  print  deque
        dq.disp()
    def  size(dq):
        # return  number  of  elements  in  the  deque
        return len(dq.list)
    def left(dq):
        return dq.list[0]
    def right(dq):
        return dq.list[-1]
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
# How  to  create  deque  class  object
dq = deque()
while  True:
    menu()
    ch = int(input('Enter Choice :   '))
    match  ch:
        case  1:
            x = eval(input('Enter  element  to  be  inserted : '))
            # How  to  insert  'x'  at  the  end  of  deque
            # How  to  print  deque
            dq.ins_rear(x)
            dq.disp()
        case  2:
            x = eval(input('Enter  element  to  be  inserted : '))
            # How  to  insert  'x'  at  the  begining  of  deque
            # How  to  print  deque
            dq.ins_front(x)
            dq.disp()
        case  3:
            # How  to  delete  left  most  element  of  deque  and  print  the  deleted  element
            # How  to  print  queue
            print(dq.del_front())
            dq.disp()
        case  4:
            # How  to  delete  right  most  element  of  deque  and  print  the  deleted  element
            # How  to  print  queue
            print(dq.del_rear())
            dq.disp()
        case  5:
            # How  to  print  the  queue
            dq.disp()
        case  6:
            # How  to  print  left  most  element  of  deque
            print(dq.left())
        case  7:
            #How  to  print  right  most  element  of  deque
            print(dq.right())
        case  8:
            # How  to  print  number  of  elements  in  deque
            print(dq.size())
        case  9:
            # How  to  stop  execution
            exit()
        # End  of  match
