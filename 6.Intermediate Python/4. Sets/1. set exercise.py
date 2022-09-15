"""
sets are unordered, mutable, no duplicates acceptable
"""
myset = {1, 2, 3, 4, 5, 6}
print(myset)
# set doesn't allow duplicates:
set1 = {1, 2, 2, 3, 4, 5, 6, 6}
print(set1)

# set using set function:
s1 = set((1, 2, 3, 4, 5, 6))
print(s1)

s1 = set([1, 2, 5, 6, 3])
print(s1)

s2 = set("Jonayed")
print(s2)

# adding elements in set:
s2.add("jonayed")
s2.add("Sarkar")
print(s2)

# removing elements from set:
s2.remove("jonayed")
print(s2)

s2.discard("Sarkar")  # this will not give any error if it doesn't find the element
print(s2)

# clear method:
s2.clear()  # fully deletes set
print(s2)

# pop method:
print(myset.pop())

print(myset.pop())

print(myset.pop())

# iterate over set:
for element in myset:
    print(element)

if "jonayed" in myset:
    print("yes")
else:
    print("No")

# set mathematical operations:
# union
odd = {1, 3, 5, 7, 9}
even = set([2, 4, 6, 8, 10])
prime = set((2, 3, 5, 7, 11))
"""
union operation takes all the non duplicate elements from all sets 
"""
u = odd.union(even).union(prime)
print(u)

# intersection:
"""
it takes only common elements from all the sets
"""

i = odd.intersection(prime)
print(i)

i = even.intersection(prime)
print(i)

# set difference:
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}
diff = a.difference(b)
print(diff)
diff = b.difference(a)
print(diff)

diff = a.symmetric_difference(b)
print(diff)  # this method gives all the elements from both sets except the common elements

# adding two sets without duplicate elements :
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s2.update(s1)
print(s2)

# updating a set with common elements which are in both sets:
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s1.intersection_update(s2)
print(s1)

# updating a set excluding all the elements which is in another set :
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s1.difference_update(s2)
print(s1)
s2.difference_update(s1)
print(s2)

# updating a set excluding all the common elements from both sets:
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s1.symmetric_difference_update(s2)
print(s1)

# finding sub set and super set:
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))

# finding disjoint set: it means there is no commonality between two sets
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s3 = {7, 8}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# copying two sets : proper way
s1 = {1, 2, 3, 4, 5}
s2 = set(s1)
s1.add(99)
print(s1)
print(s2)

# frozen set is the immutable version of set:
a = frozenset([1,2,3,4,5,6])
print(a)