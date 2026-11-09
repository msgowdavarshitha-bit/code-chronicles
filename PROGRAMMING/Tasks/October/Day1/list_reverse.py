print("9. Given a list, iterate it in reverse order and print each element. ")

lst=[1,5,3,8,9,2,22,7,99,10,17,52,44,51]

print(lst[::-1])



print("to print each element separately one by one ")

for i in range(len(lst)-1,-1,-1):
    print(lst[i])