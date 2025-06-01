# Author: Tega Omarejedje
# Project: Implement Your own Data Structures
# Date: 05/31/2025

# Inventory Manager Program
# Manages a store's inventory by allowing the user to add, remove, update, and view items.

def display_inventory(inventory):
    """Displays the inventory in a user-friendly format."""
    if not inventory:
        print("Inventory is currently empty.")
    else:
        print("\nCurrent inventory:")
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
    print()

def calculate_total_value(inventory):
    """Calculates the total value of all items in the inventory."""
    total = sum(quantity * price for quantity, price in inventory.values())
    print(f"Total value of inventory: ${total:.2f}\n")

def add_item(inventory):
    """Adds a new item to the inventory."""
    item = input("Enter item name to add: ").lower()
    if item in inventory:
        print(f"{item} already exists. Use update to change its details.")
    else:
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory[item] = (quantity, price)
            print(f"{item} added successfully!\n")
        except ValueError:
            print("Invalid input. Quantity must be an integer and price a number.\n")

def remove_item(inventory):
    """Removes an item from the inventory."""
    item = input("Enter item name to remove: ").lower()
    if item in inventory:
        del inventory[item]
        print(f"{item} removed successfully.\n")
    else:
        print(f"{item} not found in inventory.\n")

def update_item(inventory):
    """Updates the quantity or price of an existing item."""
    item = input("Enter item name to update: ").lower()
    if item in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (quantity, price)
            print(f"{item} updated successfully!\n")
        except ValueError:
            print("Invalid input. Quantity must be an integer and price a number.\n")
    else:
        print(f"{item} not found in inventory.\n")

def main():
    """Main function to run the Inventory Manager."""
    inventory = {
        "apple": (10, 2.5),
        "banana": (20, 1.2)
    }

    print("Welcome to the Inventory Manager!")

    while True:
        print("Choose an option:")
        print("1. Display inventory")
        print("2. Add item")
        print("3. Remove item")
        print("4. Update item")
        print("5. Calculate total value")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            remove_item(inventory)
        elif choice == "4":
            update_item(inventory)
        elif choice == "5":
            calculate_total_value(inventory)
        elif choice == "6":
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
