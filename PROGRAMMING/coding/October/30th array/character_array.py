def charArr():
    l1=[]
    while True:
        n=input("Enter: ")
        if n=="":
            return l1
        l1.append(n[0])

a=charArr()
print(a)
