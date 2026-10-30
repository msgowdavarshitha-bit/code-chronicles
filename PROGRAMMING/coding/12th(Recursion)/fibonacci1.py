def fibonacciWhileDe(pos):
    n1,n2=0,1

    while pos>0:
        print(n1,end=" ")
        temp=n1+n2  #holds the future value before updating
        n1=n2  #n1 will print this cycle value and hold the next cycle value
        n2=temp 
        pos-=1




def fibonacciWhileIn(pos):
    n1,n2=0,1
    i=0

    while i<pos:
        print(n1,end=" ")
        temp=n1+n2  #holds the future value before updating
        n1=n2  #n1 will print this cycle value and hold the next cycle value
        n2=temp
        i+=1


def fibonacciFor(pos):
    n1,n2=0,1

    for i in range(1,(pos+1)):
        print(n1,end=" ")
        temp=n1+n2  #holds the future value before updating
        n1=n2  #n1 will print this cycle value and hold the next cycle value
        n2=temp


def fibonacciForDecr(pos):
    n1,n2=0,1

    for i in range(pos,0,-1):
        print(n1,end=" ")
        temp=n1+n2  #holds the future value before updating
        n1=n2  #n1 will print this cycle value and hold the next cycle value
        n2=temp

pos=int(input("Enter the number: "))
fibonacciWhileDe(pos)
print()
fibonacciWhileIn(pos)
print()
fibonacciFor(pos)
print()
fibonacciForDecr(pos)
