class Person:
    def __init__(self , name , last_name , age , salary ):
        self.name = name
        self.age = age
        self.salary = salary
        self.last_name = last_name

    def full_info(self):
        return f"my name is {self.name} and my age is {self.age}"

P1 = Person("rahul" , "singh" , 34 , 45000)
P2 = Person("shivam" , "bharti" , 43 , 55000)

print(P1.full_info())
        

class Laptop:
    def __init__(self , brand_name , model , price):
        self.brand_name = brand_name
        self.model = model
        self.price = price

    def discount(self , num):
        return self.price - (num / 100) * self.price



L1 = Laptop("Hp" , "abc123" , 34000)
L2 = Laptop("Asus" , "mvgf" , 56000)

print(L1.discount(12))



class Height():

    def converter(self ,num):
        return 2.54 * 12* num


H1 = Height()
print(H1.converter(6.2))


class Circle:
    pi = 3.14
    def __init__(self , radius ):
        self.radius = radius
        

    def circumference(self):
        return 2*Circle.pi *self.radius




C1 = Circle(5 )
C2 = Circle(4 )
print(C1.circumference())



class Phone:
    def __init__(self , brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def full_name(self):
        return f"{self.brand} {self.model} {self.price}"



class Smartphone(Phone):
    def __init__(self , brand , model , price , ram , internal_memory , battery):
        super().__init__(brand , model , price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.battery = battery

    def specification(self):
        return f"brand : {self.brand} model : {self.model} ram : {self.ram} internal_memory : {self.internal_memory} price : {self.price}"
        
        

Phone1 = Phone("Realme" , "Narzo" , 13000)
Phone2 = Phone("LG" , "g7plus" , 50000)
s1 = Smartphone("Redmi" , "9power" , 11000 , "4GB" , "64GB" , "6000MZ")
print(s1.specification())
print(s1.brand)
        






































