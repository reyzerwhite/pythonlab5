class Garage:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def remove_vechicle(self,vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
        else:
            return "Транспорт не найден"
    def show_all(self):
        for vehicle in self.vehicles:
            print(vehicle)
    def find_by_brand(self,brand):
        result=[]
        for vehicle in self.vehicles:
            if vehicle.brand.lower()==brand.lower():
                result.append(vehicle)
        return result
