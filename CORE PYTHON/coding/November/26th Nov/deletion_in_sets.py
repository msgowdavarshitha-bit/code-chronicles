print("Deletion of element/ 's in a set")

s={10,20,30,40,50}
print(s)

s.remove(20)
print(s)

s.discard(30)
print(s)


# s.remove(29)
# print(s)

#ERROR
#     s.remove(29)
# KeyError: 29


print(s.discard(39))
print(s)

