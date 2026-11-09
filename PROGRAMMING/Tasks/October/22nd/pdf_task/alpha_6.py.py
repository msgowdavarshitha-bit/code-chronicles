n=int(input("Enter the number: "))

count_increment=1

for i in range(1,n+1):

    for j in range(1,i+1):
        if i%2!=0:
            print(chr(64+count_increment),end=" ")
            count_decrement=count_increment
        else:
            print(chr(64+count_decrement),end=" ")
            count_decrement-=1

        
        count_increment+=1
    print()

    count_decrement=count_decrement+(i+1)

# Enter the number: 5
# A 
# C B 
# D E F 
# J I H G 
# K L M N O 