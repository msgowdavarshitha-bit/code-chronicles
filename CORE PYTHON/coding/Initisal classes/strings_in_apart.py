print("STRING ")

str="RajaRamMohanRoy"

print(str)
print("String indexing")
print(str[1])
print(str[10])
print(str[-1])
print(str[-12])



print("\nString slicing\n")
print(str[:])
print(str[0:4])
print(str[4:7])
print(str[7:12])
print(str[12:])
print(str[:8])


print("\nUsing step ")
print(str[::-1])
print(str[7:1])  #no o/p  start from 7 and step is default +1 and nothing will print
print(str[7:1:-1])
print(str[-12:-1])
print(str[-5::-1])


print()
print(str[-3:-7])
print(str[:9:-1])
print(str[:-9])
#print(str[-10:-2:0])--->bcz it through a error ValueError: slice step cannot be zero  ("step is default +1, we cannot make it as 0 we can make it as +ve or a -ve but cannot be zero..")

#positive index start from zero left to right
#negative index start from -1  right to left