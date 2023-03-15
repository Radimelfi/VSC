# Unlimited Arguments 

# *Args 
def add (*args):
    for n in args:
        print (n)

def add(*args):
    sum = 0
    for n in args:
       sum += n
    return sum 

print(add(1,2,3,3,5,6,1,))

# **kwargs allow to built a dictionary 
def calculadora (n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n*= kwargs["multiply"]
    n/= kwargs["divide"]
    print(n)

calculadora (2, add= 3, multiply =3, divide= 5)

# how **kwargs work in class also we can use kw.get("model") for avoid error
class Car:
    def __init__(self, **kw):
        self.make =kw["make"]
        self.model = kw["model"]

my_car = Car(make = "nissan", model= "GT-R")
print (my_car.model)