#-----------------------------del keyword-------------------------------------------->
# class Student:
#     def __init__(self, name):
#         self.name = name          # initializing name attribute

# s1 = Student("Sahil")             # creating object
# print(s1)                         # prints object reference (memory address)
# print(s1.name)                    # accessing attribute

# del s1                            # deletes the object
# print(s1)                         # ❌ error because s1 is deleted

#---------------------------Private attributes & methods-------------------------------------->

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no          # public attribute
#         self.__acc_pass = acc_pass    # private attribute (name mangling)

#     def reset_pass(self):
#         print(self.__acc_pass)        # accessing private attribute inside class    

# acc1 = Account("12345", "abcdef")    # creating object

# print(acc1.acc_no)                   # accessible (public)
# # print(acc1.__acc_pass)             # ❌ error (private attribute)

# print(acc1.reset_pass())             # calls method, prints password, then None

#--------------------------------------------->
class Person:
    __name = "anonymous"               # private class attribute

    def __hello(self):                 # private method
        print("hello person!")         # prints greeting

    def welcome(self):                 # public method
        self.__hello()                 # calling private method    

p1 = Person()                          # creating object

# print(p1.__hello())                  # ❌ error (private method not accessible)

print(p1.welcome())         # calls welcome() # prints "hello person!" # prints None (no return statement)