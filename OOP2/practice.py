#------------------------------------------------------------------------------------------------------>
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) * self.radius    

# c1 = Circle(21)  
# print(c1.area())
# print(c1.perimeter())      


#------------------------------------------------------------------------------------------------------>
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role :", self.role) 
#         print("Dept :", self.dept)
#         print("Salary :", self.salary)  

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age        
#         super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer("Rahul Gandhi", 45)
# engg1.showDetails()   


#------------------------------------------------------------------------------------------------------>
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price    

odr1 = Order("Chips", 20)
odr2 = Order("Tea", 15)

print(odr1 > odr2)