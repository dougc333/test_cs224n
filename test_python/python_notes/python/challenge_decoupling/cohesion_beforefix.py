import string
import random


class VehicleRegistry:
    def gen_vehicle_id(self, len: int):
        return "".join(random.choices(string.ascii_letters, k=len))

    def generate_license(self):
        return ''.join(random.sample(string.ascii_uppercase + string.digits, k=7))


class Application:
    def register_vehicle(self, brand: str):
        registry = VehicleRegistry()
        vehicle_id = registry.gen_vehicle_id(12)
        license_plate = registry.generate_license()

        catalog_price = 0
        if brand == 'Tesla Model 3':
            catalog_price = 100000
        elif brand == 'ID2':
            catalog_price = 40000
        elif brand == 'bmw':
            catalog_price = 50000

        tax_percentage = .05
        if brand == 'Tesla Model 3':
            tax_percentage = 0.03
        payable_tax = tax_percentage * catalog_price

        # print registration
        print("Registartion complete")
        print(f"Brand:{brand}")
        print(f"Id: {vehicle_id}")
        print(f"license: {license_plate}")
        print(f"catalog_price: {catalog_price}")
        print(f"payable tax: {payable_tax}")


app = Application()
app.register_vehicle("Tesla Model 3")

