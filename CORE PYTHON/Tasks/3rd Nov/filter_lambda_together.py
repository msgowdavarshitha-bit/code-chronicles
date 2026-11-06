numbers = [12, 45, 67, 23, 89, 90, 34, 100, 15]


print("Original list: ",numbers)
even=list(filter(lambda numbers:numbers%2==0,numbers))
print("Even numbers in the list: ",even)


divisible_by_5=list(filter(lambda numbers:numbers%5==0,numbers))
print("The numbers divisible by 5: ",divisible_by_5)

greater_than_50=list(filter(lambda numbers:numbers>50,numbers))
print("the numbers greater than 50 are: ",greater_than_50)

between_20_80=list(filter(lambda numbers:numbers>20 and numbers<80,numbers))
print("The numbers between 20 to 80 are: ",between_20_80)