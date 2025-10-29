#  Write  Methods  to  create  and  print  circular  linked  list

class node:
        def __init__(self, x):
                self.data = x                      # How to initialize data field with 'x'
                self.next = None                   # Initialize next field with None

class linkedlist:
        def __init__(a):
                a.first = None                     # How to initialize first with None

        def isempty(a):
                return a.first == None             # return True when linked list is empty and False otherwise

        def disp(a):
                if a.isempty():
                        print('Linked List is empty')       # if linked list is empty
                else:
                        temp = a.first
                        while True:
                                print(temp.data, end=' ')   # How to print each node of circular linked list
                                temp = temp.next
                                if temp == a.first:
                                        break
                        print()

        def append(a, new):
                newnode = node(new)
                if a.isempty():
                        a.first = newnode                   # How to append new node to empty linked list
                        newnode.next = a.first
                else:
                        temp = a.first
                        while temp.next != a.first:
                                temp = temp.next
                        temp.next = newnode                 # How to append new node non-empty linked list
                        newnode.next = a.first

        def create(a):
                n = int(input("Enter number of nodes: "))   # How to create a linked list by appending each node
                for i in range(n):
                        x = int(input("Enter data: "))
                        a.append(x)

# End of the class

if __name__ == '__main__':
        cll = linkedlist()                                 # How to create linked list
        cll.create()
        cll.disp()                                         # How to print linked list
