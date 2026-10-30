def leap(y):
    return ((y%400!=0 and y%4==0) or (y%400==0))

y1=int(input("Enter: "))
y2=int(input("Enter: "))

for i in range(y1,y2+1):
    if leap(i):
        print(i,"Leap")
    else:
        print(i,"Not leap")


print("========="*5)
def leap(y):
    return ((y%400!=0 and y%4==0) or (y%400==0))

y1=int(input("Enter: "))
y2=int(input("Enter: "))

print("Leap years")
for i in range(y1,y2+1):
    
    if leap(i):
        print(i,end=" ")


print("\nNon leap years")
for j in range(y1,y2+1):
   
    if not leap(j):
        print(j,end=" ")
