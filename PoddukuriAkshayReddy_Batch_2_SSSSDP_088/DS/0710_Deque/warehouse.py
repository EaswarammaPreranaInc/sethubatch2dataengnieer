class WarehouseItem:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}"

class Warehouse:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity):
        if item_id in self.items:
            print("Item ID already exists. Use update to change quantity.")
        else:
            self.items[item_id] = WarehouseItem(item_id, name, quantity)
            print("Item added.")

    def update_item(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id].quantity = quantity
            print("Item updated.")
        else:
            print("Item ID not found.")

    def display_items(self):
        if not self.items:
            print("No items in warehouse.")
        else:
            for item in self.items.values():
                print(item)

def menu():
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. Display All Items")
    print("4. Exit")

if __name__ == "__main__":
    warehouse = Warehouse()
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            warehouse.add_item(item_id, name, quantity)
        elif choice == '2':
            item_id = input("Enter Item ID to update: ")
            quantity = int(input("Enter new Quantity: "))
            warehouse.update_item(item_id, quantity)
        elif choice == '3':
            warehouse.display_items()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
