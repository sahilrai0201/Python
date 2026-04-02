#----------------------------------------------------------------------------------
# tup = (2, 1, 3, 1)
# print(type(tup))      # <class 'tuple'>

# print(tup[0])
# print(tup[1])

# tup[0] = 5     #'tuple' object does not support item assignment


#-----------------------------------------------------------------------------------
# #tuple with no elements
# tup1 = ()
# print(tup1)
# print(type(tup1))     #valid tuple

# #tuple with single element
# tup2 = (1, )     #without comma python will treat it as a integer value but not tuple
# print(tup2)

# #tuple with multiple elements
# tup3 = (1, 2, 3, 4,)     #comma at last totally optional
# print(tup3)


#--------------------tuple slicing---------------------------------------------------
# tup = (1, 2, 3, 4)
# print(tup[1:3])


#--------------------tuple methods--------------------------------------------
# tup = (1, 2, 3, 4, 2, 2)
# print(tup.index(2))   #returns index of first occurrence
# print(tup.count(2))    #returns total occurrence


#---------------------------------------------------------->
#Ques1 : WAP to count the number of students with the "A" grade in the following tuple 
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))                #prints 3
