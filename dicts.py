#creating a dict

my_dict = {
    "name" : "John", 
    "age" : 30, 
    "city" : "New York"
}

# Accessing values
print(my_dict["name"])

# adding key value pair
my_dict["pet"] = False

print(my_dict)

# Changing the value
my_dict["age"] = 35
print(my_dict)

# Removing key value pairs
del my_dict["age"]
my_dict.pop("city")


print(my_dict)

# Print keys from dict
print(my_dict.keys())

# Print all values from dict
print(my_dict.values())

#
print(my_dict.items())