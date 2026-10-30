print("Number pattern")
#at every updated row if the complete row is filled with same value then It is displaying the value present in the variable i
#at every updated row, if the complete row displays the value starting from the same point and ending at certain point or  Starting at certain point and ending at the same point then it is a value from j
#If the pattern is displaying values in continuos series then, it is displaying from third variable



n=int(input("ENter a number: "))

for i in range(n,1-1,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()


# Number pattern
# ENter a number: 4
# 4444
# 333
# 22
# 1



