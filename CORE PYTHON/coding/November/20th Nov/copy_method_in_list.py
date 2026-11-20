import copy

l=[10,20,30,40]
print(l)
print(l[2])


print("Shallow copy")
l1=l
print(l1)
l[2]=50   #shallow copy
print(l)
print(l1)



print("Deep copy using copy()")
l2=l.copy()
print(l2)
l[3]=60
print(l)
print(l1)
print(l2)


# [10, 20, 30, 40]
# 30
# Shallow copy
# [10, 20, 30, 40]
# [10, 20, 50, 40]
# [10, 20, 50, 40]
# Deep copy using copy()
# [10, 20, 50, 40]
# [10, 20, 50, 60]
# [10, 20, 50, 60]
# [10, 20, 50, 40]