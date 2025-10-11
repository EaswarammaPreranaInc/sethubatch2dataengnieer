#  Write  a  program  to  convert  postfix  to  prefix         

def is_operator(ch):
    return ch in ['+', '-', '*', '/', '^']

def postfix_to_prefix(postfix):
    stack = []
    
    # scan each symbol in the postfix expression
    for ch in postfix:
        if not is_operator(ch):
            # if operand, push to stack
            stack.append(ch)
        else:
            # if operator, pop two operands
            op1 = stack.pop()
            op2 = stack.pop()
            # form prefix expression
            new_expr = ch + op2 + op1
            # push back to stack
            stack.append(new_expr)
    
    # final element in stack is the prefix expression
    return stack[-1]

# Example
postfix_expr = input("Enter a postfix expression: ")
prefix_expr = postfix_to_prefix(postfix_expr)
print("Prefix expression:", prefix_expr)

-----------------------------------------------------------
#  Write  a  program  to  convert  prefix  to  postfix      

def is_operator(ch):
    return ch in ['+', '-', '*', '/', '^']

def prefix_to_postfix(prefix):
    stack = []

    # read the prefix expression from right to left
    for ch in prefix[::-1]:
        if not is_operator(ch):
            # if operand, push to stack
            stack.append(ch)
        else:
            # if operator, pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # form postfix expression
            new_expr = op1 + op2 + ch
            # push the new expression back to stack
            stack.append(new_expr)

    # final element in stack is the postfix expression
    return stack[-1]

# Example
prefix_expr = input("Enter a prefix expression: ")
postfix_expr = prefix_to_postfix(prefix_expr)
print("Postfix expression:", postfix_expr)
---------------------------------------------------------------------
Write  a  program  to  implement  priority  queue  using  list      

class PriorityQueue:
    def _init_(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue")

    def delete(self):
        if self.is_empty():
            print("Queue is empty, nothing to delete")
            return

        # find element with highest priority (lowest value)
        highest_priority = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] < self.queue[highest_priority][1]:
                highest_priority = i

        item = self.queue.pop(highest_priority)
        print(f"Deleted item: {item[0]} with priority {item[1]}")

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Priority Queue:")
            for item in self.queue:
                print(f"Item: {item[0]}, Priority: {item[1]}")

# Example usage
pq = PriorityQueue()
pq.insert(("Job1", 3))
pq.insert(("Job2", 1))
pq.insert(("Job3", 2))
pq.display()
pq.delete()
pq.display()