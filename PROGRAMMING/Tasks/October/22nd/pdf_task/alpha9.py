n=int(input("Enter the number: "))

noc=n  #number of stars on LHS
nor=n   #number of stars on RHS
for i in range(1,n*2):
    for j in range(1,n*2):

        if j>=nor or j<=noc:
            if j<n:
                print(chr(64+j),end=" ")
            else:
                print(chr(64+ (2*n)-j),end=" ")
        else:
            print(" ",end=" ")
    print()
    if i<n:
        noc-=1
        nor+=1
    else:
        noc+=1
        nor-=1


# Enter the number: 5
# A B C D E D C B A 
# A B C D   D C B A 
# A B C       C B A 
# A B           B A 
# A               A 
# A B           B A 
# A B C       C B A 
# A B C D   D C B A 
# A B C D E D C B A 