print("Take user 4 integer list elements from the user and print only the even numbers")


def evenNumCHeck(n):
    if n%2==0:
        return True
    else:
        return False

l=[]
num=int(input("Enter the number of elements you want to add: "))
i=0
while i<num:
    n=int(input("Enter the number: "))
    l.insert(i,n)
    i+=1
print(l)  #To print the list

k=list(filter(evenNumCHeck,l))   #It is compulsory to use the list(filter(..)) 
print(k)  #Address of the k 


#Filter function is used to get some elements from the list based on the condition provided
#Syntax:-  filter(Function_name,List_of_elements)