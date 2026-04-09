#----------------------------------------------------------------------------------------->
# #recursive function
# def show(n):
#     #base case
#     if(n == 0):
#         return
#     print(n)

#     #recursive call
#     show(n-1)

# #funtion call
# show(5)    

#--------------------------FACTORIAL-------------------------------------------------------------->
# def fact(n):
#     #base case
#     if n == 0 or n == 1:
#         return 1
    
#     return n * fact(n-1)
    
# num = int(input("Enter the number : "))
# if num < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     print("Factorial of the given number is :", fact(num))
     

#--------------------------SUM OF FIRST N NATURAL NUMBERS------------------------------------------>
# def calcSum(n):
#     if(n == 0):
#         return 0
#     return calcSum(n-1) + n
    
# num = int(input("Enter the number : "))
# print(calcSum(num))   


#--------------------------PRINT ALL ELEMENTS IN A LIST------------------------------------------>
# def printList(list, index):
#     if(index == len(list)):
#         return
#     print(list[index])
#     printList(list, index+1)
    
# fruits = ["mango", "guava", "grapes", "litchie", "orange"]
# printList(fruits, 2)