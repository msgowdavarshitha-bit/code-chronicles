
print("DATE:- 06-10-2026")
print("***"*10)
print("LOGICAL OPERATORS")
#It is used to combine and check multiple boolean conditions
#I/p is bool conditions 
#o/p is boolean values or anything that represent the bool value
print("Types")
print(" and , or , not ")

print("AND logical operator")
#if all i/p the conditions are true then the o/p is also true or  if any condition is false then it will return false 
#any non zero values are considered to be true
#any empty object , 0 , False , None are considered as "False"


#BOOLEAN CONDITION :-
#   Direct bool_val or anything that represents bool value
#   ANy var that hold bool var or anything that represents bool val
#   An expression that returns bool val or anything that represents bool val 

print(True and (10+5)) #o/p is 15 not a true 
print((100>98) and (10<15) and True and (10+5))  #it will take 10+5=15, here non zero numbers are yes so it will print 15 not as True
print((100>98) or (10<15) or True or (10+5))    #True for 1st condition

print()
print(False and 9 and 100)   #since and doesn't go check next condition simply return the false
print(False or 9 or 100)
print((10 and 5) or (1 and 15))  
print((10 or 5) and (1 or 15))
print(10 and None)   #here condition is false but returns None BCZ NOne is representing False
print(10 or None)

print()
print("" and 10)  #Here empty object is "" so instead of False it print "" represents False
print(None or "")
print(-10 and -5)
print(-10 or -5)

print()
print("" and True and None)
print(True and True and None)
print(True or True or None)




print("===="*5)
print("Not logical operator")
print("It strictly returns only True or false \n It accepts only single operands to perform the operation")

#if true return true and if false return false
print(not({}))
print(not(10+5))
print(not({}))


# Logical and ==> when both the conditions are true it returns true 
# in case of non zeroes otr anything the last value is taken as a result


# #Logical or ==> when the one of the boolean condition anything that represent the boolean condidition such as value or var holding value is considered
# #one of the condition is true returns true 
# It takes the first value as a result


#logical and will return true if false, return false if true