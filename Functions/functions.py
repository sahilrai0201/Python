#--------------Function to calculate sum of two numbers----------------------------------------->
# def calcSum(a, b):      #function definition; parameters
#     sum = a + b
#     print(sum)
#     return sum

# calcSum(223, 345)        #function calling; arguments

#----------------------Function to print Hello----------------------------------------------->
# def printHello():
#     print("Hello")

# printHello()
# printHello()
# printHello()

#----------------------Function to print average of 3 numbers----------------------------------------------->
# def avg(a, b, c):
#     sum = a + b + c
#     average = sum/3
#     print(average)
#     return average

# avg(98, 97, 95)

#------------------------------Default Parameters------------------------------------------------------->
# def calcProduct(a=2, b=2):
#     print(a * b)
#     return a * b

# calcProduct()    #if there's no argument passed then default parameters will run that is 2*2 = 4

# #OR-------->

# def calcProduct(a, b=2):
#     print(a * b)
#     return a * b

# calcProduct(1)    #if there's only 1 argument passed then default parameters will run that is 1*2 = 2


#---------------------------------------------------------------------------------------------->
#Ques1 : WAF to print the length of a list (list is passed as parameter)
# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
# heroes = ["thor", "ironman", "shaktiman", "batman"]

# def printLen(list):
#     print(len(list))

# printLen(cities)
# printLen(heroes)


#---------------------------------------------------------------------------------------------->
#Ques2 : WAF to print the element of a list in single line (list is passed as parameter)
# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
# heroes = ["thor", "ironman", "shaktiman", "batman"]

# def printList(list):
#     for item in list:
#         print(item, end=" ")

# printList(cities)


#---------------------------------------------------------------------------------------------->
#Ques3 : WAF to find the factorial of n (n is passed as parameter)
# i = 1
# n = int(input("Enter the number : "))

# def printFact(n):
#     fact = 1
#     for val in range(1, n+1):
#         fact = fact * val
#     print(fact)

# printFact(n)


#---------------------------------------------------------------------------------------------->
#Ques4 : WAF to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(100)