print("Arthematic operators ")
l1=[10,20,30]
l2=[40,50,60]

print(l1)
print(l2)


print("+")
print(l1+l2)

#print(l1-l2)   --> TypeError: unsupported operand type(s) for -: 'list' and 'list'
#print(l1/l2)    --> TypeError: unsupported operand type(s) for /: 'list' and 'list'
#print(l1*l2)   --> TypeError: unsupported operand type(s) for *: 'list' and 'list'


print("*")
print(l1*2)
print(l2*6)
print("Rule: list_name * integer_value") #cannot be list1*list2 

print("- and / is not supported operator on list in python")



print("===================================================================================")
print("Membership operators ")

l=[11,22,33,44,55,100]
print(l)
print(11 in l)
print(11 not in l)

print(99 in l)
print(99 not in l)