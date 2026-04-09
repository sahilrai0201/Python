#--------------------------Reading a file---------------------------------------------------------->
# f = open("FileHandling/demo.txt", "r")

# data = f.read()       #output -> I am learning Python from Apna College. Furthermore my focus is on AI and ML.
# # data = f.read(5)      #output -> I am 
# # data = f.readline()      #output -> I am learning Python from Apna College.

# print(data)
# print(type(data))

# f.close()


#--------------------------Writing a file---------------------------------------------------------->
# f = open("FileHandling/demo.txt", "w")
# f.write("This is a new line")         #overwrites the entire demo.txt file
# f.close()

# f = open("FileHandling/demo.txt", "a")
# f.write("\nThis is a new line")         #adds this line to demo.txt file
# f.close() 

#there's no sample.txt file existing initially but when we open sample.txt file 
#with "w" or "a" mode. It will automatically creates a new file with name of it.
# f = open("FileHandling/sample.txt", "w")    
# f.close()

#--------------------------with Syntax---------------------------------------------------------->
# with open("FileHandling/demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("FileHandling/demo.txt", "w") as f:
#     f.write("New data")


#--------------------------Deleting a file---------------------------------------------------------->
# import os
# os.remove("FileHandling/sample.txt")


#---------------------------Question 1----------------------------------------->.
# with open("FileHandling/practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")


#---------------------------Question 2----------------------------------------->.
# with open("FileHandling/practice.txt", "r") as f:
#     data = f.read()

# newData = data.replace("Java", "Python")    
# print(newData)

# with open("practice.txt", "w") as f:
#     f.write(newData)


#---------------------------Question 3----------------------------------------->
def checkForWord():
    word = "pyq"
    with open("FileHandling/practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not found")

def checkForLine():
    word = "pyq"
    data = True
    lineNum = 1
    with open("FileHandling/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineNum)
                return
            lineNum += 1

    return -1            

print(checkForLine())