string = "abcdefabchgdgf"
d = {}
for i in string:
    d[i] =string.count(i)

print(d)

number = [1,4,5,6,5,7,55,3,56 , 9,89,60]
#five = [i for i in number if i%5==0]
#print(five)
for i in number:
    if i== 55:
        break
    elif i%2!=0:
        print(i)


###########################3
def add(*args):
    a = 0
    for i in args:
        a+=i
    return a
print(add(*(1,2,3,4,5,6)))




user_info = {
          "name" : "aniket",
          "fav_games" : ["chess" , "uno" , "poker"]
    }
def user(**kwargs):
    for k , v in kwargs.items():
        print(f"{k} = {v}")
user(**user_info)

num = [1,2,3,4,5]
for i in num:
    print(i)



#######################################generator#############################


def num(n):
    for i in range(1 , n+1):
        yield(i)

prem = num(20)
for i in prem:
    print(i)

number = (i for i in range(1,101))
print(number)
