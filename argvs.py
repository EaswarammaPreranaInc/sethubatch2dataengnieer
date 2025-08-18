from sys import argv

print(argv)
print(type(argv))

for i in range(len(argv)):
    print(f"argv[{i}] = {argv[i]}")

print(argv[1:])
print(f'Length: {len(argv)}')
