#creating list -> built-in data type------------------->
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))    # <class 'list'>

print(marks[0])     #94.4
print(marks[1])    #87.5

print(len(marks))    #5

student = ["karan", 95.5, 17, "Delhi"]   #valid list -> even with different data types
print(student)
print(student[0])   #mutable -> can access, and can change also
student[0] = "Aujla"
print(student)

#List slicing------------------------------------>
