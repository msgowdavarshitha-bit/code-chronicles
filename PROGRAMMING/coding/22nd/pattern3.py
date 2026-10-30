n=int(input("Num: "))

c=1
for i in range(1,n*2):
    for j in range(1,c+1):
        print(chr(96+j),end=" ")
    print()

    if i<n:
        c+=1
    else:
        c-=1



# Num: 4
# a 
# a b 
# a b c 
# a b c d 
# a b c 
# a b 
# a 