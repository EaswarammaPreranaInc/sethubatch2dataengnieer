'''


linked list implementation in python
what is linked list?

a group of nodes represented in non contiguous memory locations

A linked list is a linear data structure where each element (node) contains a value 
and a reference (link) to the link node in the sequence. Unlike arrays, 
linked lists do not require contiguous memory allocation, allowing 
for dynamic memory usage and efficient insertions and deletions.


types of linked list:

1) singly linked list
2) doubly linked list
3) circular linked list
4) circular doubly linked list

1) singly linked list

    first node contains the address of the second node
    last node contains the address of None
    each contains two parts:
        1) data
        2) link (address of the link node)
        
        
2) doubly linked list

    each node contains three parts:
        1) data
        2) link (address of the link node)
        3) prev (address of the previous node)

3) circular linked list


    a.first data --> 1
    a.second data --> 2
    a.third data --> 3
    a.fourth data --> 4
    

'''


class node :
    def __init__(self, x):
        self.data = x # 
        self.link = None # 
        
                
class linked_list :
    
    def __init__(self):
        self.first = None  # 
        
        
    def isempty(self):
        return self.first == None # return  True  when  linked list  is  empty  and  False  otherwise
    
    
    def disp(a):
        if a.isempty(): # checking whether linked list is empty
            print('linked list is empty') # 
        else:
            p = a.first # creating a pointer p and assigning it to the first node
            while p != None: # traversing the linked list until p becomes None
                print(p.data, end = ' ') 
                p = p.link # moving p to the link node
            print() 
    
    
    def append(a,new):
        if a.isempty(): # checking whether linked list is empty
            a.first = new # if linked list is empty, assign new node to first
        else:
            last = a.first # creating a pointer last and assigning it to the first node
            while last.link != None: # traversing the linked list until last.link becomes None
                last = last.link # moving last to the link node
            last.link = new # assigning new node to last.link
            
            
    def create(a):
        try:
            a.first = None
            print('Enter the values terminated by crtl + Z')
            while True: # 
                x = eval(input())
                new = node(x) # 
                a.append(new)
                
        except:
            pass
        
    # def size(a):
    #     count = 0
    #     p = a.first
    #     while p != None:
    #         count += 1
    #         p = p.link
    #     return count
    
    # def search(a,x):
    #     p = a.first
    #     while p != None:
    #         if p.data == x:
    #             return True
    #         p = p.link
    #     return False
        
        
if __name__ == '__main__':
    a = linked_list()
    a.create()
    print('Linked list : ', end= '')
    a.disp()
    
    print('size of Linked list :',end = ' ')
    print(a.size())
    
    
    x = eval(input('Enter the element to be searched: '))
    if a.search(x):
        print(x,'searched element is found in the linked list')
    else:
        print(x, 'searched element is not found in the linked list')
