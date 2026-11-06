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


def discount_generator(discount_percentage):

    def calculate_discount(price):

        discount=(price*discount_percentage)/100
        final_price_after_discount=price-discount

        return final_price_after_discount
    return calculate_discount  #here i returned the inner function so that if it is called then the inner function gets executed 


outer_function=discount_generator(int(input("Enter the discount percentage: ")))

price=int(input("Enter the actual price of the product: "))

final_price=outer_function(price)  #here i,m calling outer function discount generator indirectly calling the inner function

print("The discounted final price: ",final_price)

