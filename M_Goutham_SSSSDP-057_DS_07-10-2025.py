class deque:
    def __init__(dq):
        dq.list = []  # Create an empty deque (list)

    def isempty(dq):
        return dq.list == []

    def ins_rear(dq, x):
        dq.list.append(x)  # Insert x at rear

    def ins_front(dq, x):
        dq.list.insert(0, x)  # Insert x at front (index 0)

    def del_front(dq):
        try:
            return dq.list.pop(0)  # Remove and return front element
        except IndexError:
            return None  # When deque is empty

    def del_rear(dq):
        try:
            return dq.list.pop()  # Remove and return rear element
        except:
            return None  # When deque is empty

    def disp(dq):
        print(dq.list)  # Display deque elements

    def size(dq):
        return len(dq.list)  # Return size of deque

# Menu function
def menu():
    print('1. Insert element at the end of deque')
    print('2. Insert element at the beginning of deque')
    print('3. Delete leftmost element')
    print('4. Delete rightmost element')
    print('5. Print Deque')
    print('6. Print leftmost element')
    print('7. Print rightmost element')
    print('8. Number of elements in deque')
    print('9. Exit')

dq = deque()

while True:
    menu()
    ch = int(input('Enter Choice: '))
    
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted: '))
            dq.ins_rear(x)
            dq.disp()

        case 2:
            x = eval(input('Enter element to be inserted: '))
            dq.ins_front(x)
            dq.disp()

        case 3:
            deleted = dq.del_front()
            if deleted is not None:
                print("Deleted element:", deleted)
            else:
                print("Deque is empty.")
            dq.disp()

        case 4:
            deleted = dq.del_rear()
            if deleted is not None:
                print("Deleted element:", deleted)
            else:
                print("Deque is empty.")
            dq.disp()

        case 5:
            print("Deque:")
            dq.disp()

        case 6:
            if dq.isempty():
                print("Deque is empty.")
            else:
                print("Leftmost element:", dq.list[0])

        case 7:
            if dq.isempty():
                print("Deque is empty.")
            else:
                print("Rightmost element:", dq.list[-1])

        case 8:
            print("Number of elements in deque:", dq.size())

        case 9:exit()
