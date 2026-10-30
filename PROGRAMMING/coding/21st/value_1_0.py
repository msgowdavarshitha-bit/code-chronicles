n=int(input("Enter the number: "))

for i in range(n,1-1,-1):
    for j in range(1,i+1):
        if (i+j)%2!=0:   # even number
            print("0",end=" ")
        else:
            print("1",end=" ")  #Odd number
    print()



    #Check once again  