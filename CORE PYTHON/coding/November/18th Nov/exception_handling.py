try:
    a=int(input("a: "))
    b=int(input("b: "))
    print(a/b)
    
except Exception as e:
    print("It's a error")
    
else:
    print("Executed")