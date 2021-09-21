"""def add(a , b):
    return a+b

addition = lambda a , b: a+b

print(addition(5 , 8))

age = int(input("enter your age : "))

#ad = lambda age : age if(age < 18)
#print(ad(age))



def ad(age):
    if age < 18:      
        print ("not adult")
#ad(age)

ad = lambda  age : ["not adult" if age < 18 else "adult" for i in range(1)]
print(ad())"""


"""def hcf(a , b):
    if a<b:
        small = a
    else:
        small = b

    for i in range(1 , small+1):
        if a%i==0 and b%i==0:
            hcf = i

    return hcf
#print(hcf(20 , 40))"""



hcf = lambda a , b : [i for i in range(1 , min(a , b)+1) if a%i==0 and b%i == 0]
print(hcf(10 , 20)[-1])

even = lambda : [i for i in range(1 , 21) if i%4==0]
print(even())

def mix():
    num = []
    for i in range(1 , 21):
        if i%2==0:
            num.append(i**2)
        else:
            num.append(i**3)
    return num

mix = lambda : [i**2 if i%2==0 else i**3 for i in range(1 , 21)]
print(mix())

for i in range(1,6):
    
    for j in range(i):
        print(i , end = "")
    print()

#print(len.__doc__)


def add(a , b):
    """ this function takes two arguments and return their sum"""
    return a+b
print(add(5 , 5))
print(add.__doc__)







