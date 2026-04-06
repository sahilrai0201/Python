#creating dictionary ------------->
info = {
    "key" : "value",        # key-value pair (string → string)
    "name" : "Sahil",       # storing name
    "cgpa" : 7.6,           # storing float value
    "marks" : [98, 97, 95], # list inside dictionary
}

print(info)     # print entire dictionary

print(type(info))   # check data type (dict)

print(info["cgpa"])    # accessing value using key

info["name"] = "Saahil" # overwrite existing value
info["surname"] = "Rai"  # add new key-value pair

print(info)  # print updated dictionary

null_dict = {}      # creating an empty dictionary
null_dict["name"] = "ApnaCollege"  # adding key-value to empty dict
print(null_dict)  # print new dictionary

#nested dictionaries ---------------->
Student = {
    "name" : "Sahil",   # outer key
    "score" : {         # nested dictionary
        "Chem" : 98,    # subject-wise marks
        "Phy" : 97,
        "Math" : 95
    }
}
print(Student)  # print full nested dictionary
print(Student["score"])  # access inner dictionary
print(Student["score"]["Chem"])  # access nested value

#dict methods-------------->
print(Student.keys())  # returns all keys
print(list(Student.keys()))  # convert keys to list
print(len(list(Student.keys())))  # count number of keys

print(Student.values())  # returns all values
print(list(Student.values()))  # convert values to list

print(Student.items())  # returns key-value pairs (tuples)
print(list(Student.items()))  # convert to list of tuples

pairs = list(Student.items())  # store items in a list
print(pairs[0])  # print first key-value pair

# print(Student["name2"])   # would give KeyError (key doesn't exist)
print(Student.get("name2"))   # safe access → returns None if key not found

Student.update({"city" : "delhi"})  # add new key-value pair
print(Student)  # print updated dictionary

new_dict = {"city" : "Delhi", "age" : 16}  # another dictionary
Student.update(new_dict)  # update multiple values (overwrites existing keys)
print(Student)  # final dictionary