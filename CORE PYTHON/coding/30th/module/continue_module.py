from new1 import fun1,fun2

from new2 import fun1,fun2
#from new2 import * ======> is also same 

# fun1()
# fun2()
# fun1()
# fun2()
#in all the above cases the latest import from new 2 is printed so 




#Solution to access the particular files function which are in the same name use file_name.func_name

#use import file_name no need of the specify the function name 
import new1
import new2 
new1.fun1()
new1.fun2()
new1.fun1()
new1.fun2()