# Write  a  program  to  implement  deque  using  list
class deque:
    def __init__(dq):
        dq.list = []  # How to create an empty queue
    def isempty(dq):
        return dq.list == []  # returns True when deque is empty and False otherwise
    def ins_rear(dq, x):
        dq.list.append(x)  # How to insert 'x' at the end of deque
    def ins_front(dq, x):
        dq.list.insert(0, x)  # How to insert 'x' at the beginning of deque
    def del_front(dq):
        try:
            return dq.list.pop(0)  # remove leftmost element and return it
        except:
            return None  # return None when deletion is not possible
    def del_rear(dq):
        try:
            return dq.list.pop()  # remove rightmost element and return it
        except:
            return None  # return None when deletion is not possible
    def disp(dq):
        print('Deque :', dq.list)  # How to print deque
    def size(dq):
        return len(dq.list)  # return number of elements in deque
# End of class
def menu():
    print('\n1. Insert element at the end of deque')
    print('2. Insert element at the beginning of deque')
    print('3. Delete leftmost element')
    print('4. Delete rightmost element')
    print('5. Print Deque')
    print('6. Print leftmost element')
    print('7. Print rightmost element')
    print('8. Number of elements in deque')
    print('9. Exit')
# End of function
dq = deque()  # create deque class object
while True:
    menu()
    ch = int(input('Enter Choice : '))
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            dq.ins_rear(x)  # insert at end
            dq.disp()  # print deque
        case 2:
            x = eval(input('Enter element to be inserted : '))
            dq.ins_front(x)  # insert at beginning
            dq.disp()
        case 3:
            x = dq.del_front()
            if x is None:
                print('Deque is empty. Deletion not possible.')
            else:
                print('Deleted element from front :', x)
            dq.disp()
        case 4:
            x = dq.del_rear()
            if x is None:
                print('Deque is empty. Deletion not possible.')
            else:
                print('Deleted element from rear :', x)
            dq.disp()
        case 5:
            dq.disp()  # print deque
        case 6:
            if dq.isempty():
                print('Deque is empty')
            else:
                print('Leftmost element :', dq.list[0])
        case 7:
            if dq.isempty():
                print('Deque is empty')
            else:
                print('Rightmost element :', dq.list[-1])
        case 8:
            print('Number of elements in deque :', dq.size())
        case 9:
            print('Program stopped.')
            break
    menu()
    ch = int(input('Enter Choice : '))
    
