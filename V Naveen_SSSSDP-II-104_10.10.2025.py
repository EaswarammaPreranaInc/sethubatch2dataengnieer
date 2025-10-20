#  Write  a  program  to  convert  postfix  to  prefix

def postfix_to_prefix(expr):
    stack = []
    operators = ['+', '-', '*', '/', '^']

    for ch in expr.split():
        if ch not in operators:
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = ch + " " + op1 + " " + op2
            stack.append(new_expr)

    return stack[-1]

expr = input("Enter Postfix Expression: ")
print("Prefix Expression:", postfix_to_prefix(expr))


#  Write  a  program  to  convert  prefix  to  postfix

def prefix_to_postfix(expr):
    stack = []
    operators = ['+', '-', '*', '/', '^']

    # Scan right to left
    for ch in expr.split()[::-1]:
        if ch not in operators:
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = op1 + " " + op2 + " " + ch
            stack.append(new_expr)

    return stack[-1]

expr = input("Enter Prefix Expression: ")
print("Postfix Expression:", prefix_to_postfix(expr))


# Write  a  program  to  implement  priority  queue  using  list

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        print(f"Inserted ({item}, priority={priority})")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return
        # Find highest priority (larger number = higher priority)
        highest = max(self.queue, key=lambda x: x[1])
        self.queue.remove(highest)
        print(f"Removed ({highest[0]}, priority={highest[1]})")

    def display(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            print("Current Queue (item, priority):")
            for item, p in sorted(self.queue, key=lambda x: x[1], reverse=True):
                print(f"{item} ({p})")


# --- Main Program ---
pq = PriorityQueue()

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item: ")
        priority = int(input("Enter priority: "))
        pq.enqueue(item, priority)
    elif choice == 2:
        pq.dequeue()
    elif choice == 3:
        pq.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

