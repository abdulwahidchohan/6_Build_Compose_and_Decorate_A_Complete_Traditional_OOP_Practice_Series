class Car:
    def _init_(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand} car started.')    

my_car = Car("Toyata")
print(my_car.brand)
my_car.start()        