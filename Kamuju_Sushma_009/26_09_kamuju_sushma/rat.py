import  math
class  Rat:
	def  get(self):
		self.p=int(input("Enter numerator:")) #How  to  read  numerator  into  object  self
		self.q=int(input("Enter Denominator:")) #How  to  read  denominator  into  object  self
		self.test() #How  to  call  test()  method
	def  test(self):
		# Ask  user  to  reenter  denom  when  denom  is  zero
		if self.q==0:
			self.q=int(input("Re enter the denominator:"))
			self.test()
	def    __str__(self):
			 return f'{self.p}/{self.q}' #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		# How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.p=(a.p*b.q +a.q+b.p)
		self.q=(a.q*b.q)
		self.simplify() #How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.p=(a.p*b.q -a.q+b.p)#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.q=(a.q*b.q) 
		self.simplify()#How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.p=(a.p*b.p) # How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.q=(a.q*b.q) 
		self.simplify() #How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.p=(a.p*b.q)#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.q=(a.q*b.p) 
		self.simplify() #How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			# How  to  find  gcd  of  numerator  and   denominator
			g=math.gcd(self.p,self.q)
			# How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
			self.p=(self.p)/g
			self.q=(self.q)/g
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''