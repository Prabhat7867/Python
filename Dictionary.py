def prem(a , b):
    if a*b > 1000:
        return a+b
    else:
        return a*b
print(prem(5 , 10) + 40)


################# Dictionary ###########################3
user_info = {
       "name" : "aniket",
       "age" : 25,
       "fav_movies" : ["gadar" , "diljale" , "agneepat" , "avengers"],
       "fav_sports" : ["cricket" , "basketball" , "hockey"]
    }
user_info["fav_movies"].pop()
for i in user_info.keys():
    print(i)

for i in user_info.values():
    print(i)

for k , v in user_info.items():
    print(f"{k} : {v}")

name = "nitish"
age = 20

#print("my name is" + " " + name + " " + "and my age is" + " " + str(age))
#print(f"my name is {name} and my age is {age}")

user_info["games"] = ["card", "asphlt" , "bgmi" , "candycrush"]
print(user_info)

more_info = {
            "mobile" : "samsunf",
            "device" : "laptop"
    }
user_info.update(more_info)
print(user_info)











    
