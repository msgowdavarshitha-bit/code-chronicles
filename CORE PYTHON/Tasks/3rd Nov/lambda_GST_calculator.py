# Task 5: 
# Lambda Scenario: Product Price Create a lambda function that accepts a product price and returns the price with 18% GST added. 




result=lambda price:price+price*0.18   #actual price + 18(0.18 %) of gst on the actual price

price=int(input("Enter the price: "))
print(result(price))