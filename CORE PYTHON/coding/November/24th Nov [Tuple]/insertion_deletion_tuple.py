t=(10,20,30,40,50)
print(t)

print("Insertion of 25")
t=(t[:2]+(25,)+t[2:])
print(t)


print("deletion of 40")
t=(t[:4]+t[5:])
print(t)