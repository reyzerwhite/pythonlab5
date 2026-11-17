from abc import ABC,abstractmethod


class Vehicle(ABC):
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year=year
        self._speed=0
    
    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self._speed = value
    def accelerate(self, value):
        self.speed += value
    def stop(self):
        self.speed = 0
    def brake(self,value):
        self.speed -=value
        if self.speed<0:
            self.speed=0
    def get_info(self):
        return f"brand:{self.brand},model:{self.model},year:{self.year},speed:{self.speed} "
    def __str__(self):
        return f"{self.brand} {self.model}, скорость: {self.speed}км/ч"
    @abstractmethod
    def move(self):
        pass


