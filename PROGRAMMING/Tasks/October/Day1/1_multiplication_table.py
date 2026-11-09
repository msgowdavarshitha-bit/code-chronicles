print("3.Create a program that takes an integer and prints its multiplication table from 1 to 10. ")


n=int(input("Enter which number table you want: "))


for i in range(1,11):
    print(n,'*',i,"=",n*i)