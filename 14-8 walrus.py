'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')'''


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while  (index := a.find('is' , index + 1))!= -1:
    print(index)
print('End')
