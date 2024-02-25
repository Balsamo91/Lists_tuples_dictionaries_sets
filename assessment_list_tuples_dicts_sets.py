print("\nWelcome to the company's Account and Warehouse!\n")

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
            print("Product not found or insufficient quantity in the warehouse!")

    elif action == "account":
        print(f"\nThe total ammount availble is € {account}!")

    elif action == "list":
        print(f"\nThe warehouse availability is the following: \n{warehouse_list}")

    elif 