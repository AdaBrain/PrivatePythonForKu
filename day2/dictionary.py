# Dictionary = MapData
# key : value

# Create
shop = dict() # Empty Dictionary
shop = {
    "name": "AdaBrain Shop",
    "owner": "Ada",
    "apple": 10.5,
    "orange": 9.99,
    "water melon": 12.05,
    "stocks": [1, 1.2, 1.5, 1.0, 0.99, 5.98],
    "employee": {"A", "B", "C"},
    "electronics": {
        "iphone": 10.99,
        "nintendo_switch": 20.00
    }
}

# Read, O(1)
print(shop["name"])

# Update
shop["name"] = "Adabrain Shop branch 2022"
print(shop["name"])

shop["marvel_hero"] = "Spider-Man"
print(shop["marvel_hero"])

# Delete
del shop["marvel_hero"]
print(shop)

# Methods
for (key, val) in shop.items():
    print(key, val)

# Problem
'''
Get the key of a minimum value from the following dictionary
'''
# input:
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}
# output: Math
result = ["min", 1000]
for (k, v) in sample_dict.items():
    if v < result[1]:
        result[0] = k
        result[1] = v

print(result[0])
print(min(sample_dict, key=sample_dict.get))


# problem 2
'''Write a Python program to change Brad’s salary to 8500 in the following dictionary.'''

# Input:
sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] = 8500
print(sample_dict)

### Add each employee salary: 500 ###
for (k, v) in sample_dict.items():
    v["salary"] += 500
    v["bonus"] = 9000

print(sample_dict)


### Problem rename key's dict
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

def change_dict_key(target, old_key, new_key):
    if not target.get(old_key): 
        return

    target[new_key] = target[old_key]
    del target[old_key]

change_dict_key(sample_dict, "city", "location")
change_dict_key(sample_dict, "age", "years")
print(sample_dict)


## Problem
'''Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.'''

# input 
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to extract
keys = ["name", "salary"]

# output: {'name': 'Kelly', 'salary': 8000}

def extract_from_keys(target, keys):
    result = dict()
    for (k, v) in target.items():
        if k in keys:
            result[k] = v
    
    return result

d1 = extract_from_keys(sample_dict, ["name"])
d2 = extract_from_keys(sample_dict, ["name", "salary"])
print(d1)
print(d2)

if sample_dict.get("name"):
    print("adabrain:", sample_dict.get("name1"))
else:
    print("Key not found")