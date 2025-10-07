# Write a program to implement deque using list

class deque:
    def __init__(dq):
        dq.list = []   # Create an empty deque

    def isempty(dq):
        return dq.list == []   # True if deque is empty

    def ins_rear(dq, x):
        dq.list.append(x)   # Insert 'x' at the rear (end)

    def ins_front(dq, x):
        dq.list.insert(0, x)   # Insert 'x' at the front (index 0)

    def del_front(dq):
        try:
            return dq.list.pop(0)   # Remove and return leftmost element
        except IndexError:
            return None             # Return None if deletion not possible

    def del_rear(dq):
        try:
            return dq.list.pop()    # Remove and return rightmost element
        except IndexError:
            return None             # Return None if deletion not possible

    def disp(dq):
        if dq.isempty():
            print("Deque is empty")
        else:
            print("Deque:", dq.list)

    def size(dq):
        return len(dq.list)   # Return number of elements in deque


# End of the class

def menu():
    print("\n1. Insert element at the end of deque")
    print("2. Insert element at the beginning of deque")
    print("3. Delete leftmost element")
    print("4. Delete rightmost element")
    print("5. Print Deque")
    print("6. Print leftmost element")
    print("7. Print rightmost element")
    print("8. Number of elements in deque")
    print("9. Exit")


# Main program
a = deque()   # Create deque class object

while True:
    menu()
    ch = int(input("Enter Choice: "))

    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            a.ins_rear(x)
            a.disp()

        case 2:
            x = eval(input("Enter element to be inserted: "))
            a.ins_front(x)
            a.disp()

        case 3:
            val = a.del_front()
            if val is None:
                print("Deque is empty, deletion not possible")
            else:
                print("Deleted element (front):", val)
            a.disp()

        case 4:
            val = a.del_rear()
            if val is None:
                print("Deque is empty, deletion not possible")
            else:
                print("Deleted element (rear):", val)
            a.disp()

        case 5:
            a.disp()

        case 6:
            if a.isempty():
                print("Deque is empty")
            else:
                print("Leftmost element:", a.list[0])

        case 7:
            if a.isempty():
                print("Deque is empty")
            else:
                print("Rightmost element:", a.list[-1])

        case 8:
            print("Number of elements in deque:", a.size())

        case 9:
            break
