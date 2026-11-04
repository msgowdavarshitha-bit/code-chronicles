# Task 3: Closure 
# Scenario: Discount Calculator 
# Create a function discount_generator() that accepts a discount percentage and returns an inner function to calculate the discounted 
# price. 
# Example : discount_10 = discount_generator(10) 
# discount_20 = discount_generator(20) 
# print(discount_10(1000)) 
# print(discount_20(1000)) 
# Excepted output:  
# Python 
# 900 
# 800


def discount_generator(discount):

    def calculate_discount():
        discou=10
    return calculate_discount