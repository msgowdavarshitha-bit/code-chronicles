n=int(input("Enter the number: "))

noc=(n*2)-1
for i in range(1,n+1):
    for j in range(1,n*2):

        if j<=i or j>=noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc-=1


# Enter the number: 4
# *     *
# **   **
# *** ***
# *******