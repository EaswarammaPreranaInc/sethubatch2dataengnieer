 #=====================================================Write  a  program  to  convert  postfix  to  prefix
from prog1b import *
def convert(postfix):
   s=stack()
   for ch in postfix:
      if ch.isdigit() or ch.isalpha():
         s.push(ch)
      else:
         op1=s.pop()
         op2=s.pop()
         new_expr=ch+op1+op2
         s.push(new_expr)
   return s.pop()
postfix=input('enter the string ')
print('prefix expression: ',convert(postfix))

#=====================================================Write  a  program  to  convert  prefix  to  postfix

from prog9b import *
def pre_post(postfix):
    prefix=prefix[::-1]
    s=stack()
    for ch in prefix:
      if ch.isdigit() or ch.isalpha():
         s.push(ch)
      else:
         op1=s.pop()
         op2=s.pop()
         new_expr=ch+op1+op2
         s.push(new_expr)
    return s.pop()
postfix=input('enter the string ')
print('postfix expression: ',pre_post(postfix))

#=====================================================Write  a  program  to  implement  priority  queue  using  list




#=================================================== Write  a  program  to  implement  min  priority  queue  using  list
class priority_queue:
	def __init__(self):
		self.pq = []

	def isempty(self):
		return len(self.pq) == 0

	def insert(self, x):
		self.pq.append(x)
		self.pq.sort()  # Lowest value has highest priority

	def delete(self):
		if self.isempty():
			return None
		return self.pq.pop(0)  # Remove highest priority (smallest value)

	def highest_priority(self):
		if self.isempty():
			return None
		return self.pq[0]

	def smallest_priority(self):
		if self.isempty():
			return None
		return self.pq[-1]

	def disp(self):
		print('Priority Queue:', self.pq)

	def size(self):
		return len(self.pq)

def menu():
	print('1. Insertion')
	print('2. Deletion')
	print('3. Print priority queue')
	print('4. Highest priority element of priority queue')
	print('5. Smallest priority element of priority queue')
	print('6. Number of elements in the priority queue')
	print('7. Exit')

if __name__ == '__main__':
	pq = priority_queue()
	while True:
		menu()
		ch = int(input('Enter choice : '))
		match ch:
			case 1:
				x = eval(input('Enter element to be inserted : '))
				pq.insert(x)
				pq.disp()
			case 2:
				deleted = pq.delete()
				if deleted is None:
					print('Priority queue is empty, deletion is not permitted')
				else:
					print('Deleted element :', deleted)
				pq.disp()
			case 3:
				pq.disp()
			case 4:
				hp = pq.highest_priority()
				if hp is None:
					print('Priority queue is empty')
				else:
					print('Highest priority element :', hp)
			case 5:
				sp = pq.smallest_priority()
				if sp is None:
					print('priority queue is empty')
				else:
					print('Smallest priority element :', sp)
			case 6:
				print('Number of elements :', pq.size())
			case 7:
				exit()
