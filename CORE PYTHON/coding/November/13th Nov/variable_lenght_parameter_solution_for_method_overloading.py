def f(*args):
    print(args)
f(10)
f(10,"Raama",8.23)



def f1(**kwargs):
    print(kwargs)
f1(name="Raama",age=22)