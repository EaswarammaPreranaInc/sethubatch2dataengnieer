
class   Student:
	def   get(self):
		# How  to  read  roll  number  into  object  self
		self.rno=int(input("Enter roll number: "))
		# How  to  read  student  name  into  object  self
		self.name=input("Enter name: ")
		# How  to  read  gender  into  object  self
		self.gender=input("Enter Gender: ")
		# How  to  read  marks  of  3  subjects
		l=[]
		try:
			l.append(int(input()))
		except:
			self.marks=l
	def   compute(self):
		# How  to  calculate  total  marks
		sum=0
		for x in self.marks:
			sum+=x
		self.total=sum
		avg=sum/len(self.marks)
		self.average=avg
		avg=(avg/sum)*100
		for x in self.marks:
			if x<40:
				self.grade='Fail'
				return 
		if avg >= 70:
			self.grade='Distinction'
			return 
		elif avg >= 60:
			self.grade='First  class'
		elif avg>=50:
			self.grade='Second  class'
		else:
			self.grade='Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f'{self.rno} {self.name} {self.gender} {self.total} {self.average} {self.grade}' #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
a=Student()#How  to  create  Student  class  object
a.get()#How  to  read  inputs  into  object
a.compute()#How  to  store  results  in  object
a.disp()#How  to  print  object  with  disp()  method
print(a) #How  to  print  object  with  __str__()  method
print(a.__str__)
