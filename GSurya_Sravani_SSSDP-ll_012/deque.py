class deque:
    def __init__(self):
        # Create an empty deque
        self.list = []

    def isempty(self):
        # Check if deque is empty
        return self.list == []

    def ins_rear(self, x):
        # Insert 'x' at the end of deque
        self.list.append(x)

    def ins_front(self, x):
        # Insert 'x' at the beginning of deque
        self.list.insert(0, x)

    def del_front(self):
        # Remove leftmost element of deque and return it
        if not self.isempty():
            return self.list.pop(0)
        else:
            return None

    def del_rear(self):
        # Remove rightmost element of deque and return it
        if not self.isempty():
            return self.list.pop()
        else:
            return None

    def disp(self):
        # Display deque
        print("Deque:", self.list)

    def size(self):
        # Return number of elements in deque
        return len(self.list)


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


# Create deque object
q = deque()

# Main loop
while True:
    menu()
    ch = int(input("Enter Choice: "))

    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            q.ins_rear(x)
            q.disp()

        case 2:
            x = eval(input("Enter element to be inserted: "))
            q.ins_front(x)
            q.disp()

        case 3:
            val = q.del_front()
            if val is not None:
                print("Deleted element (front):", val)
            else:
                print("Deque is empty!")
            q.disp()

        case 4:
            val = q.del_rear()
            if val is not None:
                print("Deleted element (rear):", val)
            else:
                print("Deque is empty!")
            q.disp()

        case 5:
            q.disp()

        case 6:
            if not q.isempty():
                print("Leftmost element:", q.list[0])
            else:
                print("Deque is empty!")

        case 7:
            if not q.isempty():
                print("Rightmost element:", q.list[-1])
            else:
                print("Deque is empty!")

        case 8:
            print("Number of elements in deque:", q.size())

        case 9:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Try again.")










Enter Choice: 1
Enter element to be inserted: 13
Deque: [12, 13]

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
Enter element to be inserted: 45
Deque: [12, 13, 45]

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
Number of elements in deque: 3

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
Enter element to be inserted: 23
Deque: [23, 12, 13, 45]

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
Enter element to be inserted: 13
Deque: [13, 23, 12, 13, 45]

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
Deleted element (front): 13
Deque: [23, 12, 13, 45]

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
Deleted element (front): 23
Deque: [12, 13, 45]

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
Leftmost element: 12

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
Rightmost element: 45

1. Insert element at the end of deque
2. Insert element at the beginning of deque
3. Delete leftmost element
4. Delete rightmost element
5. Print Deque
6. Print leftmost element
7. Print rightmost element
8. Number of elements in deque
9. Exit
Enter Choice: 9
Exiting program...
