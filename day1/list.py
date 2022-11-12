# List != Array
# (x, y) != (y, x)
# (1, 1, 1.123, 'Ada', null, obj)
# List := dynamic data structure

# Empty list
n = []

n.extend([1, 2, 3])
print(n)

n.append([1, 2, 3])
print(n)

# Length, len()
print(len(n))

# List Comprehensive = Fliter
# Pythonista = Python Programmer, Pythonic code = Python Code Style
n2 = [i for i in n if type(i) is int]
print("n2:", n2)
n3 = [int(j) for j in "123"]
print(n3)

# Remove element
# CRUD = Create, Read, Update, Delete
n3.remove(2)
print(n3)
n3.pop(0)
print(n3)

del n3[0]
print(n3)