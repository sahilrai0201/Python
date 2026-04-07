#-------------------------WHILE LOOP----------------------------------->
# count = 0
# while count <= 5:
#     print("Hello", count)
#     count += 1
# print(count)    

#---------------------------------->
#Ques1 : Print numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#---------------------------------->
#Ques2 : Print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1    

#--------------------------------------------->
#Ques3 : Print the multiplication table of a number n
# n = int(input("Enter the number : "))
# count = 1
# while(count <= 10):
#     print(n * count)
#     count += 1

#-------------------------------------->
#Ques4 : Print the squares from 1 to 10
# i = 1
# while(i <= 10):
#     print(i * i)
#     i += 1    

#-------------------------------------------->
#Ques5 : Search for x in the squares of 1 to 10
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter the target : "))
# i = 0
# while(i < len(nums)):
#     if(nums[i] == x):
#         print("FOUND at index", i)
#     i += 1 

#------------------BREAK & CONTINUE-------------->      
# i = 1
# while(i <= 5):
#     if(i == 4):
#         break
#     print(i)
#     i += 1
# print("END OF LOOP")


# i = 1
# while(i <= 5):
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("END OF LOOP")    


#---------------------------------------FOR LOOP-------------------------------------------->
# nums = [1, 2, 3, 4, 5]
# for val in nums:
#     print(val)


# veggies = ["potato", "tomato", "peas", "beans", "onion"]
# for val in veggies:
#     print(val)    


# tup = (1, 2 , 3, 4, 2, 8, 9)
# for num in tup:
#     print(num)


# str = "ApnaCollege"
# for char in str:
#     if(char == 'o'):
#         print("o found")
#         break
#     print(char)
# else:
#     print("END")    

#-------------------------------------->
#Ques1 : Print the squares from 1 to 10
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in nums:
#     print(val)

#-------------------------------------------->
#Ques2 : Search for x in the given tuple
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49
# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at index", idx)
#         break
#     idx += 1

#---------------------------------------RANGE FUNCTION-------------------------------------------->
# for el in range(5):
#     print(el)

# for el in range(1, 5):
#     print(el)    

# for val in range(0, 5, 2):
#     print(val)

#-------------------------------------->
#Ques1 : Print numbers from 1 to 100
# for el in range(1, 101):
#     print(el)

#-------------------------------------->
#Ques2 : Print numbers from 100 to 1
# for el in range(100, 0, -1):
#     print(el)    

#-------------------------------------->
#Ques3 : Print multiplication table of a number n
# n = int(input("Enter the number : "))
# for el in range(1, 11):
#     print(n * el)


#----------------------------------Pass statement------------------------------------------->
# for val in range(0, 11):
#     pass  #empty
# i = 11
# if i > 5:
#     pass
# print("CODE ENDS HERE..!")

#-------------------------------------->
#Ques1 : WAP to find sum of first n numbers (using while)
# n = int(input("Enter the number : "))
# i = 1
# sum = 0
# while i <= n:
#     sum = sum + i
#     i += 1
# print(sum)

#-------------------------------------->
#Ques2 : WAP to find factorial of first n numbers (using for)
n = int(input("Enter the number : "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i += 1
print(fact)