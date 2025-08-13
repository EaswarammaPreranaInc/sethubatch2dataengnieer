
#Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

x=input('Enter a string: ').upper()
a=''
for i in range(0,len(x)):
    if x[i]  in 'AEIOU' and x[i] not in a:
        a+=x[i]
print('distinct  vowels  of  the  string: ',a)

'''
output:
Enter a string: hyderabad
distinct  vowels  of  the  string:  EA
'''
