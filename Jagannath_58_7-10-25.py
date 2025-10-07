# Write  a  program  to  implement  deque  using  list
class  deque:
    def   __init__(dq):
        dq.list=[]
    def  isempty(q):
        return dq.list==[]
    def  ins_rear(dq , x):
        dq.list.append(x)
    def  ins_front(dq , x):
        dq.list.insert(0,x)
    def  del_front(dq):
        try:
            return dq.list.pop(0)
        except:
            return None
    def  del_rear(dq):
        try:
            return dq.list.pop(-1)
        except:
            return None
    def  disp(dq):
        if dq.isempty():
            print("Deque is empty")
        else:
            print("Deque:",dq.list)
    def  size(dq):
        return len(dq.list)
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
dq=deque()
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
            val=dq.del_front()
            if val is not None:
                print('Deleted element:',val)
            else:
                print('Deletion is not possible:')
            dq.disp()
        case  4:
            val=dq.del_rear()
            if val is not None:
                print('Deleted element:',val)
            else:
                print('Deletion is not possible')
            dq.disp()
        case  5:
            dq.disp()
        case  6:
            if dq.isempty():
                print('Deque is empty')
            else:
                print('Left most element:',dq.list[0])
        case  7:
            if dq.isempty():
                print('Deque is empty')
            else:
                print('Right most element:',dq.list[-1])
        case  8:
            print('Number of elements in deque:',dq.size())
        case  9:
            break
