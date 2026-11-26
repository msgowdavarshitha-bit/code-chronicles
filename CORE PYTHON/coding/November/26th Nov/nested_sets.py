#NOTE:- nested sets are not allowed in python
#list inside sets is also not allowed
#Only tuple inside sets is allowed because tuple is immutable and set is mutable

# s={10,20,{3,6,4},111} -----------> TypeError: unhashable type: 'set'
# print(s)

# s1={10,20,[3,6,4],111} -------> TypeError: unhashable type: 'list'
# print(s1)


s2={10,20,(3,6,4),111}
print(s2)
