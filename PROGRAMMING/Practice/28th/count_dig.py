def countDig(n,count):
    if n<=0:
        return count
    return countDig(n//10,count+1)
    

n=int(input("Enter: "))
a=countDig(n,0)
print(a)