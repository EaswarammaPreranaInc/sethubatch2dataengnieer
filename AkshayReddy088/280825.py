'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes

Enter String:RamA raO
{'A': 3, 'O': 1}
'''

# x1 = input("Enter a string:")
# b = {}
# x1 = sorted(set(x1.upper()))
# x2 = set('AEIOU')
# for x in x1:
#     if x in x2:
#         b[x] = b.get(x,0)+1
# print(b)





    # Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) 
print(b)
a . update(b)


#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)