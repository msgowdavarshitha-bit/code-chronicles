arr=[]

print(arr)
print(len(arr))

print("Append") 
arr.append(10)
arr.append(2.4)
arr.append("ji")
arr.append((1,2))
print(arr)



print("===="*8)
print("Insert") 

arr.insert(2,88)
print(arr)
arr.insert(15,"jio11")
print(arr)


print("Manually")

arr[3]=233
print(arr)

# arr[9]=223      this through a error bcz when we use manual adding or accessing that index should be present previously
# print(arr)

print("====")
arr1=[2.3,5,42,0]
print(arr1)
arr2=[3,5]
print(arr2)

arr1.append(arr2)
print(arr1)
print(arr2)

arr2[1]=10
print(arr1)
print(arr2)

arr[3][0]=10
print(arr1)
print(arr2)




arr3=[3,5,7,4,4]
print(arr3)

s1="abjk"
print(s1)

arr3.extend(s1)
print(arr3)
print(s1)
arr3.extend(101)