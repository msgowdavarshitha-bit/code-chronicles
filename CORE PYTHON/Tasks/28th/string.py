# 4.Write a Python program that accepts a string from the user and displays: 
# Length of the string 
# First character 
# Last character 
# String in uppercase 
# String in lowercase 
# Number of occurrences of 'a' Reversed string 

n=input("Enter the string: ")

print(len(n))
print(n[0])
print(n[-1])
print(n.upper())
print(n.lower())

count=0
for i in n:
    if i=='a':
        count+=1
print(count)