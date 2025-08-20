# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
cubes = [x**3 for x in (2 , 4, 6 , 8, 10)]
print(cubes)





'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
a = ['hyd' , 'pune' , 'chennai' , 'vijayawada']
result = []
for i in a:
    a[0] = i[0].upper()
    result.append(a[0])
print(result)
   






'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
a = [i[0]  for i in a]
print(a)







'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

input = "hyd is green city"
b = input.upper()
c = b.split()
e = []
for i in range(len(c)) :
    d = print(f'[{c[i]} , {len(c[i])}]')
    e.append(d)






