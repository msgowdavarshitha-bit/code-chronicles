n=int(input("ENter: "))

for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(96+j),end=" ")
    print()

# ENter: 4
# a b c d 
# b c d 
# c d 
# d 




print()

for i in range(1,n+1):
    for j in range(i,1-1,-1):
        print(chr(96+j),end=" ")
    print()
# a 
# b a 
# c b a 
# d c b a 