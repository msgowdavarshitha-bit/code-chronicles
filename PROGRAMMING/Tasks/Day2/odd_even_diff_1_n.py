print("WAP to display the difference of sum of first “n” odd numbers and first “n” even numbers.")


n=int(input("Enter the number of odd and even numbers: "))


even_sum=0
odd_sum=0
i=1
while i<=n:
    even_sum+=2*i
    odd_sum+=2*i-1 
    i+=1
print(even_sum - odd_sum)
