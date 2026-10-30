n=int(input("enter the number: "))


#here take 2 variables one for increment and other for decrement bcz if u use incrementing to even row next odd row will get effected

count_increment=1

for i in range(1,n+1):

    for j in range(1,n+1):

        if i%2!=0:
            print(count_increment,end=" ")
            count_Decrement=count_increment  #once completed the odd row store that count in a decrement variable 
        else:
            print(count_Decrement,end=" ")  #print the calculated even row first element
            count_Decrement-=1   #once printed decrement

        count_increment+=1 #whatever happens 
    print()

    count_Decrement=count_Decrement+n  # once the odd row done calculate first element of the even row