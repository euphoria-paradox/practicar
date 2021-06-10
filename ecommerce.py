class Customer:
        def __init__(self, name , email):
                self.name = name
                self.email = email
                self.purchases = []

        def purchase(self,inventory, product):
                inventory_dict = inventory.inventory
                if product in inventory_dict:
                        if inventory_dict[product] > 0:
                                self.purchases.append(product)
                                inventory_dict[product] -= 1
                        else:
                                print("We are out of stock")
                else:
                        print("We don't sell this product")

        def print_purchases(self):
                print("The customer has purchased")
                for item in self.purchases:
                        print(item.name)

class Product:
	def __init__(self , name , price):
		self.name  = name
		self.price = price

class Inventory:
	def __init__(self):
		self.inventory = {}
	
	def add_product(self, product, quantity):
		if product not in self.inventory:
			self.inventory[product] = quantity
		else:
			self.inventory[product] += quantity
	
	def print_inventory(self):
		for key , value in self.inventory.items():
			print(key.name + " : " + str(value))
		
		print('\n')


customers = Customer("Jay" , "jay7@mail.ru")
#print(customers.name)
#print(customers.email)

pwinie = Product("Pwinie" , 250)
#print(pwnie.name)
#print(pwnie.price)

narzo = Product("Narzo 30pro" , 200)

inventory = Inventory()
inventory.add_product(pwinie , 150)
#inventory.print_inventory()
inventory.add_product(narzo , 120)
#inventory.print_inventory()

customers.purchase(inventory , pwinie)
inventory.print_inventory()
customers.print_purchases()
