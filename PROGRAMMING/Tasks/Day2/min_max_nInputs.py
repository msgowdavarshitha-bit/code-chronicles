print(" WAP to accept “n” random positive numbers from the user and display the largest and smallest out of it. ")


#To find smallest and largest number in a given inputs without using list and build-in function we use this method

n=int(input("Enter number of numbers you want to take: "))  # how many numbers'n' numbers i should take from user


# to compare the next entered number with whom will you compare so take first input / number of elements as a base or initial value for both smallest and greatest 
largest=n
smallest=n


#Start with 1
i=1
while i<=n:  #until i <= n do this 
    num=int(input("Enter the  number: "))

    if num>largest:
        largest=num

    elif num<smallest:
        smallest=num 

    i+=1

print("Largest number: ",largest)
print("Smallest number: ",smallest)