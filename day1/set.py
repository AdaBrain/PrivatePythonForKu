# SET = Mathematical Object
# {1, 2, 3, {9, 9, 9}}
# {1, 1, 1, 1} = {1}
# List(1, 1) != Set{1, 1} = {1}

data = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5]
print( set(data) )
print( len(set(data)) )

A = {1, 2, 3}
B = {2, 3, 4}

# Add
A.add(0)
print(A)

# Set Operations
# Union
C = A.union(B)
print(C)

# Intersaction
C = A.intersection(B)
print(C)

# Different
C = A.difference(B)
print(C)

G = {}
G["A"] = 3
print(G)
G = {1, 2}
print(G)