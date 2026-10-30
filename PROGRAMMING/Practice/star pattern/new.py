n=int(input("NUmber: "))

noc=7


for i in range(1,n+1):
    for j in range(1,n*2):
        if j<=i or j>=noc:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    noc-=1   #bcz for the next we want to update noc as 6 so that * PRINTS on 6 and 7 both



print("=="*20)

