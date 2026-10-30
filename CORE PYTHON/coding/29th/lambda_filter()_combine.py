print("WAP to print even numbers in a list using both filter() and lambda function")


l=[2,4,5,6,8,9,1,29]
k=list(filter(lambda num:num%2==0,l))
print(k)