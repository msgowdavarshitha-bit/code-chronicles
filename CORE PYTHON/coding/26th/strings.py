print("26-10-2026")

print("Strings")

print("String interning: ")

# First check if the value is present in the global memory if not present then only create the memory location, if already present pointing to the same  memory location


str1="Raama"
str2="Seetha"

str3="Raama"
str4="Seetha"

str5="Hanumantha"

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

print(id(str1))
print(id(str2))
print(id(str3))
print(id(str4))
print(id(str5))

print(str1 is str2)
print(str1 is str3)
