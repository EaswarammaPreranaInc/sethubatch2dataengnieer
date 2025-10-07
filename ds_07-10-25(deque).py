# Write  a  program  to  implement  deque  using  list
class deque:
    def __init__(self):
        self.list = []  # How to create an empty queue

    def isempty(self):
        return self.list == []

    def ins_rear(self, x):
        self.list.append(x)  # How to insert 'x' at the end of deque

    def ins_front(self, x):
        self.list.insert(0, x)  # How to insert 'x' at the beginning of deque

    def del_front(self):
        try:
            return self.list.pop(0)  # Remove leftmost element and return it
        except IndexError:
            return None  # Return None when deletion is not possible

    def del_rear(self):
        try:
            return self.list.pop()  # Remove rightmost element and return it
        except IndexError:
            return None  # Return None when deletion is not possible

    def disp(self):
        print(self.list)  # Print deque

    def size(self):
        return len(self.list)  # Return number of elements in the deque
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

dq = deque()  # Create deque class object
while True:
    menu()
    ch = int(input('Enter Choice :   '))
    match ch:
        case 1:
            x = eval(input('Enter  element  to  be  inserted : '))
            dq.ins_rear(x)
            dq.disp()
        case 2:
            x = eval(input('Enter  element  to  be  inserted : '))
            dq.ins_front(x)
            dq.disp()
        case 3:
            deleted = dq.del_front()
            print("Deleted:", deleted)
            dq.disp()
        case 4:
            deleted = dq.del_rear()
            print("Deleted:", deleted)
            dq.disp()
        case 5:
            dq.disp()
        case 6:
            if dq.size() > 0:
                print(dq.list[0])
            else:
                print("Deque is empty")
        case 7:
            if dq.size() > 0:
                print(dq.list[-1])
            else:
                print("Deque is empty")
        case 8:
            print(dq.size())
        case 9:
            exit()
    # End of match
		     
