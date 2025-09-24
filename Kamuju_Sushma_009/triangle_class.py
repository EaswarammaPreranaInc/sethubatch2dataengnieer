import  math
class  triangle:
	def  get(self):
		# How  to  read  three  sides  into  object  self
		self.x=int(input("Enter 1st side: "))
		self.y=int(input("Enter 2nd side: "))
		self.z=int(input("Enter 3rd side: "))
		
	def  test(self):
		if self.x+self.y>=self.z and self.y+self.z>=self.x and self.z+self.x>=self.y:
			pass
		else:
			print("Not a triangle")
			exit()
		# if  sum  of  every  2  sides  >=  3rd  side:
		# 		Do  nothing
		#  else:
		# 		print('Not  a  triangle')
		# 		How  to  stop  execution
	def  area(self):
			s=(self.x+self.y+self.z)/2
			area=math.sqrt(s*(s-self.x)*(s-self.y)*(s-self.z))
			return   area
	def  peri(self):
			return  self.x+self.y+self.z
# End of the class
tri=triangle()#How  to  create  triangle  class  object
tri.get()#How  to  read  inputs  into  object
tri.test()#How  to  test  whether  inputs  are  valid
print('Area : ',   tri.area())
print('Perimeter : ',  tri.peri())