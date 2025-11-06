# Program to implement Queue operations (insert, remove, display)

class Queue:
    def __init__(self):
        self.items = []    # Initialize empty queue
        
    def is_empty(self):
        return len(self.items) == 0
        
    def enqueue(self, item):
        """Insert item at the rear of queue"""
        self.items.append(item)
        print(f"Inserted {item} at rear of queue")
        
    def dequeue(self):
        """Remove and return item from front of queue"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
        
    def display(self):
        """Display all elements in the queue"""
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", end=" ")
            for item in self.items:
                print(item, end=" ")
            print()
            
def menu():
    print("\n1. Insert element (Enqueue)")
    print("2. Remove element (Dequeue)")
    print("3. Display queue")
    print("4. Exit")

if __name__ == "__main__":
    queue = Queue()
    
    while True:
        menu()
        try:
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                item = input("Enter element to insert: ")
                queue.enqueue(item)
                queue.display()
                
            elif choice == 2:
                item = queue.dequeue()
                if item is not None:
                    print(f"Removed element: {item}")
                else:
                    print("Queue is empty")
                queue.display()
                
            elif choice == 3:
                queue.display()
                
            elif choice == 4:
                print("Exiting program...")
                break
                
            else:
                print("Invalid choice! Please try again.")
                
        except ValueError:
            print("Please enter a valid number!") 