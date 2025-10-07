# Program to implement deque using list
class deque:
	def __init__(self):
		self.list = []

	def isempty(self):
		return self.list == []

	def ins__rear(self, x):
		self.list.append(x)

	def ins__front(self, x):
		self.list.insert(0, x)

	def del__front(self):
		if self.isempty():
			print("Deque is empty. Cannot delete from front.")
			return None
		return self.list.pop(0)

	def del__rear(self):
		if self.isempty():
			print("Deque is empty. Cannot delete from rear.")
			return None
		return self.list.pop()

	def disp(self):
		print(self.list)

	def size(self):
		return len(self.list)

	def left_most(self):
		if self.isempty():
			print("Deque is empty.")
			return None
		print(self.list[0])
		return self.list[0]

	def right_most(self):
		if self.isempty():
			print("Deque is empty.")
			return None
		print(self.list[-1])
		return self.list[-1]

def menu():
	print('1. Insert element at the end of deque')
	print('2. Insert element at the beginning of deque')
	print('3. Delete left most element')
	print('4. Delete right most element')
	print('5. Print Deque')
	print('6. Print left most element')
	print('7. Print right most element')
	print('8. Number of elements in deque')
	print('9. Exit')

if __name__ == '__main__':
	dq = deque()
	while True:
		menu()
		try:
			ch = int(input('Enter Choice: '))
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue
		match ch:
			case 1:
				x = input('Enter element to be inserted: ')
				dq.ins__rear(x)
				dq.disp()
			case 2:
				x = input('Enter element to be inserted: ')
				dq.ins__front(x)
				dq.disp()
			case 3:
				deleted = dq.del__front()
				if deleted is not None:
					print(f"Deleted left most element: {deleted}")
				dq.disp()
			case 4:
				deleted = dq.del__rear()
				if deleted is not None:
					print(f"Deleted right most element: {deleted}")
				dq.disp()
			case 5:
				dq.disp()
			case 6:
				dq.left_most()
			case 7:
				dq.right_most()
			case 8:
				print(f"Number of elements in deque: {dq.size()}")
			case 9:
				print("Exiting program.")
				break
			case _:
				print("Invalid choice. Please try again.")