# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . find('is')
# while  index != -1:
# 	print(index)
# 	index = a . find('is' , index + 1)
# print('End')

#Modify following program with walrus operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index=0
while (index := a.find('is',index)) != -1:
    print(index)
    index+=1
print('End')
'''

#Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index=0
while True:
    try:
        index=a.index('is',index)
        print(index)
        index+=1
    except ValueError:
        break
print('End')
'''
# Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = len(a)  
while index!=-2:
    index=a.rfind('is',0,index)
    print(index)
    index-=1
'''

# Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order
# Let  input  be  Z9K3PA7D51
# What  is  the  output ?  --->  ADKPZ13579
'''
a=input()
num=[]
char=[]
for i in a:
    if i.isdigit():
        num.append(i)
    else:
        char.append(i)
num.sort()
char.sort()
print("".join(char+num))
'''

#  Find  outputs  (Home  work)
#a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
# print(a.count(' '))   # 3
# print(a.count('\t'))  # 3
# print(a.count('\n'))  # 3


# Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

# Let  input  be  'babble'
# What  is  the  output ?  ---> ba**le
'''
a=input()
first_char = a[0]
result = first_char + a[1:].replace(first_char, '*')
print(result)
'''

#  Find  outputs  (Home  work)
# a = '15:36:48'
# print(a . split(':'))   ['15', '36', '48']
# print(a)                15:36:48

# Find Outputs (Home work)
# a = 'Hyd\nis green\tcity'
# print(a.split(' '))      # ['Hyd\nis', 'green\tcity']
# print(a.split())         # ['Hyd', 'is', 'green', 'city']
# print(a.split('green'))  # ['Hyd\nis ', '\tcity']
# print(a.split(''))       # ValueError: empty separator
#
# a = 'Hyd\tis\tgreen\tcity'
# print(a.split('\t'))   # ['Hyd', 'is', 'green', 'city']
# print(a.split())       # ['Hyd', 'is', 'green', 'city']
# print(a.split(' '))    # ['Hyd\tis\tgreen\tcity']

# a = 'Hyd   is   green   city'
# print(a.split())       # ['Hyd', 'is', 'green', 'city']
# print(a.split(' '))    # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# a = 'www.gmail.com'
# print(a.split('.'))    # ['www', 'gmail', 'com']

# Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
# Let  input  be  123+45+6+789
# Print  the  sum  result
'''
a = input("Enter an expression with + symbols: ")
result = sum(int(num) for num in a.split('+'))
print("The sum is:", result)
'''

# Write  a  program  to  sort  string  in  alphabetical  order
# Let  input  be  RAJESH
# What  is  the  output ?  --->  AEHJRS
'''a = input("Enter a string: ")
sorted_string = ''.join(sorted(a))
print("Sorted string:", sorted_string)
''' 



# Write  a  program  to  reverse  each  word  of  the  sentence

# 1) Let  input  be  Hyd  is  green  city
#     What  is  the  output ?  ---> dyH si neerg ytic

'''a = input("Enter a sentence: ")
reversed_words = ' '.join(word[::-1] for word in a.split())
print("Reversed words:", reversed_words)
'''
