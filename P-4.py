shopping_list = []

print(" Welcome to your shopping quest!")
print("Enter 5 unique shopping items:")

while len(shopping_list) < 5:
    item = input(f"Enter item {len(shopping_list) + 1}: ").strip().lower()

    if item in shopping_list:
        print("Duplicate item! Please enter a different one.")
    elif item == "":
        print("Empty input is not allowed.")
    else:
        shopping_list.append(item)

shopping_list.sort()

print("\n Your sorted shopping list:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item.capitalize()}")

remove_choice = input("\nDo you want to remove an item? (yes/no): ").strip().lower()

if remove_choice == "yes":
    item_to_remove = input("Enter the name of the item to remove: ").strip().lower()
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f" '{item_to_remove}' has been removed.")
    else:
        print(" That item was not found in your list.")

print("\n Final shopping list:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item.capitalize()}")
