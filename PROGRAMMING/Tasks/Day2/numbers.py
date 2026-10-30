print("2. Imagine processing a list of numbers where you want to skip negative values, but stop completely if you find a zero ")


lst=[1,9,-1,9,4,33,-287,-19,84,91,-8,10,-20,0,21,-29,98,100]


for i in lst:
    if i<0:
        continue
    elif i==0:
        break
    print(i)