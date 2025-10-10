: #  Write  a  program  to  convert  postfix  to  prefix

# Program to convert Postfix expression to Prefix

def isOperator(x):
    return x in ['+', '-', '*', '/', '^']

def postfix_to_prefix(postfix):
    stack = []
    for ch in postfix:
        if not isOperator(ch):
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = ch + op2 + op1
            stack.append(new_expr)
    return stack[-1]

# Example
postfix = "AB+C*"
print("Postfix:", postfix)
print("Prefix:", postfix_to_prefix(postfix))




: #  Write  a  program  to  convert  prefix  to  postfix
     
# Program to convert Prefix expression to Postfix

def isOperator(x):
    return x in ['+', '-', '*', '/', '^']

def prefix_to_postfix(prefix):
    stack = []
    # Traverse from right to left
    for ch in reversed(prefix):
        if not isOperator(ch):
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = op1 + op2 + ch
            stack.append(new_expr)
    return stack[-1]

# Example
prefix = "*+ABC"
print("Prefix:", prefix)
print("Postfix:", prefix_to_postfix(prefix))




: Write  a  program  to  implement  priority  queue  using  list

# Program to implement Priority Queue using List

class PriorityQueue:
    def _init_(self):
        self.queue = []

    def insert(self, element, priority):
        self.queue.append((element, priority))
        print(f"Inserted ({element}, Priority={priority})")

    def delete(self):
        if not self.queue:
            print("Queue is empty")
            return
        # Find highest priority (smallest number = highest priority)
        highest = min(self.queue, key=lambda x: x[1])
        self.queue.remove(highest)
        print(f"Deleted element: {highest[0]} (Priority={highest[1]})")

    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Priority Queue contents:")
            for elem, pri in sorted(self.queue, key=lambda x: x[1]):
                print(f"Element: {elem}, Priority: {pri}")

# Example
pq = PriorityQueue()
pq.insert('A', 3)
pq.insert('B', 1)
pq.insert('C', 2)
pq.display()
pq.delete()
pq.display()
