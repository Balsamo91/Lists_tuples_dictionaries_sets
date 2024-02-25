student_record = ("John Doe", 20, "Computer Science")


# Creating multiple variable from tuple ONLY
name, age, departement = student_record

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Department: {departement}\n")

second_record =  age, departement, name
print(second_record)
print(student_record)