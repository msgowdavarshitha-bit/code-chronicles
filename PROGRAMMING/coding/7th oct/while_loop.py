print("DATE:- 07-10-2026")
n=int(input("Enter the number: "))
i=0
while n<=i:
	print(i,end=" ")
	i-=1
print("\n Last i: ",i)



#to print every number from n till 0
n = int(input("Enter the number: "))
i = n

while i >= 0:
    print(i, end=" ")
    i -= 1

print("\nLast i:", i)







print("****"*10)
print("\n")

n=int(input("Enter the number: "))
diff=1 
while n<=0:
	print(n,end=" ")
	n=n-diff
	diff+=1
print("\n Last n: ",n)





print("****"*10)
print("\n")

while True:
	n=int(input("Enter a number: "))
	if n==0:
		break
	print("THe number you entered is:",n)




print("****"*10)
print("\n")

while True:
	n=int(input("Enter the number: "))
	if n==10 or n==100:
		continue
	print("The current number is: ")





print("===========================================")
i=1
n=5
while i<=n:
    if i==3:
        continue
    print(i,end=" ")
    i+=1
print("Execution stopped")
