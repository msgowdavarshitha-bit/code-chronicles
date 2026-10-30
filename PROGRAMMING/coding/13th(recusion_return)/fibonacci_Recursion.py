print("WAP to display the fibonacci series for the given position")


def fibSeries(pos,n1,n2): #parameters that should be passed
    if pos<=0:  #base condition 
        return
    print(n1)
    fibSeries((pos-1),(n2),(n1+n2))  # arguments passed or these are the arguments that is to passed/updated for the next cycle

n=int(input("Enter the number: "))
fibSeries(n,0,1)  #values for the initial function call
#Here we dont return in the function call bcz we are printing current cycle value in the every cycle itself so dont return the result just come back
