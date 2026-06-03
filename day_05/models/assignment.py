# class User:
#     def __init__(self, name, phone_no):
#         self.name = name
#         self.phone_no =phone_no
#     def display_info(self):
#         return f"  name: {self.user}: phone number: {self.phone_no} "
    

# class Customer(User):
#     def __init__(self, name, phone_no, address):
#         super().__init(name, phone_no)
#         self.address = address
#         self.orders = []
       

#     def place_order(self, order):
#         self.orders.append(order)
#         print("your order is successfully placed")

# class FoodItem:
#     def __init__(self, food_name, price):
#         self.food_name = food_name
#         self.price = price

#     def food_details(self):
#         print(f"{self.food_name}-Rs{self.price}")

# class Restaurant:
#     def __init__(self, rest_name):
#         self.rest_name = rest_name
#         self.menu:list[FoodItem]=[]

#     def add_food(self, food:FoodItem):
#         self.menu.append(food)

#     def show_menu(self):
#         for item in self.menu:
#             item.display_food_details()

# class order:
#     def __init__(self, order_id:str, customer:Customer,
#                  restaurant:Restaurant, order_item:list[FoodItem], status):
#         self.order_id = order_id
#         self.customer=customer
#         self.restaurant = restaurant
#         self.order_item = order_item
#         self.status = status

#     def add_item(self, item:FoodItem):
#         self.order_item.append(item)

#     def calculate_total(self):
#         total =0 
#         for item in self.order_item:
#             total +=item.price
#         return total
    
#     def update_status(self, status):
#         self.status=status

#     def show_order(self):
#         print(f"Order id:{self.order_id}")
#         print(f"customer name: {self.customer.name}")
#         print(f"restuarant name: {self.restaurant_name}")
#         for item in self.order_items:
#             item.display_food_details()
#         print(f"order status {self.status}")
#         print(f"bill total: {self.calculate_total()}")


# class DeliveryPartner(User):
#     def __init__(self, name, phone_no):
#         super().__init__(name, phone_no)

#     def delivery_order(self, order:order):
#         order.update_status("preparing")
#         order.update_status("out for delivery")
#         order.update_status("delivery")

# res=Restaurant("KFC")
# food_item1=FoodItem("chicken nuggets", 160)
# food_item2=FoodItem("chicken wrap", 180)
# food_item3=FoodItem("choco lava cake", 100)


# res.add_food(food_item1)
# res.add_food(food_item2)
# res.add_food(food_item3)

# res.show_menu()


class User:
    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no

    def display_info(self):
        return f"Name: {self.name}, Phone Number: {self.phone_no}"


class Customer(User):
    def __init__(self, name, phone_no, address):
        super().__init__(name, phone_no)
        self.address = address
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        print("Your order is successfully placed")


class FoodItem:
    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price

    def display_food_details(self):
        print(f"{self.food_name} - Rs {self.price}")


class Restaurant:
    def __init__(self, rest_name):
        self.rest_name = rest_name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        print(f"\nMenu of {self.rest_name}:")
        for item in self.menu:
            item.display_food_details()


class Order:
    def __init__(self, order_id, customer, restaurant, order_items, status):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.order_items = order_items
        self.status = status

    def add_item(self, item):
        self.order_items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.order_items:
            total += item.price
        return total

    def update_status(self, status):
        self.status = status

    def show_order(self):
        print(f"\nOrder ID: {self.order_id}")
        print(f"Customer Name: {self.customer.name}")
        print(f"Restaurant Name: {self.restaurant.rest_name}")

        print("\nItems Ordered:")
        for item in self.order_items:
            item.display_food_details()

        print(f"\nOrder Status: {self.status}")
        print(f"Bill Total: Rs {self.calculate_total()}")


class DeliveryPartner(User):
    def __init__(self, name, phone_no):
        super().__init__(name, phone_no)

    def deliver_order(self, order):
        order.update_status("Preparing")
        order.update_status("Out for Delivery")
        order.update_status("Delivered")


# Restaurant
res = Restaurant("KFC")

food_item1 = FoodItem("Chicken Nuggets", 160)
food_item2 = FoodItem("Chicken Wrap", 180)
food_item3 = FoodItem("Choco Lava Cake", 100)

res.add_food(food_item1)
res.add_food(food_item2)
res.add_food(food_item3)

res.show_menu()

# Customer
cust = Customer("Neelima", "9876543210", "Belgaum")

# Order
order1 = Order(
    "ORD101",
    cust,
    res,
    [food_item1, food_item3],
    "Placed"
)

cust.place_order(order1)

# Display Order
order1.show_order()

# Delivery Partner
partner = DeliveryPartner("Rahul", "9999999999")
partner.deliver_order(order1)

print("\nAfter Delivery:")
order1.show_order()