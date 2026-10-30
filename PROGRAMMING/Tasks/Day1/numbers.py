print("8. Write a program that prints numbers from 1 to 50. For multiples of 3, print 'Fizz'instead of the number. For multiples of 5, print 'Buzz'. For numbers that are multiples of both 3 and 5, print 'FizzBuzz' ")

a=int(input("Enter the number: "))

for i in range(1,a+1):
    if i%3==0 and i%5==0:    
    #add this as a first condition if not if will check if and it satisfies doesn't go for next elif "In case both 3 & 5 divisible numbers"
            print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    
    else:
        print(i)