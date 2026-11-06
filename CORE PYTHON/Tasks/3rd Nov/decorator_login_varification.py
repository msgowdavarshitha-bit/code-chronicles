# Task 4: Decorator Scenario: Login Verification Create a decorator login_required() that checks whether a user is logged in before allowing a function to execute. 
# ● If logged in, display the dashboard. 
# ● If not logged in, display "Please login first." 



log_in=int(input("Enter 1 if logged in 0 if not logged in: "))
def login_required(func):

    
    def check_login():
        if log_in==1:
            func()
            
        else:
            print("Please log-in first")

    return check_login    #closure



@login_required     #decorator login_required outer function
def greet():
    print("Successfully logged in WELCOME....")

greet()