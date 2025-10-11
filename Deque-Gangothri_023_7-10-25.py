# Write a program to implement deque using list
class deque:
    def __init__(dq):
        dq.list = []  # create an empty deque

    def isempty(dq):
        return dq.list == []  # return True when deque is empty, False otherwise

    def ins_rear(dq, x):
        dq.list.append(x)  # insert 'x' at the end of deque

    def ins_front(dq, x):
        dq.list.insert(0, x)  # insert 'x' at the beginning of deque

    def del_front(dq):
        try:
            return dq.list.pop(0)  # remove leftmost element and return it
        except IndexError:
            return None

    def del_rear(dq):
        try:
            return dq.list.pop()  # remove rightmost element and return it
        except IndexError:
            return None

    def disp(dq):
        print("Deque:", dq.list)  # print deque

    def size(dq):
        return len(dq.list)  # return number of elements

    def leftmost(dq):
        try:
            return dq.list[0]
        except IndexError:
            return None

    def rightmost(dq):
        try:
            return dq.list[-1]
        except IndexError:
            return None


def menu():
    print("1. Insert element at the end of deque")
    print("2. Insert element at the beginning of deque")
    print("3. Delete leftmost element")
    print("4. Delete rightmost element")
    print("5. Print Deque")
    print("6. Print leftmost element")
    print("7. Print rightmost element")
    print("8. Number of elements in deque")
    print("9. Exit")


dq = deque()  # create deque class object

while True:
    menu()
    ch = int(input("Enter Choice: "))
    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            dq.ins_rear(x)
            dq.disp()
        case 2:
            x = eval(input("Enter element to be inserted: "))
            dq.ins_front(x)
            dq.disp()
        case 3:
            x = dq.del_front()
            if x is None:
                print("Deque is empty, deletion not permitted")
            else:
                print("Deleted element:", x)
            dq.disp()
        case 4:
            x = dq.del_rear()
            if x is None:
                print("Deque is empty, deletion not permitted")
            else:
                print("Deleted element:", x)
            dq.disp()
        case 5:
            dq.disp()
        case 6:
            x = dq.leftmost()
            if x is None:
                print("Deque is empty")
            else:
                print("Leftmost element:", x)
        case 7:
            x = dq.rightmost()
            if x is None:
                print("Deque is empty")
            else:
                print("Rightmost element:", x)
        case 8:
            print("Number of elements:", dq.size())
        case 9:
            exit()
'''Output:
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 1
Enter element to be inserted: 25
Deque: [25]
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 1
Enter element to be inserted: 10.8
Deque: [25, 10.8]
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 1
Enter element to be inserted: 'hyd'
Deque: [25, 10.8, 'hyd']
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 1
Enter element to be inserted: 3+4j
Deque: [25, 10.8, 'hyd', (3+4j)]
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 2
Enter element to be inserted: 44
Deque: [44, 25, 10.8, 'hyd', (3+4j)]
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 3
Deleted element: 44
Deque: [25, 10.8, 'hyd', (3+4j)]
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 4
Deleted element: (3+4j)
Deque: [25, 10.8, 'hyd']
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 5
Deque: [25, 10.8, 'hyd']
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 6
Leftmost element: 25
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 7
Rightmost element: hyd
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 8
Number of elements: 3
1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 9'''