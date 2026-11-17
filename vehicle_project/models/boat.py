from models.vehicle import Vehicle
class boat(Vehicle):
    def __init__(self, brand,model,year,oars,passengers):
        super().__init__(brand, model,year)
        self.oars = oars
        self.passengers = passengers
    def get_info(self):
        return f"{super().get_info()},oars:{self.oars},passengers:{self.passengers}"
    def move(self):
        return("boar is swim")