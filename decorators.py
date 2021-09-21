##decorator
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    
    def wrapper_function():
        """ this is wrapper function """
        print("this is awesome function")
        return any_function()
    return wrapper_function


@decorator_function
def prem():
    """ this is prem function """
    return "this is prem"

print(prem())

print(prem.__doc__)


#wrap = decorator_function(prem)
#print(wrap.__doc__)
#print(wrap())



@decorator_function
def func():    
    return "hello world"

print(func())

@decorator_function
def prem():
    return "this is prem"
print(prem())




#################################################################


def outer_function():
    def inner_function(a):
        return f"this is inner function and my id is {a}"
    return inner_function


prem = outer_function()
print(prem(67))


def decorator_function(any_function):
    def wrapper_function(*args , **kwargs):
        print("this is  caculator function")
        return any_function(*args , **kwargs)
    return wrapper_function



@decorator_function
def calculator(a , b):
    add = a+b
    multy = a*b
    return add , multy

print(calculator(5 , 5 ))



import time

t1 = time.time()
calculator(10 , 10)

t2 = time.time()

total = t2-t1

print(total)




























