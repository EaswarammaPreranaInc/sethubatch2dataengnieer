#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):
	@abstractmethod
	def  get(self):
		 pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
class   number(datatype):
	def  get(self):
			self.x=int(input("Enter Any Number :"))  # How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' ,self.x)
class   string(datatype):
	def  get(self):
			self.x=input("Enter any String :") # How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x  # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.x)
# End  of  the  function
if  __name__ == '__main__':
	while  True:
			ch =input('Enter number/string/exit : ')
			if   ch == 'number':
					a=[number(),number(),number()]  #How  to  create  list  of  3  number  class  objects

			elif  ch  == 'string':
					a=[string(),string(),string()]  # How  to  create  list  of  3  string  class  objects
			elif ch == 'exit':
					break # How  to  stop  execution
			else:
				print("Invalid Choice")
			a[0].get()  # How  to  read  input  into  first  object
			a[1].get() # How  to  read  input  into  2nd  object
			a[2].add(a[0],a[1])  # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			a[2].display()  # How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')
