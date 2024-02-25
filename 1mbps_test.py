print("Welcome to the company's Account and Warehouse!\n")

account = 1000

warehouse_list = []

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
            warehouse_list.append({"name" : name, "price" : price, "quantity" : quantity})
            account -= price * quantity
            print(f"Purchase has been successful! {quantity} unit(s) of {name} bought for a total of {price * quantity}.")
            print(warehouse_list)
            print(account)
        else:
            print("\nNot enough fund, Bruh!!!!")
            print(account)

    elif action == "sale":
        name = input("Enter the name of product: ")
        price = int(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity required: "))
        for w in warehouse_list:
            if w["name"] == name and w["price"] == price and w["quantity"] >= quantity:
                w["quantity"] -= quantity
                account += price * quantity
                print(f"Sale has been successful! {quantity} unit(s) of {name} sold for a total of {price * quantity}.")
                print("Updated warehouse:", warehouse_list)
                print("Updated account balance:", account)
                break
        else:
            print("Product not found or insufficient quantity in the warehouse, Bruh!!!")

    elif action == "account":
        print(f"\nThe total ammount availble is € {account}!")

    elif action == "list":
        print(f"\nThe warehouse availability is the following: \n{warehouse_list}")

    elif action == "warehouse":
        name = input("Enter the name of product: ")
        for find in warehouse_list:
            if find["name"] == name:
                print(f"\nHere is the result:\n\nName: {find["name"]}\nPrice: {find["price"]}\nQuantity: {find["quantity"]}")
        else:
            print("\nProduct is not in the system, Bruh!!!")

    elif action == "review":
        from_indice = int(input("Enter FROM when you want to check historycal data, start from 1 as been the oldest in time: "))
        to_indice = int(input("Enter the TO when you wan to check data, higher number means lastest: "))
   
        if from_indice >= 1 and to_indice <= len(warehouse_list):
            print(warehouse_list[from_indice:to_indice])
            
        else:
            print("Not in range, Bruh!!!")
        
    else:
        print("\nInvalid command!\n")
        
        
        
        # print(len(warehouse_list))


    # elif action == "sale":
    #     if account 

    #     if task_id > len(to_do_list):
    #         print("item out of range")
    #     else:    
    #         to_do_list.pop(task_id - 1)

    # # else:
    #     print("\nInvalid command!\n")


    # elif action == "sale":
    #     name = input("Enter the name of product: ")
    #     price = int(input("Enter the price of the product: "))
    #     quantity = int(input("Enter the quantity required: "))
    #     for w in warehouse:
    #         if w["name"] == name and w["price"] == price and w["quantity"] >= quantity:
    #             w["quantity"] -= quantity
    #             account += price * quantity
    #             print(f"Sale successful! {quantity} units of {name} sold for a total of {price * quantity}.")
    #             print("Updated warehouse:", warehouse)
    #             print("Updated account balance:", account)
    #             break
    #     else:
    #         print("Product not found or insufficient quantity in the warehouse!")




        # for d in warehouse:
        #     if d["name"] == name and d["price"] == price and d["quantity"] == quantity:
        #         warehouse.remove(d)
        #         print(warehouse)
        #         if quantity <= 0:
        #             warehouse.remove(d)
        #             account -= price
        #             print(warehouse)
        #             print(account)
        #         else:
        #             print("I did not understand!!!!")
        #             print(warehouse)
        #             print(account)
        #             break

        # match_warehouse = [w for w in warehouse if w['quantity'] == quantity]

        # if not match_warehouse or quantity <= 0:
        #     print("There is no available quantity!")

        # else:
        #     warehouse = [w for w in warehouse if w['quantity'] != quantity]
        #     account += price

        #     print(warehouse)
        #     print(account)



        # if name == warehouse[1]:
        #     # warehouse -= name
        #     print(name)

        # elif price == warehouse:
        #     warehouse -= price
        #     account -= price

        # elif quantity == warehouse:
        #     warehouse -= quantity

        # else:
        #     print("\nThere is nothing in here, Bruh!!!")
        #     print(account)

        # print(warehouse)
        # print(account)


    # elif action == "sale":
    #     if account 

    #     if task_id > len(to_do_list):
    #         print("item out of range")
    #     else:    
    #         to_do_list.pop(task_id - 1)
    # # else:
    #     print("\nInvalid command!\n")



# print("Welcome to the company's Account and Warehouse!\n")

# account = 0

# ### Perform necessary calculations and update the account and warehouse accordingly.
# warehouse = {
#     "name" : "",
#     "price" : 0,
#     "quantity" : 0
# }

# warehouse = []

# ####

# # list = warehouse
# # print(list)

# # while True:
# #     print("To-Do List: ")
# #     for item in to_do_list:
# #         # It is taking the list and .index() is taking the index number of the item and the +1 to start counting from 1 and not 0 as computers
# #         print(f"{to_do_list.index(item) + 1}. {item}") 
    
# #     print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
# #     action = input("What would you like to do?: ").lower()

# #     if action == "end":
# #         break
# #     elif action == "balance":
# #         balance = input("Enter the ammount you want to add or substract: ")
# #         to_do_list.append(balance) # this will add items to list but only in the running terminal. This as it is will not save added items to the code list
# #     elif action == "remove":
# #         task_id = int(input("Enter a task ID to remove: "))
# #         if task_id > len(to_do_list):
# #             print("item out of range")
# #         else:    
# #             to_do_list.pop(task_id - 1)
# #     else:
# #         print("\nInvalid command!\n")

# # balace_list = []
# # while True:
# #     print("To-Do List: ")
# #     for item in balace_list:
# #         # It is taking the list and .index() is taking the index number of the item and the +1 to start counting from 1 and not 0 as computers
# #         print(f"{balace_list.index(item) + 1}. {item}") 
    
# #     print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
# #     action = input("What would you like to do?: ").lower()

# #     # if action == "end":
# #     #     break
# #     # elif action == "balance":
# #     #     balance = input("Enter the ammount you want to add or substract: ")
# #     #     to_do_list.append(balance) # this will add items to list but only in the running terminal. This as it is will not save added items to the code list
# #     # elif action == "remove":
# #     #     task_id = int(input("Enter a task ID to remove: "))
# #     #     if task_id > len(to_do_list):
# #     #         print("item out of range")
# #     #     else:    
# #     #         to_do_list.pop(task_id - 1)
# #     # else:
# #     #     print("\nInvalid command!\n")


# while True:
#     print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
#     action = input("What would you like to do?: ").lower()

#     if action == "end":
#         break
#     elif action == "balance":
#         balance = int(input("Enter the ammount you want to add or substract: "))
#         while True:
#             if account + balance >= 1:
#                 account += balance # this will add the balance to account
#                 print(account)
#                 break
#             elif account <= 0 and balance <= 0:
#                 print("Not sufficient funds! Retry another time!")
#                 continue
#             else:
#                 print("Not sufficient funds! Retry another time!")
#                 break
    
#     elif action == "purchase":
#         name = input("Enter the name of product: ")
#         price = int(input("Enter the price of the product: "))
#         quantity = int(input("Enter the quantity required: "))
#         if account > price:
#             warehouse.
#             warehouse["price"] = price
#             warehouse["quantity"] = quantity
#             account -= price
#             print(warehouse)
#             print(account)
#         else:
#             print("\nNot enough fund, Bruh!!!!")
#             print(account)

#     # elif action == "sale":
#     #     if account 

#     #     if task_id > len(to_do_list):
#     #         print("item out of range")
#     #     else:    
#     #         to_do_list.pop(task_id - 1)
#     # # else:
#     #     print("\nInvalid command!\n")