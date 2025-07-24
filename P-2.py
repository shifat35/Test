first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


first_part = first_name[:3]
last_part = last_name[-3:]


username = (first_part + last_part).lower()

print("Your unique username is:", username)
