print("29-10-2026")

print("ARRAYS")
print("Principles")

#in python arrays are called as lists
#it is an object 
#It is a data structure
#DATA structure is a organized way of storing a data

#Arrays is data structure that stores the data in contiguous memory locations. Each individual memory location is recongnized using the index
#In python arrays can hold both homogenous and heterogenous data
#It is an iterable object
#It can hold 0 or None or empty or single valued data or any other objects also
#Memory is dynamic :- size of m/m locaton can be shrinked or enlarged based on insertion or deletion of values from array
#AN array is python is represented in a pair of [], which can be accessed by using arr_reference_var_name
#Duplicates are allowed
#array m/m is allocated in heap which is assigned by the PVM
#It can hold multiple individual elements into the same m/m location
#To access those individual element we can use array_var_name[index]

#Index:- unique integer value that is assigned by the PVM during the execution to represent the memory location of each individual element
#Python can support both positive and negative indexing :- bcz it is not compatible with other languages so in programming we use +ve indexing
#Positive index start from 0 upto len(array)-1

#Eg:-arr=[12,45,-98,76,34,-99]
#   len(arr)=6  length start from 1 and indexing start from 0
# +ve :- 0



print("#len()  function")
#it is a predefined function that returns the count of number of individuals element present in an 'iterable object'

#It doesn't accept single valued data
#the least val that a len() can return is 0


arr=[10,89.9,"mni",9.8]
print(arr)
print(type(arr))
print(len(arr))

v1={2,3,5,2,1,3,4,2,3,0}
print(v1)
print(type(v1))
print(len(v1))


v2="varshitha"
print(v2)
print(type(v2))
print(len(v2))

dic={1:"HI",3:"Helo"}
print(dic)
print(type(dic))
print(len(dic))

tuple=(2,3,3,1,4)
print(tuple)
print(type(tuple))
print(len(tuple))


val=10768219
print(val)
print(type(val))
#print(len(val)) --> Through an error it is not a iterable object and this is single integer valued data


