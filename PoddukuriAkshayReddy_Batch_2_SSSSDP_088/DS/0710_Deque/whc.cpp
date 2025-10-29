#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class WarehouseItem {
public:
    string itemID;
    string name;
    int quantity;
    WarehouseItem() {}
    WarehouseItem(string id, string n, int q) : itemID(id), name(n), quantity(q) {}
};

class Warehouse {
    unordered_map<string, WarehouseItem> items;
public:
    void addItem(const string & id, const string & name, int quantity) {
        if (items.find(id) != items.end()) {
            cout << "Item ID already exists. Use update to change quantity.\n";
        } else {
            items[id] = WarehouseItem(id, name, quantity);
            cout << "Item added.\n";
        }
    }
    void updateItem(const string& id, int quantity) {
        if (items.find(id) != items.end()) {
            items[id].quantity = quantity;
            cout << "Item updated.\n";
        } else {
            cout << "Item ID not found.\n";
        }
    }
    void displayItems() {
        if (items.empty()) {
            cout << "No items in warehouse.\n";
        } else {
            for (const auto& pair : items) {
                cout << "ID: " << pair.second.itemID << ", Name: " << pair.second.name << ", Quantity: " << pair.second.quantity << endl;
            }
        }
    }
};

void menu() {
    cout << "1. Add Item\n";
    cout << "2. Update Item Quantity\n";
    cout << "3. Display All Items\n";
    cout << "4. Exit\n";
}

int main() {
    Warehouse warehouse;
    int choice;
    while (true) {
        menu();
        cout << "Enter choice: ";
        cin >> choice;
        cin.ignore();
        if (choice == 1) {
            string id, name;
            int quantity;
            cout << "Enter Item ID: ";
            getline(cin, id);
            cout << "Enter Item Name: ";
            getline(cin, name);
            cout << "Enter Quantity: ";
            cin >> quantity;
            cin.ignore();
            warehouse.addItem(id, name, quantity);
        } else if (choice == 2) {
            string id;
            int quantity;
            cout << "Enter Item ID to update: ";
            getline(cin, id);
            cout << "Enter new Quantity: ";
            cin >> quantity;
            cin.ignore();
            warehouse.updateItem(id, quantity);
        } else if (choice == 3) {
            warehouse.displayItems();
        } else if (choice == 4) {
            cout << "Exiting...\n";
            break;
        } else {
            cout << "Invalid choice. Try again.\n";
        }
    }
    return 0;
}
