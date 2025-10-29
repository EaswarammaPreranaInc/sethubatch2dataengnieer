
class node:
    def __init__(self, x):
        self.data = x  # data part of the node
        self.link = None  # link part of the node
    

class sll(linked_list):

    def __init__(self):
        super().__init__()

    def size(self):
        count = 0
        p = self.first
        while p != None:
            count += 1
            p = p.link
        return count
    
    def search(a,x):
        p = a.first
        while p != None:
            if p.data == x:
                return True
            p = p.link
        return False
    
