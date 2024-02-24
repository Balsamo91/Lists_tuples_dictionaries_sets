# to_do_list = ["Cook dinner", "Do homework", "Go to the grocery store"]

# while True:
#     print("To-Do List: ")
#     for item in to_do_list:
#         print(f"- {item}")
    
#     print("\nOptions: add, remove, exit")
#     action = input("Command: ").lower()

#     if action == "exit":
#         break
#     elif action == "add":
#         pass #just to remove the error in the else. and don't iunterrupt runnig code
#     elif action == "remove":
#         pass
#     else:
#         print("\nInvalid command!\n")



#######################
        
to_do_list = ["Cook dinner", "Do homework", "Go to the grocery store"]

while True:
    print("To-Do List: ")
    for item in to_do_list:
        # It is taking the list and .index() is taking the index number of the item and the +1 to start counting from 1 and not 0 as computers
        print(f"{to_do_list.index(item) + 1}. {item}") 
    
    print("\nOptions: add, remove, exit")
    action = input("Command: ").lower()

    if action == "exit":
        break
    elif action == "add":
        task = input("Enter a task to add: ")
        to_do_list.append(task) # this will add items to list but only in the running terminal. This as it is will not save added items to the code list
    elif action == "remove":
        task_id = int(input("Enter a task ID to remove: "))
        if task_id > len(to_do_list):
            print("item out of range")
        else:    
            to_do_list.pop(task_id - 1)
    else:
        print("\nInvalid command!\n")