# lists are mutable,ordered and also allows duplicates
list1 = ["apple", "banana", "mango", "jack fruit"]
print(list1)

# empty lists:

list2 = list()
print(list2)

"""
list can contain integer,boolean,string all kinds of data all along
"""
list3 = [1, 2, True, "Apple", "Apple"]
print(list3)

# printing list elements by its index
item = list1[0]
print(item)
item = list1[1]
print(item)
item = list1[2]
print(item)
item = list1[3]
print(item)
# if we give index that not present in that list it will give an error
"""
we can use mines index number to print or access list item from the last index
"""
print(list1[-1])  # gives the very last elements
print(list1[-2])  # gives second last elements
print(list1[-3])  # gives third last elements
print("\n\n")

# iterate through a list:
for items in list1:
    print(items)

# check  if any item is inside your list:
if "Apple" in list1:
    print("Found in list")
else:
    print("not found inside the list")

if "apple" in list1:
    print("Found in list")
else:
    print("not found inside the list")

# length method to find how many items in my list:
print(len(list1))

# add at the end of list:
list1.append("grapes")
print(list1)

# to insert at a specific index:

list1.insert(2, "blueberry")
print(list1)

# to remove an item from the last of the list:
item = list1.pop()
print(item, " is removed")
print(list1)

#  to remove a specific item :
list1.remove("jack fruit")
print(list1)
# list1.remove("Jack fruit")
print(list1)  # if item not present it will give error

# to clear whole list:
print(list3, " = list 3")
list3.clear()
print(list3)

# to reverse the list elements:
print(list1)
list1.reverse()
print(list1)

# to sort the list:
print(list1)
list1.sort()
print(list1)  # sorted by character

numbers = [1, 9, 5, 7, 3, 4, -1, -7]
numbers.sort()  # it changes the list order
print(numbers)
print(numbers)

# tricks with list:
new_list = [0] * 5
print(new_list)
myList = [1, 2, 3, 4, 5]

list5 = new_list + myList
print(list5)

# slicing:
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[1:5])  # it prints from index 1 to 4
print(num[:6])  # if we don't specify the start index it starts from 0 index
print(num[3:])  # if we don't specify the end index it ends at its last index
# slicing step index:

"""
to print every element after 1 index or 2 or n number of index
"""
print(num[::3])
print(num[::2])
print(num[::1])
# reversing using step index:
print(num[::-1])

# copy one list to another:
l1 = ["apple", "banana", "water melon"]
# l2 = l1 # its not the proper way of coping
l2 = l1
l2.append("grapes")
print(l1)
print(l2)
l3 = ["apple", "banana", "water melon"]
l4 = l3.copy()  # correct way to copy
l4.append("grapes")
print(l3)
print(l4)

l2 = list(l1)

l2.append("grapes")
print(l2)
print(l1)

l2 = l1[:]

l2.append("grapes")
print(l2)
print(l1)

# list comprehension:
li1 = [1, 2, 3, 4, 5, 6]
b = [i ** 2 for i in li1]

print(li1)
print(b)

l1 = [1, 2, 3]

l2 = [4, 5, 6]
print(l1 + l2)

newlist = []
for i in l1:
    if i % 2 == 0:
        newlist.append(i)
    else:
        newlist.append(0)
newList = [i if i % 2 == 0 else 0 for i in l1]
print(newlist)
