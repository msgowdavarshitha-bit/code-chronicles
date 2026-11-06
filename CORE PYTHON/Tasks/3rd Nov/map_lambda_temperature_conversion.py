# Task 7: Map Scenario: Temperature Conversion Given Celsius temperatures: 
# Formula: temperatures = [0, 25, 30, 37, 100] 
# Use map() and lambda to convert Celsius to Fahrenheit. 
# 
# 𝐹 = (𝐶 × 9/5) + 32 
# 
# Also: 
# ● Convert all numbers into squares. 
# ● Convert all names into uppercase. 
# ● Add 100 to each number in a list. 


def temperature_conversion(celsius):
    F=(celsius*9/5)+32
    return F


c=int(input("Enter the temperature in celsius: "))
print("The temperature before conversion into Fahrenheit: ",c)

result=list(map(temperature_conversion,[c]))

print("The temperature after conversion into Fahrenheit: ",result)