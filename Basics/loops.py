#-------------------------WHILE LOOP----------------------------------->
# count = 0
# while count <= 5:
#     print("Hello", count)
#     count += 1
# print(count)    

#------------------------------------------------------------------------->
#Ques1 : Print numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#------------------------------------------------------------------------->
#Ques2 : Print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1    

#------------------------------------------------------------------------->
#Ques3 : Print the multiplication table of a number n
# n = int(input("Enter the number : "))
# count = 1
# while(count <= 10):
#     print(n * count)
#     count += 1

#------------------------------------------------------------------------->
#Ques4 : Print the squares from 1 to 10
# i = 1
# while(i <= 10):
#     print(i * i)
#     i += 1    

#------------------------------------------------------------------------->
#Ques5 : Search for x in the squares of 1 to 10
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter the target : "))
# i = 0
# while(i < len(nums)):
#     if(nums[i] == x):
#         print("FOUND at index", i)
#     i += 1 

#----------------------BREAK & CONTINUE--------------------------------------->      
# i = 1
# while(i <= 5):
#     if(i == 4):
#         break
#     print(i)
#     i += 1
# print("END OF LOOP")


i = 1
while(i <= 5):
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
print("END OF LOOP")    