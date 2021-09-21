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


class Super_smartphone(Smartphone):
    count = 0
    def __init__(self , brand , model , price , ram , internal_memory , battery,front_camera):
        Super_smartphone.count = Super_smartphone.count+1
        super().__init__(brand , model , price , ram , internal_memory , battery) 
        self.front_camera = front_camera

    def product_info(self):
        return f"{self.brand} {self.front_camera}"

    def instance_count(self):
        return f"i have created {Super_smartphone.count} instances"

    def __add__(self , other):
        return self.price + other.price
        


S1 = Super_smartphone("samsung" , "abc123" , 43900 , "5GB" , "234GB" , "6000MH" , "15MP")
S2 = Super_smartphone("samsung" , "ab" , 70000 , "5GB" , "256GB" , "5000MH" , "15MP")

print(S1.instance_count())
print(S1 + S2)


class A:

    def method_A(self):
        return "this is method A"

    def hello(self):
        return "this is hello method"



class B:
    def method_B(self):
        return "this is method B"

    def hello(self):
        return "this is hello function"

class C(A , B):
    pass

C1 = C()

print(C1.hello())

#print(help(C))









        



















    
    
