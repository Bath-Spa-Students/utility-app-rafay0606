
#Vending Machine Simulator Program

#Dispaying the Title Message using ASCII Art

print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")

class VendingMachine:
    def __init__(self):
        # Menu items along with their codes, prices & category
        self.menu = {
            'S1': {'name': 'Smarties', 'price': 4.00, 'category': 'Sweets'},
            'V2': {'name': 'Vimto', 'price': 1.50, 'category': 'Drinks'},
            'P3': {'name': 'Perrier Sparkling Water', 'price': 6.50, 'category': 'Drinks'},
            'I4': {'name': 'Indomie Cup Noodles', 'price': 5.00, 'category': 'Snacks'},
            'K5': {'name': 'Kitkat Classic', 'price': 2.00, 'category': 'Sweets'},
            'R5': {'name': 'Redbull', 'price': 7.50, 'category': 'Drinks'},
            'L6': {'name': 'Lays Salt Chips', 'price': 1.00, 'category': 'Snacks'},
            'S7': {'name': 'Safari Chocolate', 'price': 3.50, 'category': 'Sweets'},
            'D8': {'name': 'Dairy Milk', 'price': 15.00, 'category': 'Sweets'},
            'S9': {'name': 'Sandwich', 'price': 6.50, 'category': 'Hot Food'},
            'S10': {'name': 'Sando Wafer', 'price': 1.50, 'category': 'Snacks'}
        }
        
        # Stock system
        self.stock = {'S1': 9, 'V2': 16, 'P3': 3, 'I4': 23, 'K5': 5, 'R5': 7, 'L6': 6, 'S7': 17, 'D8': 18, 'S9': 8, 'S10': 4}

        # Money in the machine
        self.money_in_the_machine = 0.00

    # Displaying the menu along with border
    def display_menu(self):
        print("\n" + "=" * 30 + " Vending Machine Menu " + "=" * 30)
        categories = set(item['category'] for item in self.menu.values())

        for category_index, category in enumerate(categories, start=1):
            print(f"{category_index}. {category}")

        print("=" * 74)
    
    # Allowing the customer to select a category from the menu or enter '0' to stop the exploration 
    def input_category(self):
        while True:
            try:
                selected_category_index = int(input("Enter the number of the category you want to explore, or '0' to stop: "))
                if selected_category_index == 0:
                    return None
                categories = set(item['category'] for item in self.menu.values())
                if 1 <= selected_category_index <= len(categories):
                    return list(categories)[selected_category_index - 1]
                else:
                    print("Invalid category number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Setting Border & displaying submenu for selected category   
    def display_submenu(self, category):
        print("\n" + "=" * 30 + f" {category} Menu " + "=" * 30)
        for code, item in self.menu.items():
            if item['category'] == category:
                stock_status = "(Out of Stock)" if self.stock[code] == 0 else ""
                print(f"{code}: {item['name']} - AED {item['price']} {stock_status}")

        print("=" * 74)

    # Reciving input from user
    def input_code(self):
        return input("Enter the code of the item you want to purchase, or '0' to go back to categories: ")

    # Accepting cash from the customer 
    def accept_money(self):
        money_inserted = float(input("Insert money: AED "))
        self.money_in_the_machine += money_inserted
        return money_inserted

    # Calculating the change of money to give back
    def calculate_change(self, item_price, money_inserted):
        return money_inserted - item_price

    # Giving the customer the item needed & updating stock of that SKU
    def dispense_item(self, code):
        if code in self.menu and self.stock[code] > 0:
            item = self.menu[code]
            self.stock[code] -= 1
            print(f"Dispensing {item['name']}...")
            return item
        else:
            print("Sorry, we are currently out of stock or the selected item is invalid.")
            return None
        
    #Dislaying change to give to the customer
    def display_change(self, change):
        print(f"Change: AED {change:.2f}")

    # Offering customer to add other items in the cart as well according to their selected category
    def suggest_purchase(self, category):
        suggestions = [item['name'] for code, item in self.menu.items() if item['category'] == category and self.stock[code] > 0]
        if suggestions:
            print(f"Consider adding {', '.join(suggestions)} to your purchase!")

    # Thank You Message after shopping
    def thank_you_message(self):
        print("Thank you for shopping with us. Have a great day!")

    # # Main execution loop to manage the program's flow and user interactions
    def run(self):
        while True:
            self.display_menu()
            selected_category = self.input_category()

            if selected_category is None:
                self.thank_you_message()
                break

            if selected_category in set(item['category'] for item in self.menu.values()):
                while True:
                    self.display_submenu(selected_category)
                    code = self.input_code()

                    if code.lower() == '0':
                        break

                    if code in self.menu:
                        item = self.menu[code]
                        item_price = item['price']

                        money_inserted = self.accept_money()

                        if money_inserted >= item_price:
                            change = self.calculate_change(item_price, money_inserted)
                            purchased_item = self.dispense_item(code)
                            if purchased_item:
                                self.display_change(change)
                                self.suggest_purchase(item['category'])
                        else:
                            print("Insufficient funds. Please insert more money.")
                    else:
                        print("Invalid code. Please enter a valid code from the menu.")
            else:
                print("Invalid category. Please enter a valid category from the menu.")

# Finally, Running the program
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()