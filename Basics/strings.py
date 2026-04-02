#----------------------------------------STRINGS------------------------------------------------------------
# str1 = "This is a string."
# str2 = 'ApnaCollege'
# str3 = """Example string"""

# str4 = "This is a string.\n We are creating it in Python."
# print(str4)

#concatenation------------>
# str1 = "Apna"
# str2 = "College"
# print(str1 + " " + str2)

#len() is used to find the length of a string---------->
# print(len(str1))
# print(len(str2))

#indexing-------------------------->
# str = "Apna College"
# ch = str[0]
# ch1 = str[4]
#str[4] = "@"   #TypeError: 'str' object does not support item assignment
# print(ch)
# print(ch1)

#slicing--------------------------------->
# str = "Apna College"
# print(str[1 : 4])       #ending index is not included
# print(str[ : 4])        #same as str[0 : 4]
# print(str[0 : ])          #same as str[0 : len(str)]

# str = "Apple"
# print(str[-5 : -2])    #negative indexing

#string function--------------------------------------->
# str = "i am from studying python from ApnaCollege"

# print(str.endswith("ege"))      #True/False

# print(str.capitalize())          #first char is capitalized in output

# print(str)                 #capitalize() do not change original str

# str = str.capitalize()     #changes are now done in original string
# print(str)                  

# print(str.replace("python", "PYTHON"))

# print(str.find("y"))     #returns 1st index of 1st occurrence of that char/word
# print(str.find("from"))
# print(str.find("Q"))       #prints -1 for non-existing chars

# print(str.count("from"))

#Ques1 : WAP to input user's first name & print its length----------->
# name = input("Enter your first name : ")
# print("length of your name is", len(name))

#Ques2 : WAP to find the occurrence of $ in a string
# str = "$Sahil$$"
# print(str.count("$"))

#----------------------------------------CONDITIONAL STATEMENT------------------------------------------------
# age = 21
# if(age >= 18):
#     print("Can vote") 
#     print("Can drive")


# light = "grey"
# if(light == "red"):
#     print("Stop") 
# elif(light == "green"):
#     print("Go")    
# elif(light == "Yellow"):
#     print("Be Ready")
# else:
#     print("Light is broken") 


# marks = int(input("Enter marks : "))
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"    
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of student ->", grade)
            

#nesting
# age = int(input("Enter age : "))
# if(age >= 18):
#     if(age >= 80):
#         print("Cannot drive")
#     else:
#         print("Can drive")
# else:
#     print("cannot drive")          


#Ques1 :  WAP to check if a number entered by user is odd or even
# num = int(input("Enter the number : "))
# if(num % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")    


#Ques2 :  WAP to find the greatest of 3 numbers entered by the user
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))
# if(a >= b and a >= c):
#     print("first is greatest", a)
# elif(b >= c):
#     print("second is greatest", b)
# else:
#     print("third is greatest", c)      


#Ques3 : WAP to check if a number is multiple of 7 or not
# x = int(input("Enter the number : "))
# if(x % 7 == 0):
#     print(x, "is a multiple of 7")
# else:
#     print(x, "is not a multiple of 7")    