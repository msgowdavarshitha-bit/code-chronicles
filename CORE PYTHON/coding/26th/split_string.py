str="Rama is sleeping"
str1=str.split()  
print(str1)

#length
print(len(str1))


#string indexing
print(str[0])


#Task 2:-  
#str="Raama is sleeping"
#str1="Seelping is Raama"

#Split it first and then reverse the splitted string
print(str1[::-1])


#Without using slicing
new=" "
for i in str1:
    new=i+" "+new
print(new)