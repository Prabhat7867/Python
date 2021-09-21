### Iterator --- filter , map , reduce , etc
### iterables -- list , string , tuples ,etc

num = list(range(1,21))

def is_even(a):
    return a%2==0
#print(is_even)

even = filter(is_even , num)

#for i in even:
    #print(i)


even1 = list(even)
for i in even1:
    print(i)
    
for i in even1:
    print(i)

odd = list(filter(lambda a : a%2!=0 , num))
print(odd)

### map

square = tuple(map(lambda a : a**2 , num))
print(square)

### reduce

import functools


def add(a , b):
    return a+b


a = functools.reduce(add , num )
print(a)

num = list(range(1 , 21))
multy = functools.reduce(lambda a , b : a*b , num)
print(multy)


###############class ################################

class Person:
    def __init__(self , name , id_ , last_name):
        self.name = name
        self.id_ = id_
        self.last_name = last_name

P1 = Person("prabhat" , "abc123" , "rajput")
P2 = Person("tarun" , "420" , "gilhari")
print(P2.id_)


































