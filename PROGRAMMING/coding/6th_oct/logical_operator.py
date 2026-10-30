
print("DATE:- 06-10-2026")
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
print((100>98) or (10<15) or True or (10+5))
print(False and 9 and 100)
print(False or 9 or 100)
print((10 and 5) or (1 and 15))
print((10 or 5) and (1 or 15))
print(10 and None)
print(10 or None)
print("" and 10)
print(None or "")
print(-10 and -5)
print(-10 or -5)
print("" and True and None)
print(True and True and None)
print(True or True or None)

print("Not logical operator")
print("It strictly returns only True or false \n It accepts only single operands to perform the operation")

print(not({}))
print(not(10+5))
print(not({}))


