l=[10,20,30,40]
print(l)

#Adding the elements
l.append(50)
print(l)
l.append(60)
print(l)

l.extend([70,80,90])
print(l)

b=[100,110,120]
l.extend(b)
print(l)

l.insert(2,25)
print(l)

# [10, 20, 30, 40]
# [10, 20, 30, 40, 50]
# [10, 20, 30, 40, 50, 60]
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# [10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

#Removing the elements
l.remove(30)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.clear()            # []
print(l)
del l
#print(l)            #NameError: name 'l' is not defined

# [10, 20, 25, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# [10, 20, 25, 40, 50, 60, 70, 80, 90, 100, 110]
# [10, 20, 25, 40, 50, 60, 70, 80, 90, 100]

a=[10,11,10,10,10,12,10]
print(a.count(10))          #5
a.remove(10)                #[11, 10, 10, 10, 12, 10]
print(a)