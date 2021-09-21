num = {1,2,3,4,5 , 5 , 4 , 6 , 87, 8}
#for i in num:
    #print(i)
num.discard(5)
print(num)

num.add(10)
print(num)


#################################3Comprehention############################

num = []
for i in range(1,21):
    if i%2==0:
        num.append(i**2)
    else:
        num.append(i**3)
    
    
    
#number = [i for i in range(1,21)]    #append, for loop
#number = [i for i in range(1,21) if i%2==0] ## append for loop condition
number = [i**2 if i%2==0 else i**3 for i in range(1,21) ] # append codition for loop
print(number)
print(num)


a = int(input("enter first number : "))
b = int(input("enter second number : "))
for i in range(1 , min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf = i
#print(hcf)


hcf = [i for i in range(1 , min(a , b)+1) if a%i==0 and b%i==0]
print(hcf[-1])


even = {i : "even" if i%2==0  else "odd" for i in range(1 , 11) }
print(even)


#names = ["rahul" , "vishal" , "nikhil" , "prabhat" , "nitish"]
#for i in enumerate(names):
    #print(i)








































