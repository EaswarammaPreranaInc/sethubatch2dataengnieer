class stack:
    def __init__(s):
        s.list = []   # Create an empty stack

    def isempty(s):
        return s.list == []   # Return True when stack is empty

    def push(s, x):
        s.list.append(x)   # Insert 'x' into the stack

    def pop(s):
        try:
            return s.list.pop()   # Delete and return the last element
        except IndexError:
            return None   # Return None when deletion is not possible

    def peek(s):
        try:
            return s.list[-1]   # Return the last element of the stack
        except IndexError:
            return None

    def disp(s):
        print('Stack:', s.list)   # Print stack

    def size(s):
        return len(s.list)   # Return number of elements in the stack


def menu():
    print("\n--- Stack Menu ---")
    print('1. Insertion')
    print('2. Deletion')
    print('3. Print Stack')
    print('4. Last element of stack')
    print('5. Number of elements in the stack')
    print('6. Exit')


if __name__ == '__main__':
    s = stack()   # Create stack class object
    while True:
        menu()
        try:
            ch = int(input('Enter choice: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match ch:
            case 1:
                x = eval(input('Enter element to be inserted: '))
                s.push(x)
                s.disp()

            case 2:
                x = s.pop()
                if x is None:
                    print('Stack is empty, deletion not permitted')
                else:
                    print('Deleted element:', x)
                s.disp()

            case 3:
                s.disp()

            case 4:
                x = s.peek()
                if x is None:
                    print('Stack is empty')
                else:
                    print('Last element:', x)

            case 5:
                print('Number of elements:', s.size())

            case 6:
                print("Exiting program...")
                break

            case _:
                print("Invalid choice! Please enter a number between 1–6.")
