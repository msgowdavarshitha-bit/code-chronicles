try:
    a=int(input("a: "))
    b=int(input("b: "))
    print(a/b)
    
except ValueError as e:
    print("it's a value error")
    
except ZeroDivisionError as e:
    print("it's a ZeroDivisionError error")   
    
except Exception as e:
    print("It's a error")

print("=====================================================================================")
try:
    a=int(input("a: "))
    b=input("b: ")
    print(a/b)
    
except ValueError as e:
    print("it's a value error")
    
except ZeroDivisionError as e:
    print("it's a ZeroDivisionError error")   
    
except Exception as e:
    print(e)



