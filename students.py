class   Student:
	def   get(self):
		self.rollno=int(input("Enter ROllNO : "))#How  to  read  roll  number  into  object  self
		self.name=input("Enter Name : ")#How  to  read  student  name  into  object  self
		self.gender=input("Enter Gender : ")#How  to  read  gender  into  object  self
		line=input("Enter marks of 3 subjects : ")
		list=line.split()
		self.marks=[]
		for i in list:
		    self.marks.append(eval(i))#How  to  read  marks  of  3  subjects
	def   compute(self):
		self.totalmarks=sum(self.marks)#How  to  calculate  total  marks
		self.avg=sum(self.marks)/len(self.marks)#How  to  calculate  average  marks
		if  self.marks[0] <40 or self.marks[1] <40 or self.marks[2] <40:
		    self.res='fail'# At  least  one  subject  is  below  40:
				#How  to  initilaize  grade  to  'Fail'
		elif  self.avg>= 70:
		    self.res='Distinction'
				# How  to  initilaize  grade  to  'Distinction'
		elif  self.avg  >= 60:
		    self.res='First  class'
				# How  to  initilaize  grade  to  'First  class'
		elif  self.avg  >= 50:
		    self.res='Second  class'
				# How  to  initilaize  grade  to  'Second  class'
		else:
		    self.res='Third  class'
				# How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rollno)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.totalmarks)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.res)
	def   __str__(self):
		return  F'RollNO : {self.rollno},Name : {self.name},Gender : {self.gender},Totalmarks : {self.totalmarks},Average : {self.avg},Grade : {self.res}'#All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
if __name__=='__main__':
    s=Student()#How  to  create  Student  class  object
    s.get()#How  to  read  inputs  into  object
    s.compute()#How  to  store  results  in  object
    s.disp()#How  to  print  object  with  disp()  method
    print(s.__str__())#How  to  print  object  with  _str_()  method
