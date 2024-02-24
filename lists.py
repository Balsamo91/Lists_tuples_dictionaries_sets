# Creating a list
my_list = [1, 2, 3, "Python", 5.5]
print(my_list)

# You can access items within a list based on the index. Index is staring from 0
print(my_list[3])

# Checking the length of the list
print(len(my_list))

# Printing the last item in the list
print(my_list[-1])

# Adding elements. append() --> add somwthing at the END of the list
my_list.append("New Item")
print(my_list)

# insert items inside list. first specify the position the after comma add something
my_list.insert(3, 4)
print(my_list)
my_list.insert(-2, "f")
print(my_list)

# Removing items based on the value, known items
my_list.remove("Python")
print(my_list)

# Removing an item based on a index. it can also remove the whole variable using del my_list[]
del my_list[0]
print(my_list)

# Removing an item based on a index using .pop function
my_list.pop(2)
print(my_list)