'''
Write a Python class Restaurant with attributes like menu_items, book_table, 
and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.

Perform the following tasks now:
    - Now add items to the menu.
    - Make table reservations.
    - Take customer orders.
    - Print the menu.
    - Print table reservations.
    - Print customer orders.

Note: Use dictionaries and lists to store the data.
'''


class Restaurant:

    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price
        return self.menu_items

    def remove_item_from_menu(self, item):
        self.menu_items.pop(item)
        return self.menu_items

    def book_tables(self, reservation):
        self.book_table.append(reservation)
        return self.book_table

    def customer_order(self, table, order):
        if table in self.book_table:
            self.customer_orders.append({table: order})
        else:
            print(f"Table number {table} is not reserved")
        return self.customer_orders

    def cancel_order(self, table):
        self.customer_orders.pop(table)
        return self.customer_orders

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table(self):
        print("Reserved Tables:")
        for table in self.book_table:
            print(f"Table number {table} is reserved")

    def print_order(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            for table, order in order.items():
                print(f"Table {table}: {order}")


restaurant = Restaurant()
restaurant.add_item_to_menu("Ice Cream", 2.99)
restaurant.add_item_to_menu("Coffe", 1.99)
restaurant.add_item_to_menu("Water", 0.99)
restaurant.add_item_to_menu("Tea", 3.99)
restaurant.add_item_to_menu("Pizza", 5.99)
restaurant.add_item_to_menu("Pasta", 4.99)
restaurant.book_tables("1")
restaurant.book_tables("2")
restaurant.book_tables("3")
restaurant.book_tables("4")
restaurant.customer_order("1", ["Ice Cream", "Coffe"])
restaurant.customer_order("2", ["Water", "Tea"])
restaurant.customer_order("8", ["Pizza", "Pasta"])
restaurant.print_menu()
restaurant.print_table()
restaurant.print_order()
