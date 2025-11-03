#1 Write  destructor  to  delete  whole  linked  list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def __del__(self):
        current = self.head
        while current:
            temp = current
            current = current.next
            del temp
        self.head = None
        print('Linked list is empty')

ll = sll()
ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked list before deletion:")
ll.display()

del ll 

#2 Write  a  method  to  reverse  linked  list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next  
            cur.next = prev  
            prev = cur    
            cur = next      
        self.head = prev 
ll = sll()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print('Input Linked List:')
ll.print_list()
ll.reverse()

print('Reversed Linked List:')
ll.print_list()

