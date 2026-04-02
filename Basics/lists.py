#creating list -> built-in data type----------------------->
# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))    # <class 'list'>

# print(marks[0])     #94.4
# print(marks[1])    #87.5

# print(len(marks))    #5

# student = ["karan", 95.5, 17, "Delhi"]   #valid list -> even with different data types
# print(student)
# print(student[0])   #mutable -> can access, and can change also
# student[0] = "Aujla"
# print(student)

#List slicing----------------------------------------------->
# marks = [87, 64, 33, 95, 76]
# print(marks[1:4])
# print(marks[ :4])   #same as marks[0:4]
# print(marks[1: ])   #same as marks[1:len(marks)]
# print(marks[-3:-1])

#List methods----------------------------------------------->
#all these methods are performed originally in the list unlike strings
list = [2, 1, 3]

list.append(4)     #adds one element at the end [2, 1, 3, 4]
print(list)

list.sort()     #sorts in ascending order [1, 2, 3, 4]
print(list)
 
list.sort(reverse = True)   #sorts in descending order [4, 3, 2, 1]
print(list)

list1 = [2, 5, 6, 9]
list1.reverse()         #reverses list [9, 6, 5, 2]
print(list1)

list1.insert(3, 67)   #inserts element at index ->  (index, element)
print(list1)

list2 = [2, 1, 3, 1]
list2.remove(1)        #removes the first occurrence of element
print(list2)

list3 = [2, 3, 4, 5, 9, 1]
list3.pop(3)   #removes element at index -> pop(index)
print(list3)
