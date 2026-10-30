print("5.Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.). ")

lis=[1,3,4,5,5,6,3,22,901,3798,73,27,29,84]


for i in range(0,len(lis),2):
    print(lis[i],end=" ")