#Task 01
#1.  str1=" R A M A"  --> to remove the spaces between the characters



str1="R A M A"
str2=" "

for i in str1:
    if i==" ":
        continue
    else:
        str2=str2+i

print(str2)