# ------------------------FIRST PROGRAM------------------------------
print("Hello World")
print("My name is Sahil Rai.", "My age is 22.")

# print(23)
# print(35 + 23)

# ------------------------VARIABLES---------------------------------
name = "Sahil Rai"
age = 22
price = 25.99
age2 = age

# print("My name is", name)
# print("My age is", age2)

# print(type(name))
# print(type(age))
# print(type(price))

# ------------------------DATA TYPES-------------------------------
age = 33
old = False
a = None
# print(type(old))
# print(type(a))

# ------------------------Print Sum-----------------------------------
a = 390
b = 588
sum = a + b
# print(sum)

# ------------------------Arithmetic Operators-------------------------------
a = 5
b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)   #output is always a floating number
# print(a % b)   #remainder
# print(a ** b)   #a^b

# ------------------------Relational Operators-------------------------------
a = 50
b = 20

#all these statements return true or false
# print(a == b)    
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# ------------------------Assignment Operators-------------------------------
# num = 10
# num += 10    #num = num + 10
# print("num :", num)

#num = 10
# num -= 10     #num = num - 10
# print("num :", num)

# num = 10
# num *= 10   #num = num * 10
# print("num :", num) 

# num = 10
# num **= 3
# print(num)

# ------------------------Logical Operators-------------------------------
a = 69
b = 53
# print(not(a > b))
# print(not True)

val1 = True
val2 = False
# print("AND operator :", val1 and val2)
# print("OR operator :", (a == b) or (a > b))

# ------------------------Type conversion-------------------------------
a = 2      #int
b = 4.25    #float
#pyhton converts int to float, reduces wastage of data that is Implicit Conversion.
sum = a + b     #2.0 + 4.25 = 6.25
# print(sum)

#Explicit Conversion which is forcefully done by user.
a = float("2")
b = 4.25
# print(type(a))
# print(a + b)

a = 3.14
a = str(a)
# print(type(a))

# ------------------------Input in Python-------------------------------
# name = input("Enter your name : ")
# print("Welcome", name)

# val = input("Enter data : ")
#whether you enter float, int, char, str, etc it will always 'str' as its type
# print(type(val), val)         

# val = int(input("Enter the data : "))
# print(type(val), val)

# val = float(input("Enter the data : "))
# print(type(val), val)

name = input("Enter name : ")
age = int(input("Enter age : "))
marks = float(input("Enter marks : "))
print("Welcome", name)
print("Age =", age)
print("Marks =", marks)
