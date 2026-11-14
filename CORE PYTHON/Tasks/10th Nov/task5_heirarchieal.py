# Task 5: Hierarchical Inheritance – E-Commerce Product 
# → Electronics / Clothing 
# None 
                                                                                                                             
# Objective: Create multiple child classes that inherit common 
# product details from a parent class while implementing 
# category-specific methods. 
# Class Structure 
#                  Product 
#                 /       \ 
#          Electronics   Clothing 
# 1. Parent Class – Product 
# Attributes: 
# ● product_name 
# ● price 
# Method: 
# ● display_product() – Display the common product 
# information. 
# 2. Child Class – Electronics 
# Attribute: 
# ● warranty 
# Methods: 
# ● display_warranty() – Display the warranty period. 
# ● check_warranty() – Display warranty availability. 
# 3. Child Class – Clothing 
# Attribute: 
# ● size 
# Methods: 
# ● display_size() – Display the clothing size. 
# ● check_size() – Display the available size. 
# Task: 
# ● Create an Electronics object for an electronic product. 
# ● Create a Clothing object for a clothing product. 
# ● Access the common properties and methods inherited from 
# the Product class. 
# ● Access the category-specific properties and methods of both 
# child classes. 
# ● Display the complete information of both products. 
# Concept: Hierarchical Inheritance


class Product:
    def display_product(self,product_name,price):
        self.product_name=product_name
        self.price=price

        print("Common product information: ")
        print("Name of the product is: ",product_name)
        print("Price of the product is : ",price)


class Electronics(Product):
    def display_warranty(self,warranty):
        self.warranty=warranty
        print("Warranty Period: ",self.warranty)

    def check_warranty(self):
        if self.warranty:
            print("Warranty is available.")
        else:
            print("Warranty is not available.")


class Clothing(Product):
    def display_size(self,size):
        self.size=size
        print("Clothing Size: ",self.size)

    def check_size(self):
        if self.size:
            print("Size is available.")
        else:
            print("Size is not available.")



# Electronics Product
print()
print("Enter Electronics Product Details")

electronics_name=input("Enter product name: ")
electronics_price=float(input("Enter product price: "))
warranty=input("Enter warranty period: ")


electronics=Electronics()
print()
print("Electronics Product Information")
electronics.display_product(electronics_name,electronics_price)
electronics.display_warranty(warranty)
electronics.check_warranty()





# Clothing Product
print()
print("Enter Clothing Product Details")
clothing_name=input("Enter product name: ")
clothing_price=float(input("Enter product price: "))
size=input("Enter clothing size: ")


clothing=Clothing()
print()
print("Clothing Product Information")
clothing.display_product(clothing_name,clothing_price)
clothing.display_size(size)
clothing.check_size()

