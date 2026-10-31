print("****"*10)
print("Functions")
#it is an independent block of code included to perform and specific action based on the inputs provided
#NOTE  a function can execute its logic only when it is being called

#SYNTAX:- #1.function declaration
        # def fun_name(parameters):
                #function definition/ scope of a function/body of the function
                #logic
                #return value or values
        #function call
#      var_name=fun_name(arguments)

#requirement required variables to perform an action is a parameter
#Arguments are the values that are passed to call a function or function to work
#return will allow to store in a function where it is called and store the result of the operation or the result of the function
#the arguments or the number of the arguments should be in the correct order where the function defined parameters and number of parameter should be same as the number of arguments are passed
#THe program execution will start 


#the input that is required by a function to execute a logic
#argument the values that are passed to a function during a function call for it to execute the logic

#return is a keyword that will and it will the last execution line and anything after the return within the function will not work  " Once return works no other lines of code within the function will execute"

#uses of return 
#it instructs the pvm to take back the execution flow from called function to function call
#it helps to return the val or values from called function back to the function call
#Usability :- It helps the reusability of the code unlimited times

def divNum(num,deno):
    rem=num%deno
    return deno
res=divNum(10,3)
print(res)
res=divNum(res,20)
print(res)