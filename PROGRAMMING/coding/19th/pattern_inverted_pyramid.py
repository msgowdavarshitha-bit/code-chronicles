#right angle triangle 

#Relationship table:- to understand the relationship between i, j and other variables
#Comparision table:- to know the realtionship and difference between 2 patterns


n=int(input("ENter a number: "))

for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print("* ",end="")  #same as right angled triangle but add space after each *
    print()


# ENter a number: 4
# * * * * 
#  * * * 
#   * * 
#    * 