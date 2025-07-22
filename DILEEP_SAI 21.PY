a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#'Dictionary with print function'
print(a.keys())#'Keys of dictionary'
print(a.values())#'Values of dictionary'
print(a.items())#'All the tuples of dict_items object'
print("Elements of each tuple:")
for item in a.items():
    print(item) # prints (Keys, value)
print("Keys and values of dictionary:")
for k, v in a.items():
    print(f"Key: {k}, Value: {v}")
