#it is a in-build data structure that holds the data in key value format

#it is an iterable object(same shared m/m location )
#it is represented by curly braces{}
#Eg:- dict_name={key1:value1, key2,value2,.......,key_n:value_n}

dict={101:"Raadha",102:"suma",103:"Raadha"}
print(dict)

#each single pair of key-value is called as item
#dictionary can also be defined as collection of items
#to get the count of number of items in dictionary :- we use len(iterable_object) 

#keys are the unique elements that is stored into key part of a dictionary
#if a key is tried to be duplicated then it holds the latest updated value
#Type of the keys:- 
#every primitive and immutable data type elements can be passed as key of dictionary  where as mutable objects like list,sets cannot be passed as a key
#dictionary cannot be passed as a key
#empty sting can also be a key

#dict.keys() --> return all the keys of the passed dictionary


print("Values")
#it can be duplicated
#any element can be passed as a value in a dictionary
#dict.values() ---> return all the values of the passed dictionary
#it can be empty also and anything such as list,tuple,string,dictionary....

print("To return each item one by one from the dictionary:- 'dict.items()'")

dict={100:"Hi",102:"value1"}
print(len(dict))
print(len(dict.keys()))
