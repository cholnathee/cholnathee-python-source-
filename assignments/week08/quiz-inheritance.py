""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

สร้างลำดับชั้นของคลาส (Class Hierarchy):

    คลาสหลัก (Base class) ชื่อ Vehicle มีคุณลักษณะ (attributes) ได้แก่ brand, model, year
    คลาสย่อย (Derived class) ชื่อ Car มีคุณลักษณะเพิ่มเติมคือ number_of_doors
    กำหนดเมธอด get_info() ในทั้งสองคลาส

"""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle: {self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return (f"Car: {self.year} {self.brand} {self.model}, "
                f"{self.number_of_doors} doors")

my_car = Car("BMW", "M3", 2000, 4)
print(my_car.get_info())
print(my_car.model)
print(my_car.brand)
print(my_car.year)
print(my_car.number_of_doors)
