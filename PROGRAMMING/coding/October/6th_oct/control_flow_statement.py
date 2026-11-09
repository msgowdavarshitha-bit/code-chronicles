print("Control flow statements")
#THe statements that control the execution flow of program
#Types
#1. Conditional statements
#   a.simple if
#   b.if-else
#   c. if-elsif ladder
#   d. Short hand if

#2.Looping statements:
#   1.for loop 
#       -> With range() = Increment and decrement
#       -> without range()
#   2. while loop
#   3. JUmping statements
#           break , continue , return


print("For loop")
#1. for with range() function
# range() is a predefined function that helps to execute the defined sequence values 'internally'
# Syntax:- range(start,stop,step)
#start,stop,step can be integers only
#Start--> from where the sequence should begin  and default is 0
#End/stop --> It is compulsory to be passed and defines till where the sequence should get executed
#Step--> it is the difference between curr3ent element and next element  and default is +1



print(range(1,10,+2))
print(range(5))
print(range(77,80))
#print(range())  --->  atleast 
#It cannot store individual value 
#Syntax :- for variable_name in range(start,end,step):
                #logic
           #remaining statements of the program

#Incrementing for loop:
#    for var_name in range(start,(actual end - 1),positive step)
#       #logic
#   #remaining code

#Write a program to display natural numbers from begining with difference of 3 upto n where n is also included

n=int(input())
arr=[]
for i in range(1,n+1,3):
    arr.append(i)


m=20
for j in range(1,m+1,+3):
    print(j,end=" ")
print("\n Last j: ",j)


print("Rules for increment for loop")
#pass the positive step
#if the actual value also need to be included then (actual_end+1)
#Start should be lesser than the mentioned end value


print("Decrementing for loop")
#syntax :- for var_name in range(start,actual_end - 1, -ve step)
                #logic
           #remaining code
#I wan to display a natural numbers starting from 1 in a decrementing order with the difference of 5


print("rules")
#compulsory pass the negative step
#start should be greater than mentioned end
#if the actual end value should be included then (actual end-1)

m=8
actual_end=1
for j in range(n,(actual_end-1),-4):
    print(j,end=" ")
print("\n Last j: ",j)





print("****"*10)
print("FOr without range()")
# for var_name in iterable / group of elements:
    #logic
#remaining code


print("RULES")
#no single valued data 
#the cursor moves only in forward direction
#it directly fetches each individual value
#even iterable objects are valid/ works
#group of elements can be passed by segregating them using comma ','

#NOTE for with range when used on an iterable object like arrays or string it represents index 
#   for without range when used on an iterable objects it represents values


arr=[8,10,[23],"abc"]
for i in arr:
    print(i,end=" ")

for j in range(0,len(arr)):
    print(arr[j],end=" ")

for i in 10,23,"ade":
    print(i,end=" ")
for j in "":
    print(j,end=" ")
for j in []:
    print(j,end=" ")
for j in "100":
    print(j,end=" ")
#for j in 100:    this through an error because integer is not iterable
#    print(j,end=" ")
for j in 23,9,7,10,20," ":
    print(j,end=" ")


