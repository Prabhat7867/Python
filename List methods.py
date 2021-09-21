#2. insert
number = [1,2,3,4,5]
#number.insert(3, 78)
#print(number)


################# delete data from list ##############33

#1. pop
number.pop(2)
print(number)

#2. remove

name = ["prem" ,"rahul" , "mohit"]
name.remove("rahul")
print(name)

## sort
num = [5 , 4 , 1 , 2 , 67]
num.sort()
print(num)

##copy

a = [1,2,3,4,5]
b = a.copy()
b.pop()
print(b)

##############even odd#############3
num1 = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in num1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)






























