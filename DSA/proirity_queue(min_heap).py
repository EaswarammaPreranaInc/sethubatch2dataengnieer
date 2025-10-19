
# ------------------------------ MIN HEAP --------------------------------------
class priority:
    def __init__(p):
        p.l=[]   
    def push(p,x):
        p.l.append(x)
        p.l.sort()
        
    def pop(p):
        return p.l.pop(0)
        
    def smallest(p):
        try:
            return p.l[0]
        except:
            return None
    def largest(p):
        try:
            return p.l[-1]
        except:
            return None
            
    def length(p):
        return len(p.l)
    def disp(p):
        print('Priority Queue:', p.l)
        
def menu():
    print("\n---Priority Queue ---")
    print('1. Insertion')
    print('2. Deletion')
    print('3. print PriorityQueue ')
    print('4. smallest element of Priority Queue :')
    print('5. Largest Element of Priority Queue :')
    print('6. Number of  Elements in Priority Queue :')
    print('7. Exit')


if __name__=='__main__':
    
    p=priority()
    
    while(True):
        menu()
        try:
            ch = int(input('Enter choice: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match ch:
            case 1:
                x = eval(input('Enter element to be inserted: '))
                p.push(x)
                p.disp()

            case 2:
                try :
                    print("Deleted Element is : ",p.pop())
                except:
                    print("Queue is Empty !  Deletion is not possible")
                p.disp()

            case 3:
                p.disp()
            case 4:
                x = p.smallest()
                if x is None:
                    print('Priority Queue is Empty')
                else:
                    print('Smallest element:', x)
            case 5:
                x=p.largest()
                if x is None:
                    print('Priority Queue is Empty')
                else:
                    print('Largest element:',x)
            case 6:
                print('Number of elements:', p.length())

            case 7:
                print("Exiting program...")
                break

            case _:
                print("Invalid choice! Please enter a number between 1–7 :")

            
        
    





    

    