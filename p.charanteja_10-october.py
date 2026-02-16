# Postfix to Prefix Conversion

def is_operator(c):
    return c in "+-*/^"

def postfix_to_prefix(postfix):
    stack = []
    for ch in postfix:
        if not is_operator(ch):
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            expr = ch + b + a
            stack.append(expr)
    return stack[-1]
'''
# Example usage
postfix_expr = "ABC*+"
result = postfix_to_prefix(postfix_expr)
print("Prefix expression:", result) #Prefix expression: +A*BC
'''





# Prefix to Postfix Conversion

def prefix_to_postfix(prefix):
    stack = []
    # Read right to left
    for ch in reversed(prefix):
        if not is_operator(ch):
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            expr = a + b + ch
            stack.append(expr)
    return stack[-1]
'''
# Example usage
prefix_expr = "+A*BC"
result = prefix_to_postfix(prefix_expr)
print("Postfix expression:", result) #Postfix expression: ABC*+
'''




# Priority Queue Implementation Using List

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)
        self.queue.sort(reverse=True)  # Highest priority first

    def delete(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove highest priority element
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def display(self):
        print("Priority Queue:", self.queue)
'''
# Example usage
pq = PriorityQueue()
pq.insert(5)
pq.insert(1)
pq.insert(3)
pq.display()    # Output: [5, 3, 1]
print(pq.delete())  # Output: 5
pq.display()
'''
