
import sys
inventory = {}

def format_currency(value):
    return f"${value: ,}"

def add_new_item():
    name = input("Enter item name").strip()
    if name in inventory:
        print("Item already exits")
        return
    try:
        price = float(input("Enter item price: "))
        stock = int(input("Enter stock quantity"))
        category = input("Enter category").strip()
        inventory[name] = {
            "price":price, 
            "stock":stock, 
            "category": category
            }
        print(f"{name} added to inventory.")
    except ValueError:
        print("Invalid input")

def show_menu():
    print("\n=== SMART INVENTORY MANAGER ===")
    print(f"Current Inventory Value: {format_currency(get_inventory_value())}")
    check_low_stock(alert_only=True)
    print("\n1. Add New Item")
    print("2. Update Stock (Add/Remove)")
    print("3. Search Items by Category")
    print("4. Check Low Stock Items")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")

    def add_new_item():
        name = input("Enter item name: ").strip()
        if name in inventory:
            print("Item already exist.")
            return
        try:
            price = float(input("Enter the item price: "))
            stock = int(input("Enter stock quantity: "))
            category = input("Enter category: ").strip()
            inventory[name] = {
                "price":price, 
                "stock":stock, 
                "category":category
                }
            print(f"{name} added to inventory.")
        except ValueError:
            print("Invalid Input")

# Update Stock
def update_stock():
    name = input("Enter item name to update: ").strip()
    if name not in inventory:
        print("Item not found")
        return
    try:
        change = int(input("Enter the stock change (positive to add and negative to remove): "))
        new_stock = inventory[name]["stock"] + change
        if new_stock < 0:
            print("Cannot have a negative stock")
        else:
            inventory[name]["stock"] = new_stock
            print(f"{name} stock updated to {new_stock}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Search by category
def search_by_category():
    category = input("Category to search: ").strip().lower()
    found = [item for item, info in inventory.items() if info ["category"].lower() == category]
    if found:
        print(f"Found {len(found)} items in '{category.title()}':")
        for item in found:
            info = inventory[item]
            print(f"- {item} - {format_currency(info['price'])} ({info['stock']}) in stock")
    else:
        print(f"No items found in the category '{category}'.")

# Check low stock
def check_low_stock(alert_only=False):
    low_stock = [item for item, info in inventory.items() if info["stock"] <= 5]
    if low_stock:
        print("LOw Stock Alert:")
        for item in low_stock:
            print(f"- {item} ({inventory[item]['stock']} units remaining)")
    elif not alert_only:
        print("All items have sufficient stock")
    elif alert_only and not low_stock:
        pass

def get_inventory_value():
    return sum(info["price"] * info["stock"] for info in inventory.values())

def calculate_total_inventory_value():
    total = get_inventory_value()
    print(f"\n Total inventory Value: {format_currency(total)}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option").strip()
        if choice == '1':
            add_new_item()
        elif choice == '2':
            update_stock()
        elif choice == 3:
            search_by_category()
        elif choice == 4:
            check_low_stock(alert_only=False)
        elif choice == 5:
            calculate_total_inventory_value()
        elif choice == 6:
            print("Exiting smart inventory Manager.")
            break
        else:
            print("Invalid choice.")
main()
