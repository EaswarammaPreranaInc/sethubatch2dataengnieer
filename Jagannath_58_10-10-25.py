Write  a  program  to  convert  postfix  to  prefix
def is_operator(c):
    return c in "+-*/^"
def postfix_to_prefix(postfix):
    stack = []
    for ch in postfix:
        if not is_operator(ch):
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            expression = ch + op2 + op1
            stack.append(expression)
    return stack[-1]
postfix_expr = "AB+C*"
print("Postfix Expression:", postfix_expr)
print("Prefix Expression:", postfix_to_prefix(postfix_expr))

Write  a  program  to  convert  prefix  to  postfix
def is_operator(c):
    return c in "+-*/^"
def prefix_to_postfix(prefix):
    stack = []
    for ch in reversed(prefix):
        if not is_operator(ch):
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            expression = op1 + op2 + ch
            stack.append(expression)
    return stack[-1]
prefix_expr = "*+ABC"
print("Prefix Expression:", prefix_expr)
print("Postfix Expression:", prefix_to_postfix(prefix_expr))

Write  a  program  to  implement  priority  queue  using  list
class PriorityQueue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item, priority):
        self.queue.append((item, priority))
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        highest_priority_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[highest_priority_index][1]:
                highest_priority_index = i
        item = self.queue.pop(highest_priority_index)
        return item[0]
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Priority Queue:")
            for item, priority in self.queue:
                print(f"Item: {item}, Priority: {priority}")
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)
pq.display()
print("\nDequeued element:", pq.dequeue())
pq.display()
