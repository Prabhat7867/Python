num = [2 , 2 , 0 , 4]
"""add = 0
for i in num:
    add = add + i
print(add)"""

add = ""
for i in num:
    add = add+ str(i)
print(add)

###################################################################
names = ["prem" , "shivam" , "kajal" , "shalu" , "shivani"]
even = []
for i in names:
    if len(i) %2==0:
        even.append(i)

print(even)
###################################################################


num = list(range(1,21))
def even_odd(num):
    
    even = []
    odd = []
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd
vishal , aniket = even_odd(num)
print(vishal)
print(aniket)

mix = [1,2,3, "prem" , [1,4,6.8,9]]
mix[4][2] = 6
print(mix)

#######################################Tuples #####################

num1 = (1,2,3,4,5,6,7,8 ,[1,2,3,4])
num1[-1].pop()
print(num1)
for i in num1:
    print(i)
print(type(num1))



############################3Homework ######################3
#1. print fibonacci series
#2. create a function that tells whether a number is prime or not
#3. find HCF of two numbers using function
















    
