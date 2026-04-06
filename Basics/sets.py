collection = {1, 2, 3, 4}   # creating a set (unique elements only)
print(collection)           # print set elements
print(type(collection))     # check type (set)

collection1 = {1, 2, 2, 2, "hello", "world", "world"}  # duplicates will be removed automatically
print(collection1)          # prints only unique elements
print(len(collection1))     # length = number of unique elements

collection2 = {}   # this creates an empty dictionary, NOT a set
print(type(collection2))    # type will be dict

collection3 = set()   # correct way to create an empty set
print(type(collection3))    # type will be set

#set methods -------------->
collection4 = set()   # creating an empty set

collection4.add("ApnaCollege")  # adding string element
collection4.add(1)              # adding integer
collection4.add(2)
collection4.add(2)              # duplicate, will not be added
collection4.add(3)
collection4.add(4)
collection4.add((1, 2, 3))      # adding tuple (allowed, as it's immutable)
print(collection4)              # print set

collection4.remove(1)   # removes element '1'
print(collection4)

collection4.pop()       # removes a random element (sets are unordered)
print(collection4)

collection4.clear()     # removes all elements → empty set
print(collection4)



set1 = {1, 2, 3}        # first set
set2 = {2, 3, 4}        # second set
print(set1.union(set2))    # union → all unique elements from both sets
print(set1. intersection(set2))    # intersection → common elements