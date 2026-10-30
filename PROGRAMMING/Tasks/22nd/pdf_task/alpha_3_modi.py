n=int(input("Enter: "))

noc=n
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(chr(64+j),end=" ")
    print()

    if i<n:
        noc-=1
    else:
        noc+=1

# Enter: 6
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# A B C D E F 