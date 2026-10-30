def outer():

    print("HI")
    a=10
    print(10)

    def inner():
        print(a)
        b=10
        print(b)
    inner()
    print(a)
    #print(b)

    
#print(a)
outer()
#print(a)