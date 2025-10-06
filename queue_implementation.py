class queue:
    def __init__(q):
        # Create an empty queue
        q.list = []

    def isempty(q):
        # Return True when queue is empty, otherwise False
        return len(q.list) == 0

    def enqueue(q, x):
        # Insert 'x' into the queue (at the end)
        q.list.append(x)

    def dequeue(q):
        # Remove first element of the queue and return it
        # Return -1 when deletion is not possible (empty queue)
        if q.isempty():
            return -1
        else:
            return q.list.pop(0)

    def first(q):
        # Return first element of queue
        if q.isempty():
            return -1
        else:
            return q.list[0]

    def last(q):
        # Return last element of queue
        if q.isempty():
            return -1
        else:
            return q.list[-1]

    def disp(q):
        # Print the queue
        if q.isempty():
            print("Queue is empty.")
        else:
            print("Queue:", q.list)

    def size(q):
        # Return number of elements in the queue
        return len(q.list)

# End of class

def menu():
    print("\n--- Queue Operations Menu ---")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Print queue")
    print("4. First element of queue")
    print("5. Last element of queue")
    print("6. Number of elements in the queue")
    print("7. Exit")

# Create queue class object
q1 = queue()

# Menu-driven program
menu()
ch = int(input("Enter choice: "))

while ch != 7:
    match ch:
        case 1:
            x = eval(input("Enter element to be inserted: "))
            q1.enqueue(x)
            q1.disp()

        case 2:
            deleted = q1.dequeue()
            if deleted == -1:
                print("Queue underflow! Deletion not possible.")
            else:
                print("Deleted element:", deleted)
            q1.disp()

        case 3:
            q1.disp()

        case 4:
            print("First element of queue:", q1.first())

        case 5:
            print("Last element of queue:", q1.last())

        case 6:
            print("Number of elements in the queue:", q1.size())

        case _:
            print("Invalid choice! Please try again.")

    menu()
    ch = int(input("Enter choice: "))

print("Program terminated.")
