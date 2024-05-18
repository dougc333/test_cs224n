from dataclasses import dataclass
import random
import string


@dataclass
class Car:
    brand: str
    tax_percentage: float


class Sales:
    def __init__(self, car: Car):
        self.car = car
        self.catalog_price: float = self.calcPrice()
        self.payable_tax: float = self.calcTax()

    def calcPrice(self) -> float:
        catalog_price = 0.
        if self.car.brand == 'Tesla Model 3':
            catalog_price = 100000
        elif self.car.brand == 'ID2':
            catalog_price = 40000
        elif self.car.brand == 'bmw':
            catalog_price = 50000
        return catalog_price

    def calcTax(self) -> float:
        payable_tax = 0.0
        if self.car.brand == 'Tesla Model 3':
            payable_tax = self.car.tax_percentage * self.calcPrice()
        return payable_tax


class VehicleRegistry:
    def gen_vehicle_id(self, len: int = 7):
        return "".join(random.choices(string.ascii_letters, k=7))

    def generate_license(self, len: int = 7):
        return ''.join(random.sample(string.ascii_uppercase + string.digits, k=len))


class Register:
    def __init__(self, sale: Sales):
        self.sale = sale
        self.vehicle_id: str
        self.licensePlate: str
        self.getIdAndLicense()
        self.print()

    def getIdAndLicense(self):
        v = VehicleRegistry()
        self.id = v.gen_vehicle_id()
        self.licensePlate = v.generate_license()

    def print(self):
        print("Registartion complete")
        print(f"Brand:{self.sale.car.brand}")
        print(f"Id: {self.vehicle_id}")
        print(f"license: {self.licensePlate}")
        print(f"catalog_price: {self.sale.catalog_price}")
        print(f"payable tax: {self.sale.payable_tax}")


# create a car, sell teh car, register the car.
car = Car("Tesla Model 3", .02)
sale = Sales(car)
register = Register(sale)

# test by adding a new vehicle
# identify teh data and separate the data from teh code
