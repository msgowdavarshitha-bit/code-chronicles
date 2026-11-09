print("15. Keep asking the user for a password until they get it right, but lock them out after 3 wrong Note: Let the curr_password be predefined. ")


current_psw="129"


for i in range(1,4):
    n=input("Enter your password: ")
    if n==current_psw:
        print("Correct password.") 
        break

else:
    print("You reached limit of attempt...")
