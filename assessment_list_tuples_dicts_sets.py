
print("Welcome to the company's Account and Warehouse!\n")

account = 0

### Perform necessary calculations and update the account and warehouse accordingly.
warehouse = {
    "name" : "",
    "price" : 0,
    "quantity" : 0
}

warehouse = []

####

# list = warehouse
# print(list)

# while True:
#     print("To-Do List: ")
#     for item in to_do_list:
#         # It is taking the list and .index() is taking the index number of the item and the +1 to start counting from 1 and not 0 as computers
#         print(f"{to_do_list.index(item) + 1}. {item}") 
    
#     print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
#     action = input("What would you like to do?: ").lower()

#     if action == "end":
#         break
#     elif action == "balance":
#         balance = input("Enter the ammount you want to add or substract: ")
#         to_do_list.append(balance) # this will add items to list but only in the running terminal. This as it is will not save added items to the code list
#     elif action == "remove":
#         task_id = int(input("Enter a task ID to remove: "))
#         if task_id > len(to_do_list):
#             print("item out of range")
#         else:    
#             to_do_list.pop(task_id - 1)
#     else:
#         print("\nInvalid command!\n")

# balace_list = []
# while True:
#     print("To-Do List: ")
#     for item in balace_list:
#         # It is taking the list and .index() is taking the index number of the item and the +1 to start counting from 1 and not 0 as computers
#         print(f"{balace_list.index(item) + 1}. {item}") 
    
#     print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
#     action = input("What would you like to do?: ").lower()

#     # if action == "end":
#     #     break
#     # elif action == "balance":
#     #     balance = input("Enter the ammount you want to add or substract: ")
#     #     to_do_list.append(balance) # this will add items to list but only in the running terminal. This as it is will not save added items to the code list
#     # elif action == "remove":
#     #     task_id = int(input("Enter a task ID to remove: "))
#     #     if task_id > len(to_do_list):
#     #         print("item out of range")
#     #     else:    
#     #         to_do_list.pop(task_id - 1)
#     # else:
#     #     print("\nInvalid command!\n")


while True:
    print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
    action = input("What would you like to do?: ").lower()

    if action == "end":
        break
    elif action == "balance":
        balance = int(input("Enter the ammount you want to add or substract: "))
        while True:
            if account + balance >= 1:
                account += balance # this will add the balance to account
                print(account)
                break
            elif account <= 0 and balance <= 0:
                print("Not sufficient funds! Retry another time!")
                continue
            else:
                print("Not sufficient funds! Retry another time!")
                break
    
    elif action == "purchase":
        name = input("Enter the name of product: ")
        price = int(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity required: "))
        if account > price:
            warehouse.
            warehouse["price"] = price
            warehouse["quantity"] = quantity
            account -= price
            print(warehouse)
            print(account)
        else:
            print("\nNot enough fund, Bruh!!!!")
            print(account)

    # elif action == "sale":
    #     if account 

    #     if task_id > len(to_do_list):
    #         print("item out of range")
    #     else:    
    #         to_do_list.pop(task_id - 1)
    # # else:
    #     print("\nInvalid command!\n")