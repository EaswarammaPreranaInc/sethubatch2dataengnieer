
#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from abc import ABC, abstractmethod

class datatype(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self, m, n):
        pass

    @abstractmethod
    def display(self):
        pass

class number(datatype):
    

    def get(self):
        self.x = int(input("Enter a number: "))  #  Reads number into self.x

    def add(self, m, n):
        self.x = m.x + n.x  #  Adds m.x and n.x, stores in self.x

    def display(self):
        print("Sum of the numbers:", self.x)  #  Prints result

class string(datatype):


    def get(self):
        self.x = input("Enter a string: ")  #  Reads string into self.x

    def add(self, m, n):
        self.x = m.x + n.x  # Joins m.x and n.x, stores in self.x

    def display(self):
        print("Join of the two strings:", self.x)  #  Prints result

def menu():
    print("\n1. Add numbers")
    print("2. Join strings")
    print("3. Exit")

#  Main program
if __name__ == "__main__":
    while True:
        menu()
        ch = int(input("Enter choice: "))  # Avoid eval

        if ch == 1:
            a = [number(), number(), number()]  # Create 3 number objects
        elif ch == 2:
            a = [string(), string(), string()]  #  Create 3 string objects
        else:
            break  #  Stop execution

        a[0].get()  # Read input into first object
        a[1].get()  #  Read input into second object
        a[2].add(a[0], a[1])  # Add/join and store in third object
        a[2].display()  # Print result