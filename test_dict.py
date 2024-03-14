my_dict = {
    "name": "ben",
    "job": "tech",
}
#print (my_dict["name"])
for item, details in my_dict.items():
    print(item.capitalize(), details)
    for value in details:
        print(f"-{value}")

        