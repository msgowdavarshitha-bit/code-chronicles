n=int(input("Num: "))

noc=n

for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(96+j),end=" ")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1


# Num: 4
# a b c d 
# a b c 
# a b 
# a 
# a b 
# a b c 
# a b c d 