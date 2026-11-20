print("Dynamic in nature")

l=[]
i=0

while True:
    n=int(input("Enter the number: "))
    l.insert(i,n)

    i+=1
    print("DO you want to continue press 1: ")
    print("DO you want to exit press 2: ")
    choice=int(input("ENter your choice: "))

    if choice==1:
        continue
    else:
        break
print(l)