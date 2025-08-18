a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}      # No output
print(a)                                                            # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))                                                      # <class 'dict'>
print(a[10])                                                        # Ramesh
print(a[20])                                                        # Kiran
print(a[15])                                                        # Amar
print(a[18])                                                        # Sita
print(a[19])                                                        # error
print(a[0])                                                         # error
print(a['Amar'])                                                    # error 
a[15] = 'Krishna'                                                   
del a[20]                                                           # Remove key 20
a[25] = 'Vamsi'                                                    
print(a)                                                            # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))                                                       # 4
print(a * 2)                                                        # error


a = {10: 'Hyd', 10: 'Sec'}                                        
print(a)                                                            # {10: 'Sec'}
print(len(a))                                                       # 1

b = {'R': 'Red', 'G': 'Green', 'B': 'Blue', 'Y': 'Yellow',
     'G': 'Gray', 'B': 'Black'}                                    
print(b)                                                            # {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))                                                       # 4

a = {True: 'Yes', 1: 'No', 1.0: 'May be'}
print(a)                                                            # {True: 'May be'}
print(len(a))                                                       # 1


a = {}                                                           
print(type(a))                                                      # <class 'dict'>
print(len(a))                                                       # 0
print(a)                                                            # {}

b = dict()                                                          
print(type(b))                                                      # <class 'dict'>
print(len(b))                                                       # 0
print(b)                                                            # {}

a = {}                                                             
print(type(a))                                                      # <class 'dict'>
print(len(a))                                                       # 0
print(a)                                                            # {}

b = dict()                                                          
print(type(b))                                                      # <class 'dict'>
print(len(b))                                                       # 0
print(b)                                                            # {}
