t=(10,20,30,40,50,60)

print(t)
print(t[4])
print(t[:-2])
print(t[-2:])
print(t[-4:4])
print(t[4:1:-1])
#print(t[-5:1:0])  ValueError: slice step cannot be zero
print(t[4:1:1])


# (10, 20, 30, 40, 50, 60)
# 50
# (10, 20, 30, 40)
# (50, 60)
# (30, 40)
# (50, 40, 30)
# ()