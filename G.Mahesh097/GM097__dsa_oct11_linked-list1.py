# Write functions to create and print linked list

class node:
    def __init__(self, x):
        self.data = x
        self.link = None
		
class linked_list:
    def __init__(self):
        self.first = None

    def isempty(self):
        return self.first is None

    def disp(self):
        if self.isempty():
            print('Linked List is empty')
        else:
            p = self.first
            while p is not None:
                print(p.data, end='\t')
                p = p.link
            print()

    def append(self, new):
        if self.isempty():
            self.first = new
        else:
            last = self.first
            while last.link is not None:
                last = last.link
            last.link = new

    def create(self):
        try:
            self.first = None
            print('Enter values terminated by Ctrl+Z (or type any non-number to stop):')
            while True:
                x = eval(input())
                new = node(x)
                self.append(new)
        except:
            pass

# End of the class
if __name__ == '__main__':    
    a = linked_list()
    a.create()
    print('Linked List:', end=' ')
    a.disp()

'''
Output:
10
20
30
^Z  
Enter values terminated by Ctrl+Z (or type any non-number to stop):
Linked List: 10    20    30
'''
