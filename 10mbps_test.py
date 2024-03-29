print("\nWelcome to the company's Account and Warehouse!\n")

# Setting up the global variable and empty list 
account = float(1000)
warehouse_list = {}

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
            balance = int(input("Enter the ammount you want to add or substract: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # Starts the validation and it will prevent the account to go negative
        while True:
            if account + balance >= 1:
                account += balance # this will add the balance to account
                print(account)
                break
            elif account <= 0 and balance <= 0:
                print("\nNot sufficient funds! Retry another time!")
                continue
            else:
                print("\nNot sufficient funds! Retry another time!")
                break
    # If the user type "purchase" the program will ask user inputs and if not int() the user will need to restart
    elif action == "purchase":
        name = str(input("Enter the name of product: "))
        try:
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity required: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # If account is higher then the purchase price entered then add the variable into the warehouse_list[] as a dictionary
        if account > price:
            # warehouse_list.append({"name" : name, "price" : price, "quantity" : quantity})
            warehouse_list.copy({"name" : name, "price" : price, "quantity" : quantity})
            account -= price * quantity # substract the purchased items from the account
            print(f"\nPurchase has been successful! {quantity} unit(s) of {name} bought for a total of {price * quantity}.")
            print(warehouse_list)
            print(account)
        else:
            print("\nNot enough fund, Bruh!!!!")
            print(account)

    # If the user type "sale" the program will ask user inputs and if not int() the user will need to restart
    elif action == "sale":
        name = input("Enter the name of product: ")
        try:
            price = int(input("Enter the price of the product: "))
            quantity = int(input("Enter the quantity required: "))
        except ValueError:
            print("\nIncorrect input, Please retry!")
            continue
        # in the for loop checking if the warehouse_list[] there is availability of the item(s) requested.
        #If the user wants to sale less quantity then the quantity is calculated and updates the warehouse_list[]
        for w in warehouse_list:
            if w["name"] == name and (w["price"] <= price or w["price"] >= price) and w["quantity"] >= quantity:
                w["quantity"] -= quantity
                account += price * quantity
                print(f"\nSale has been successful! {quantity} unit(s) of {name} sold for a total of {price * quantity}.")
                print("Updated warehouse:", warehouse_list)
                print("Updated account balance:", account)
                break
        else:
            print("\nProduct not found or insufficient quantity in the warehouse, Bruh!!!")

    elif action == "account":
        print(f"\nThe total ammount availble is € {account}!")

    elif action == "list":
        for key, value in warehouse_list.items():
            print(f"- {key}: {value}")
        # print(f"\nThe warehouse availability is the following: \n{warehouse_list}")

    elif action == "warehouse":
        name = input("Enter the name of product: ")
        for find in warehouse_list:
            if find["name"] == name:
                print(f"\nHere is the result:\n\nName: {find["name"]}\nPrice: {find["price"]}\nQuantity: {find["quantity"]}")
                break
            else:
                print("\nProduct is not in the system, Bruh!!!")

    elif action == "review":
        try:
            from_indice = int(input("Enter FROM when you want to check historycal data, start from 1 as been the oldest in time: "))
            to_indice = int(input("Enter the TO when you wan to check data, higher number means lastest: "))
        except ValueError:
            print("\nIncorrect input, please retry!")
            continue
        if from_indice >= 0 and to_indice <= len(warehouse_list):
            print(warehouse_list[from_indice:to_indice])
            
        else:
            print("\nNot in range, Bruh!!!")
        
    else:
        print("\nInvalid command!\n")


#             from_indice_input and to_indice_input are the input values obtained from the user.

#     int(from_indice_input): Converts from_indice_input to an integer using the int() function.

#     if from_indice_input else 0: This is a conditional expression (also known as a ternary operator). It checks if from_indice_input is non-empty (truthy). If it is, the expression evaluates to int(from_indice_input). If it is empty (falsy), the expression evaluates to 0.

#     So, effectively, this line ensures that from_indice is an integer value if from_indice_input is non-empty, otherwise, it is set to 0.

#     to_indice = int(to_indice_input) if to_indice_input else len(operations_recorded): Similar to the previous line, this converts to_indice_input to an integer if it is non-empty, and if it is empty, it is set to the length of operations_recorded.

#     This line ensures that to_indice is an integer value if to_indice_input is non-empty, otherwise, it is set to the length of operations_recorded.

# In summary, these lines handle the conversion of user input to integers (from_indice and to_indice) while gracefully handling the case when the user presses Enter without entering any value. If the user input is empty, the default values are set to 0 and the length of operations_recorded, respectively.
        
        