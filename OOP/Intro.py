#------------------------------------------------------->
# class Student:
#     name = "Karan Kapoor"   # class variable (common for all objects)

# s1 = Student()              # creating first object
# print(s1.name)              # accessing class variable using object

# s2 = Student()              # creating second object
# print(s2.name)              # both objects share same class variable

#------------------------------------------------------->
# class Car:
#     color = "blue"          # class variable
#     brand = "mercedes"      # class variable

# car1 = Car()                # creating object
# print(car1.color)           # accessing color
# print(car1.brand)           # accessing brand    

#----------------------------------Constructor----------------------------------------->
# class Student:
#     college_name = "ABC College"
#     name = "Anonymous"

#     # default constructor
#     def __init__(self):
#         pass
#         # NOTE: This constructor does nothing and will be OVERRIDDEN
#         # by the parameterized constructor defined below

#     # constructor ---> automatically called when object is created
#     # parameterized constructor
#     def __init__(self, name, marks):
#         self.name = name   # instance variable (unique for each object)
#         self.marks = marks # instance variable to store marks
        
#         # values passed during object creation are assigned to object attributes
#         print("Adding new student to database...")  # message during object creation


# s1 = Student("karan", 97)   # object creation: "karan" and 97 passed to constructor
# # initializes s1.name = "karan", s1.marks = 97
# print(s1.name, s1.marks)    # prints the values stored in the object (name and marks)


# s2 = Student("arjun", 95)   # another object with different data
# # initializes s2.name = "arjun", s2.marks = 95
# print(s2.name, s2.marks)    # prints values of second object 

# print(Student.college_name)
# print(s1.name)     #precedence of obj attr > class attr

#----------------------------------Methods----------------------------------------->
# class Student:
#     college_name = "ABC College"
#     name = "Anonymous"

#     # default constructor
#     def __init__(self):
#         pass

#     # parameterized constructor
#     def __init__(self, name, marks):
#         self.name = name   
#         self.marks = marks 

#         # print("Adding new student to database...") 

#     def welcome(self):
#         print("Welcome student,", self.name)    

#     def getMarks(self):
#         return self.marks


# s1 = Student("karan", 97)
# # print(s1.name, s1.marks)

# s2 = Student("arjun", 95)
# # print(s2.name, s2.marks)

# print(s1.getMarks())

#Ques 1 : --------------------------------------------------------------------------->
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is :", sum/3)

# s1 = Student("tony stark", [99, 98, 97])    
# s1.get_avg()         

# s1.name = "ironman"
# s1.get_avg()


#-----------------------Static methods-------------------------------------->
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod      #decorator    
    def hello():
        print("hello")    

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is :", sum/3)

s1 = Student("tony stark", [99, 98, 97])    
s1.get_avg()         

s1.name = "ironman"
s1.get_avg()

s1.hello()