print("FIBONACCI SERIES")

def fibonacci(pos):
    n1,n2=0,1

    while pos>0:
        print(n1,end=" ")
        temp=n1+n2  #holds the future value before updating
        n1=n2  #n1 will print this cycle value and hold the next cycle value
        n2=temp 
        pos-=1

pos=int(input("Enter the number: "))
fibonacci(pos)


#initially n1=0 and n2=1
#curr(now position value), next(next to current) , future (sum of current and next)
#pos=6
#print(n1)

#n1
#It print current cycle value 
#it holds next cycle value

#n2 
#initially holds next cycle value
#holds thr future cycle value

#pos
#keeps the track of number of cycles

#temp
#temporary memory which holds future cycle value without/before changing current and next cycle value(n1 and n2 respectively)


#to display fibonacci for the given position
    #Using decrementing while loop
    #using incrementing while loop
    #Using decrementing for loop
    #using incrementing for loop