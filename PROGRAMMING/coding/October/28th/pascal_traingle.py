print("Pascal's traingle")

n=int(input("Enter: "))


for i in range(0,n):
    num=1
    for k in range(n,i+1,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print(num,end=" ")
        num=(num*(i-j))//(j+1)
    print()


# Enter: 5
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 

print("num=(num*(i-j))//(j+1):-  This is fixed formula for pascal's triangle")

#(n*(i-j))//(j+1)

