name = input("Create Username: ")

if len(name) < 3:
    print("Name must contain at least 3 characters")
if len(name) > 50:
    print("Name must contain a maximum of 50 characters")
else:
    print("Name looks good!")
