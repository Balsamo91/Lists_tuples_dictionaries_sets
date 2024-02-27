import datetime
print("\nWelcome to the company's Account and Warehouse!\n")

# Setting up the global variable and empty list 
account = 1000
warehouse_list = []
operations_recorded = []


# Start of the program
while True:
    # Asking the user to chose an option based on what they want to do
    print("\nOptions: balance, sale, purchase, account, list, warehouse, review, end")
    action = input("What would you like to do?: ").lower()

    # If user type "end" the program terminates
    if action == "end":
        break
    
    # If user type "balance" the program will ask user input and if not int() the user will need to restart
    elif action == "balance":
        try:
            balance = float(input("Enter the ammount you want to add or substract: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # Starts the validation and it will prevent the account to go negative
        while True:
            if account + balance >= 0:
                account += balance # this will add the balance to account
                print(account)
                break
            elif account <= 0 and balance <= 0:
                print("\nNot sufficient funds! Retry another time!")
                break
            else:
                print("\nNot sufficient funds! Retry another time!")
                break
    # If the user type "purchase" the program will ask user inputs and if not int() the user will need to restart
    elif action == "purchase":    
        try:
            name = str(input("Enter the name of product: ")).lower()
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity required: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # If account is higher than the purchase price entered then add the variable into the warehouse_list[] as a dictionary
        if account > price:
            # If user enters the same item, this will catch it and it will add the quantity, if not it will add the dict to the list warehouse_list[] 
            item_exist = False
            for p in warehouse_list:
                if p["name"] == name:
                    p["quantity"] += quantity
                    item_exist = True
                    break
            if not item_exist:
                warehouse_list.append({"name" : name, "price" : price, "quantity" : quantity})
            account -= price * quantity # substract the purchased items from the account
            print(f"\nPurchase has been successful! {quantity} unit(s) of {name} bought for a total of {price * quantity}.")
            # print("\nWarehouse items:")
            # for item in warehouse_list:
            #     for key, value in item.items():
            #         print(f"{key}: {value}")
            #         print()
            operations_recorded.append({
            "type": "purchase",
            "name": name,
            "price": price,
            "quantity": quantity,
            "timestamp": datetime.datetime.now()})
            
            print(warehouse_list)
            print(account)
            print(operations_recorded)
        else:
            print("\nNot enough fund, Bruh!!!!")
            print(account)

    # If the user type "sale" the program will ask user inputs and if not int() the user will need to restart
    elif action == "sale":
        try:
            name = input("Enter the name of product: ").lower()
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity required: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # in the for loop checking if the warehouse_list[] there is availability of the item(s) requested.
        #If the user wants to sale less quantity then the quantity is calculated and updates the warehouse_list[]
        for s in warehouse_list:
            if s["name"] == name and (s["price"] <= price or s["price"] >= price) and s["quantity"] >= quantity:
                s["quantity"] -= quantity
                account += price * quantity
                print(f"\nSale has been successful! {quantity} unit(s) of {name} sold for a total of {price * quantity}.")
                # print("Updated warehouse:", warehouse_list)
                # print("Updated account balance:", account)
                operations_recorded.append({
                "type": "sale",
                "name": name,
                "price": price,
                "quantity": quantity,
                "timestamp": datetime.datetime.now()})
                break
        else:
            print("\nProduct not found or insufficient quantity in the warehouse, Bruh!!!")


    elif action == "account":
        print(f"\nThe total ammount availble is € {account}!")

    elif action == "list":
        print("\nThe warehouse availability is the following:\n")
        for list in warehouse_list:
            print()
            for key, value in list.items():
                print(f"- {key.capitalize()}: {value}")
        # print(f"\nThe warehouse availability is the following: \n{warehouse_list}")

    elif action == "warehouse":
        name = input("Enter the name of product: ")
        for find in warehouse_list:
            if find["name"] == name:
                # print(f"\nHere is the result:\n\nName: {find["name"]}\nPrice: {find["price"]}\nQuantity: {find["quantity"]}")
                print(f"\nHere is the result:\n\nName: {find["name"]}\nQuantity: {find["quantity"]}")
                break
            else:
                print("\nProduct is not in the system, Bruh!!!")

    # elif action == "review":
    #     try:
    #         from_index = int(input("Enter 'from' index: ")) if input("Enter 'from' index (press Enter to skip): ").strip() else None
    #         to_index = int(input("Enter 'to' index: ")) if input("Enter 'to' index (press Enter to skip): ").strip() else None

    #         # Check if indices are within the valid range
    #         if (from_index is not None and (from_index < 0 or from_index >= len(operations_recorded))) or \
    #            (to_index is not None and (to_index < 0 or to_index >= len(operations_recorded))):
    #             print("Invalid index range. Please enter valid indices.")
    #         else:
    #             # Display recorded operations within the specified range
    #             for i in range(from_index if from_index is not None else 0, to_index + 1 if to_index is not None else len(operations_recorded)):
    #                 print(operations_recorded[i])
    #     except ValueError:
    #         print("Invalid input. Please enter valid indices.")

    else:
        print("\nInvalid command!\n")
        