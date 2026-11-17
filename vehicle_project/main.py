from models.car import Car
from models.Truck import Truck
from models.motorcycle import Motorcycle
from models.boat import boat
from garage import Garage
def main():
    boat1=boat("BRO Boats","BRO 370",2025,2,3)
    car1=Car("BMW","M5",2024,4)
    truck1=Truck("Volvo","FH16",2023,25)
    Motorcycle1=Motorcycle("Honda","CBR600",2024, True)
    vehicle1=[car1,truck1,Motorcycle1,boat1]
    for vehicle in vehicle1:
        vehicle.move()
        print(vehicle.get_info())
    garage=Garage()
    for vehicle in vehicle1:
        garage.add_vehicle(vehicle)
    print(garage.show_all())
    fon=garage.find_by_brand("Honda")
    for vehicle in fon:
        print(vehicle.get_info())
if __name__=="__main__":
    main()