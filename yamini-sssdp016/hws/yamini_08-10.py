'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
a=c1.__dict__
for i,j in a.items():
	if i.startswith('__') and i.endswith('__'):
		a.remove(i)
print(a)


#  End  of  the  class