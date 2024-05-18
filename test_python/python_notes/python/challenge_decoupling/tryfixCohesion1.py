class VehicleInfo:
    brand: str
    catalog_price: float
    electric: bool

    def __init__(self, brand: str, catalog_price: float, electric: bool):
        self.brand = brand
        self.catalog_price = catalog_price
        self.electric = electric

    def compute_tax(self):
        """
        """
        pass

    def print(self):
        '''
        '''


class Vehicle:
    id: str
    license_plate: str
    vehicle_info: VehicleInfo

    def __init__(self, id: str, license_plate: str, vehicle_info: VehicleInfo):
        self.id = id
        self.license_plate = license_plate
        self.vehicle_info = vehicle_info

    def print(self):
        '''
        '''


class VehicleRegistry:
    self.vehicle_info = {}

    def add_vehicle_info(self, ):