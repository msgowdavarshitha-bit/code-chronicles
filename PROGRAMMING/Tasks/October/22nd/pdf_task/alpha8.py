n=int(input("Enter the number: "))

noc=n  #number of stars on LHS
nor=n   #number of stars on RHS
for i in range(1,n+1):
    for j in range(1,n*2):

        if j>=nor or j<=noc:
            if j<n:
                print(chr(64+j),end="")
            else:
                print(chr(64+ (2*n)-j),end="")
        else:
            print(" ",end="")
    print()
    noc-=1
    nor+=1


# Enter the number: 6
# ABCDEFEDCBA
# ABCDE EDCBA
# ABCD   DCBA
# ABC     CBA
# AB       BA
# A         A