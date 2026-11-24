print("Zip function")
print("2 or more list are combined to form a new list")

name=["Raama","Seetha","Bajarangi"]
age=[10,20,25]
info=list(zip(name,age))
print(info)

#[('Raama', 10), ('Seetha', 20), ('Bajarangi', 25)]



print("=================================================================================")
print("If one of the corresponding element is not there")
name=["Raama","Seetha","Bajarangi"]
age=[10,25]
info=list(zip(name,age))
print(info)
#[('Raama', 10), ('Seetha', 20)]



print("=================================================================================")
print("If one of the corresponding element is not there solution using zip_longest")

from itertools import zip_longest
name=["Raama","Seetha","Bajarangi"]
age=[10,25]
info=list(zip_longest(name,age,fill_value="#"))
print(info)
#[('Raama', 10), ('Seetha', 20)]

