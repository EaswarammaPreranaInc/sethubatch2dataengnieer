#1:

class D:
    def __init__(self):
        super().__init__()
        print('class D constructor')

class E:
    def __init__(self):
        super().__init__()
        print('class E constructor')

class F:
    def __init__(self):
        super().__init__()
        print('class F constructor')

class B(D, E):
    def __init__(self):
        super().__init__()
        print('class B constructor')

class C(D, E, F):
    def __init__(self):
        super().__init__()
        print('class C constructor')

class A(B, C):
    def __init__(self):
        super().__init__()
        print('class A constructor')

print(A.mro())
obj = A()
print('Bye')
'''
Output:

[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye




# Part 2: Circular Linked List Implementation

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def isempty(self):
        return self.first is None

    def disp(self):
        if self.isempty():
            print('Linked List is empty')
        else:
            temp = self.first
            while True:
                print(temp.data, end=' ')
                temp = temp.next
                if temp == self.first:
                    break
            print()

    def append(self, new):
        new_node = Node(new)
        if self.isempty():
            self.first = new_node
            new_node.next = self.first  # circular link
        else:
            temp = self.first
            while temp.next != self.first:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.first

    def create(self):
        n = int(input('Enter number of nodes: '))
        for i in range(n):
            x = input('Enter data: ')
            self.append(x)

if __name__ == '__main__':
    l = LinkedList()
    l.create()
    l.disp()
```
Example Output (for inputs 3 → A, B, C):

Enter number of nodes: 3
Enter data: A
Enter data: B
Enter data: C
A B C