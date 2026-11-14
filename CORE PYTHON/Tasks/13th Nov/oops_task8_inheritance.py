# Task 8: Inheritance – Electronic Product & Clothing Product 
# 
# Concept: Inheritance 
# 
# Question: 
# Create a parent class Product with the following attributes: 
#   ● product_name
#    ● product_id 
#   ● price 

# Create two child classes: 
# 
# ElectronicProduct 
# ● Additional attribute: warranty_period 
# ● Method: display_warranty()
#  
# ClothingProduct 
# ● Additional attribute: size 
# ● Method: display_size() 
# 
# Requirements: 
# 1. Create a constructor using __init__(). 
# 2. Use inheritance to access parent class attributes. 
# 3. Create separate methods specific to each product category. 
# 4. Create objects for both child classes. 
# 5. Display the complete product details.  

class Product:
    def __init__(self,product_name,product_id,price):
        self.product_name=product_name
        self.product_id=product_id 
        self.price=price
    
    def display(self):
        print("Name of the product: ",self.product_name)
        print("ID of the product: ",self.product_id)
        print("Price of the product: ",self.price)

class ElectronicProduct(Product):
    def __init__(self,product_name,product_id,price,warranty_period):
        Product.__init__(self,product_name,product_id,price)
        self.warranty_period= warranty_period 

    def display_warranty(self):
        print("The warranty period is: ",self.warranty_period)


class ClothingProduct(Product):
    def __init__(self,product_name,product_id,price,size):
        Product.__init__(self,product_name,product_id,price)
        self.size= size 
    
    def display_size(self):
         print("The size of the product is: ",self.size)

product_name=input("Enter the product name: ")
product_id=input("Enter the product ID: ")
price=int(input("Enter the product price: "))
warranty_period=int(input("Enter the warranty period in months: ")) 
size=input("Enter the product size: ")
o1=ElectronicProduct(product_name,product_id,price,warranty_period)
o2=ClothingProduct(product_name,product_id,price,size)


print()
o1.display()
o1.display_warranty()
print()
o2.display()
o2.display_size()

print()
o2.display()
o1.display_warranty()
o2.display_size()