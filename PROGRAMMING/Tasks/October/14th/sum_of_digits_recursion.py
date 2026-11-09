def digitSum(n,res):
    if n<=0:
        return res
    digit=n%10

    return digitSum(n//10,res+digit)


n=int(input("Enter the number: "))
print(digitSum(n,0))

