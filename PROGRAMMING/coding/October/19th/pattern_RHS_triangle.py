n=int(input("ENter the number: "))

for i in range(n,(1-1),-1):  #for the ith 
    for k in range(n,i,-1):  #for the spaces in the left
        print(" ",end="")
    for j in range(1,(i+1)):    #for the printing the *'s
        print("*",end="")
 
    print()



# ENter the number: 4
# ****
#  ***
#   **
#    *