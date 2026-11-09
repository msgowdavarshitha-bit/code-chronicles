print("3. Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.")


result=0
while True:
    n=int(input("Enter the number: "))

    if n<0:
        break

    result+=n
print(result)

