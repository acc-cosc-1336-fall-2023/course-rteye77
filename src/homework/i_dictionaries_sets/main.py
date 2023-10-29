import dictionary

while True:
    inventory = {}
    
    while True:
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            widget_name = input("Enter the widget name: ")
            quantity = int(input("Enter the quantity: "))
            dictionary.add_inventory(inventory, widget_name, quantity)
            print(f"{quantity} {widget_name}(s) added/updated in inventory.")
        elif choice == "2":
            widget_name = input("Enter the widget name to delete: ")
            result = dictionary.remove_inventory_widget(inventory, widget_name)
            print(result)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")