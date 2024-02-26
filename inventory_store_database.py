inventory = {
    "apple": {"category": "fruit", "price": 0.99, "stock": 100},
    "milk": {"category": "dairy", "price": 2.99, "stock": 50},
    "bread": {"category": "bakery", "price": 2.49, "stock": 100}
}

while True:
    print("Available commands: all, category, exit")
    command = input("Enter a command: ")

    if command == "all":
        print("inventory: ")
        for item, details in inventory.items(): # itereting through dict, assigning key to item (for example apple), value to details (nested dict)
            # print(item, details)
            print(f"{item.capitalize()}: ")
            for detail, value in details.items():
                print(f"- {detail.capitalize()}: {value}")

    elif command == "category":
        category = input("Enter a category: ")
        print(f"Inventory in {category.capitalize()}: ")
        for item, details in inventory.items():
            if details["category"] == category:
                print(f"{item.capitalize()}")

    elif command == "add":
        item_name = input("provide item ")
        category = input("provide category: ")
        price = float(input("provide price: "))
        stock = int(input("Provide the amount of items: "))
        inventory[item_name] = {"category": category, "price": price, "stock": stock}

    elif command == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid command")