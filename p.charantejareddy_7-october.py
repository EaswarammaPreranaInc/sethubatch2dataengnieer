class deque:
    def __init__(self):
        self.dq = []

    def isempty(self):
        return len(self.dq) == 0

    def ins_rear(self, x):
        self.dq.append(x)

    def ins_front(self, x):
        self.dq.insert(0, x)

    def del_front(self):
        if self.isempty():
            return None
        return self.dq.pop(0)

    def del_rear(self):
        if self.isempty():
            return None
        return self.dq.pop()

    def disp(self):
        print("Deque:", self.dq)

    def size(self):
        return len(self.dq)

    def leftmost(self):
        if self.isempty():
            return None
        return self.dq[0]

    def rightmost(self):
        if self.isempty():
            return None
        return self.dq[-1]

def menu():
    print('1. Insert element at the end of deque')
    print('2. Insert element at the beginning of deque')
    print('3. Delete left most element')
    print('4. Delete right most element')
    print('5. Print Deque')
    print('6. Print left most element')
    print('7. Print right most element')
    print('8. Number of elements in deque')
    print('9. Exit')

# Create deque class object
d = deque()

while True:
    menu()
    ch = int(input('Enter Choice : '))
    match ch:
        case 1:
            x = eval(input('Enter element to be inserted : '))
            d.ins_rear(x)
            d.disp()
        case 2:
            x = eval(input('Enter element to be inserted : '))
            d.ins_front(x)
            d.disp()
        case 3:
            deleted = d.del_front()
            print("Deleted element:", deleted)
            d.disp()
        case 4:
            deleted = d.del_rear()
            print("Deleted element:", deleted)
            d.disp()
        case 5:
            d.disp()
        case 6:
            print("Left most element:", d.leftmost())
        case 7:
            print("Right most element:", d.rightmost())
        case 8:
            print("Number of elements in deque:", d.size())
        case 9:
            print("Exiting...")
            break
