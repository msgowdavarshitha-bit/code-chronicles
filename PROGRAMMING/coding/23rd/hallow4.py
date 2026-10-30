n=int(input("Enter a number: "))

for i in range(n,(1-1),-1):
    for k in range(n,i-1,-1):
        print(" ",end="")
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print() 

# Enter a number: 5
#  * * * * * 
#   *       * 
#    *       * 
#     *       * 
#      * * * * * 

