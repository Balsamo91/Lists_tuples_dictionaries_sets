print("Welcome to the company's Account and Warehouse!\n")

account = 1000

warehouse = []

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
            warehouse.append({"name" : name, "price" : price, "quantity" : quantity})
            account -= price
            print(warehouse)
            print(account)
        else:
            print("\nNot enough fund, Bruh!!!!")
            print(account)

    elif action == "sale":
        name = input("Enter the name of product: ")
        price = int(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity required: "))
        for d in warehouse:
            if d["name"] == name and d["price"] == price and d["quantity"] >= quantity:
                d["quantity"] -= quantity
                account += price * quantity
                print(f"Sale successful! {quantity} units of {name} sold for a total of {price * quantity}.")
                print("Updated warehouse:", warehouse)
                print("Updated account balance:", account)
                break
        else:
            print("Product not found or insufficient quantity in the warehouse!")








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