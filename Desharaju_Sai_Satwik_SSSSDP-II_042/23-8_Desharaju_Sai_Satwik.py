a = set()
a.add(True)
a.add(25)
a.add(10.8)
a.add(1)
a.add('Hyd')
a.add(25)
a.add(None)
a.add('Hyd')
a.add(1.0)
print(a)
a.add((10, 20, 30))  


a = {25, 10.8, 'Hyd', True}
tpl = (10, 20, 30)
print(a)
print(id(a))
a.add(tpl)
a.add('Sec')
print(a)
print(id(a))
print(len(a))
a.add(frozenset([100, 200, 300]))


s = set()
tpl = (10, 20, 15, 18)
s.add(tpl)
print(s)
print(len(s))


tpl = (10, 20, 15, 18, 10, 20)
s = set()
s.update(tpl)
print(len(s))
print(s)


a = [10, 20, 30]
b = {30, 40, 50}
c = (50, 60, 70)
s = set()
s.update(a, b, c)
print(s)
print(len(s))


a = set()
a.update('Rama Rao')
print(a)
print(len(a))


a = {10, 20, 15, 18}
print(a)
b = a.copy()
print(b)
print(a is b)
print(a == b)
c = a
print(a is c)


a = {25, 10.8, 'Hyd', True}
print(a)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a)


a = {25, 10.8, 'Hyd', True}
print(a)
a.remove('Hyd')
print(a)


a = {25, 10.8, 'Hyd', True}
print(a)
a.discard('Hyd')
print(a)
a.discard('Sec')
print(a)


a = {10, 20, 15, 18}
print(a)
a.clear()
print(a)
print(len(a))


a = {10, 20, 30, 40}
b = [30, 40, 50, 60]
print(a.union(b))
print(a | set(b))
print(set(b).union(a))
