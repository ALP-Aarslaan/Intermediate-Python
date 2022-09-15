# tuples are ordered, immutable, allows duplicate elements
myTuple = ("jonayed", 23, "debidwar")
print(myTuple)

# if we declare a tuple with one element inside parethesis it will be not recognized as tuple
a = (23)
print(type(a))
a = ("jonayed")
print(type(a))

# if we give a comma after this one element then it will be recognized as Tuple:
a = ("jonayed",)
print(type(a))
# if we don't give any parenthesis it will also recognize it as tuple:
a = "Jonayed", 23, "debidwar"
print(a)
print(type(a))

# we can also create tuple from Tuple class:
t1 = tuple(["jonayed", "sarkar", "19101019"])
print(t1)
# here inside tuple class we need to provide iterable object like list to
# insert elements in tuple


# accessing elements from tuples:
print(t1[0])
print(t1[1])
print(t1[2])
# print(t1[3]) it will give index out of bound error as there is no index 3 inside this tuple
# we can also use negative indexing:
print(t1[-2])
print(t1[-1])

# tuple is immutable so we can not assign elemnts in it:
# t1[0] = "Tommy" this line will give error as typle is immutable
print(t1)

# tuple elements printing using for loop:
for elements in t1:
    print(elements)

# to check if one element is inside the tuple:
if "jonayed" in t1:
    print("found")
else:
    print("not found")

if "boston" in t1:
    print("found")
else:
    print("not found")

# length of a tuple:

t2 = ("a", "b", "c", "d", "e", "f")
print("length of this tuple : ", len(t2))

# to count an element how many times it appeared :

t2 = ("a", "p", "p", "l", "e")
print("p appeared :", t2.count("p"), " times")

# to find the index in which an element 1st occurred:
print(t2.index("e"))

# convert tuple to list and vice versa:

my_list = list(t2)  # tuple to list
print(my_list)

t2 = tuple(my_list)  # list to tuple
print(t2)

# tuple slicing:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = numbers[2:6]  # it will give from index 2 to 5 except the 6
print(b)
b = numbers[:]
print(b)
b = numbers[:7]
print(b)
b = numbers[2:]
print(b)
b = numbers[-1]
print(b)

# stepping element:
b = numbers[::1]
print(b)
b = numbers[::2]
print(b)
b = numbers[::3]
print(b)

# to reverse a tuple we use negative step:
b = numbers[::-1]
print(b)

# unpacking a tuple and access each element alongside with a variable:
address = ("Mohammad", 23, "19101019")
name, age, Id = address  # number of elements must match with number of variables
print(name)
print(age)
print(Id)

num = (1, 2, 3, 4, 5, 6)
i1, *i2, i3 = num
print(i1)
print(i2)
print(i3)

# comparing list and tuple:
import sys

lists = ["jonayed", 23, "19101019", 3.73]  # lists take more memory than tuple so tuples are efficient

tuples = ("jonayed", 23, "19101019", 3.73)
print(sys.getsizeof(lists), "bytes")
print(sys.getsizeof(tuples), "bytes")

import timeit

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(timeit.timeit(stmt="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", number=1000000), " time taken by list")
# this prints how much time taken
print(timeit.timeit(stmt="(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)", number=1000000), " time taken by tuple")
