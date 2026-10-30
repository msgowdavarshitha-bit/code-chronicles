n=int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2!=0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()




#     Enter the number: 4
# A b C d 
# A b C d 
# A b C d 
# A b C d 