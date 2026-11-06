# Task 2: Nested Function  
# Scenario: Electricity Bill Calculator Create an outer function calculate_bill() and an inner function calculate_units(). 
# ● Outer function accepts consumed units. 
# ● Inner function calculates the bill amount. 
# ● Return the final bill. 

def calculate_bill(units, sanctioned_load):

    def calculate_units():

        energy_charge = units * 5.80

        fixed_charge = sanctioned_load * 150

        pg_surcharge = units * 0.35

        total_bill = energy_charge + fixed_charge + pg_surcharge

        return total_bill

    return calculate_units()


units = int(input("Enter consumed units: "))

sanctioned_load = float(input("Enter sanctioned load (kW): "))

bill = calculate_bill(units, sanctioned_load)

print("Total BESCOM Electricity Bill: ", round(bill, 2))