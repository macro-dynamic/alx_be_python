def display_menu():
    """
    This function prints the shopping list menu options.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:
        display_menu()  # Ensure the menu is displayed in each iteration
        try:
            choice = int(input("Enter your choice (1-4): "))  # Input is cast to integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Add an item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == 2:
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        elif choice == 3:
            # View the current shopping list
            if shopping_list:
                print("\nShopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a numb
