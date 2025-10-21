class node:
    def __init__(self, x):
        self.data = x
        self.link = None   # important to initialize link

class linkedlist:
    def __init__(self):
        self.first = None

    def isempty(self):
        return self.first is None

    def append(self, new):
        if self.isempty():
            self.first = new
            new.link = self.first  # circular link to itself
        else:
            last = self.first
            while last.link != self.first:
                last = last.link
            last.link = new
            new.link = self.first   # close the circle

    def create(self):
        try:
            self.first = None
            print("Enter values terminated by Ctrl+Z :")
            while True:
                x = eval(input())  # example: 10 ↵ 20 ↵ 30 ↵ Ctrl+Z
                new = node(x)
                self.append(new)
        except EOFError:
            pass

    def disp(self):
        if self.isempty():
            print('Linked List is empty')
            return
        else:
            p = self.first
            while True:
                print(p.data, end='\t')
                p = p.link
                if p == self.first:
                    break
            print()

# ---- Main Program ----
if __name__ == '__main__':
    ll = linkedlist()
    ll.create()   # create circular linked list
    print("Circular Linked List elements:")
    ll.disp()     # display circular linked list
