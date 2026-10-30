n=int(input("ENter: "))

for i in range(1,n+1):
    for j in range(i,n+1):
        print(chr(96+j),end=" ")
    print()



# a 
# b a 
# c b a 
# d c b a 