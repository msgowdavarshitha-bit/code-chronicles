a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))

try:
    print(a/b)
except Exception as e:
    print("Error occurred")  