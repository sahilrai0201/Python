#------------------------------ SINGLE INHERITANCE--------------------------->
# class Car:
#     color = "black"

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")    

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())  
# print(car1.name)
# print(car1.color)

#------------------------------MULTI LEVEL INHERITANCE--------------------------->
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")    

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

#------------------------------MULTIPLE INHERITANCE--------------------------->
# class A:
#     varA = "Welcome to class A" 

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#------------------------------------Super Method------------------------------------->
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")    

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)        
# print(car1.name)


#------------------------------------Class Method------------------------------------->
# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     # self.name = name 
#     #     # Person.name = name 
#     #     self.__class__.name = "Rahul Kumar"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)

#------------------------------------Property Method------------------------------------->
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    # def calcPercenatage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


student1 = Student(98, 97, 99)
print(student1.percentage)

student1.phy = 86
# print(student1.phy)
# student1.calcPercenatage()
print(student1.percentage)