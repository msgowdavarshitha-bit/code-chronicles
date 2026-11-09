print("WAP to enter the numbers till the user enters 0 and at the end it should display the count of positive number and negative number separately.")

count_pos=0
count_neg=0

while True:
    n=int(input("Enter the number: "))
    if n==0:
        break

    elif n<0:
        count_neg+=1
    else:
        count_pos+=1

print("Number of positive numbers: ",count_pos)
print("Number of negative numbers: ",count_neg)