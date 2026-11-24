from itertools import zip_longest
name=["Raama","Seetha","Bajarangi"]
age=[10,25]
info=list(zip_longest(name,age,fillvalue="#"))
print(info)
#[('Raama', 10), ('Seetha', 20)]
print("=================================================================================")
print("If one of the corresponding element is not there solution using zip_longest")


# 