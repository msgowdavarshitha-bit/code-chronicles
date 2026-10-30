print("COMBINATIONAL PATTERNS")

n=int(input("Enter a number: "))

noc=1  #no of columns


for i in range(1,n*2):
    for j in range(1,noc+1):
            print("*",end="")
    print()
    if i<n:
        noc+=1
    else:
         noc-=1



# COMBINATIONAL PATTERNS
# Enter a number: 4
# *
# * *
# * * *
# * * * *
# * * *
# * *
# * 