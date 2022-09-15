"""
dictionaries follows : unordered, mutable and key_value pairs
"""
info = {"name": "Jonayed", "age": 23, "city": "Cumilla"}
print(info)

# we can use dict class to declare a dictionary:
info1 = dict(name="Jonayed", age=23, city="Cumilla")
print(info1)

# to access values inside a dictionary we need to give the key:
value = info1["name"]
print(value)

# if a key is not inside this dictionary and we call it to find its value:
# value = info1["data"]
# print(value) this will give key error

# how to add a new key value pair inside a dictionary:
info["email"] = "19101019@uap-bd.edu"
print(info)

# if we use same key and different value in a dictionary:
info["email"] = "19101020@uap-bd.edu"  # existing value gets overwritten
print(info)

# how to remove a value from dictionary:
del info["email"]
print(info)  # its removed email address

info.pop("name")  # it removed name
print(info)

info.popitem()  # it will remove last value and key from the dictionary
print(info)

# to check if a value is inside the dictionary:
if "name" in info:
    print(info["name"], " available")
else:
    print("not available")

try:
    print(info1["name"])
except:
    print("value not found")

try:
    print(info1["last_name"])
except:
    print("value not found")

# loop through a dictionary:
dictionary = {"name": "jonayed", "age": 23, "reg": "19101019"}
for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

# to print both key and values:
for key, value in dictionary.items():
    print(key, value)

# how to copy a dictionary into another dictionary:
# dictionary1 = dictionary
# print(dictionary1)
# dictionary1.clear()
# print(dictionary , dictionary1)
"""
as we can see if we do something with the new dictionary it affects the old one 
so this is not the right way of copying a dictionary
"""
# proper way to copy:
dictionary1 = dictionary.copy()
dictionary1["email"] = "19101019@uap-bd.edu"
print(dictionary1)
print(dictionary)

# merging two dictionaries as well as updating values:
dictionary.update(dictionary1)
print(dictionary)

"""
we can use any immutable type data as key in a dictionary
we can not use list
"""
# we can use tuple as key of a dictionary:
tuples = (1, 3)
my_dict = {tuples: tuples[0] + tuples[1]}
print(my_dict)

a ={}
print(type(a))
