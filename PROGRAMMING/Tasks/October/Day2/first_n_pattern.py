print("12. WAP to display first “n” values of the following series. Eg:  N = 3  2  22  222   N = 5  2  22  222  2222  22222 ")


n=int(input("Enter the number: "))

str_num="2"

for i in range(1,n+1):
    print(str_num*i,end=" ")