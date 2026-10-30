n=int(input("Number: "))
# nor=(n*2)-1
# noc=1
#No need of nor and noc 

for i in range(1,n*2):
    for j in range(1,n*2):
        if j==1 or j==(n*2)-1 or i==j or (i+j)==(n*2):
            print("*",end="")
        else:
            print(" ",end="")
    print()

    # if i<n:
    #     noc+=1
    #     nor-=1
    # else:
    #     noc-=1
    #     nor+=1


# Number: 4
# *     *
# **   **
# * * * *
# *  *  *
# * * * *
# **   **
# *     *