print("7. Write a program to calculate and print the sum of all natural numbers from 1 to a given number N. ")

a=int(input("Enter a number till where you want the natural numbers sum: "))


result=0

for i in range(1,a+1):
    result=result+i
print(result)