def square(numbers):
    return numbers**2

numbers=[2, 3, 4, 5, 6]
print(list(map(square, numbers)))


def uppercase(name):
    return name.upper()

names=["varshitha","Bajarangi","Raama","Seetha"]
print(list(map(uppercase, names)))





def add_hundred(n):
    return n+100

numbers = [10, 20, 30, 40, 50]
print(list(map(add_hundred, numbers)))