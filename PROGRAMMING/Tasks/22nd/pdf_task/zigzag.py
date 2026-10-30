n=int(input("Enter: "))

c_i=1

for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2!=0:
            print(c_i,end=" ")
            c_d=c_i
        else:
            print(c_d,end=" ")
            c_d-=1
        c_i+=1
    print()

    c_d=c_d+(i+1)

# Enter: 4
# 1 
# 3 2 
# 4 5 6 
# 10 9 8 7 