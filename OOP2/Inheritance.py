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
