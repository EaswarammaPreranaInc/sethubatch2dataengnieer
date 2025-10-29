
import new
a=[]
for i in dir(new):
    if i.startswith('__') and i.endswith('__'):
        continue
    else:
        a.append(i)
print(a)