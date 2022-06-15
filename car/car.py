from abc import ABC, abstractmethod
from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable


class Car(Serviceable):
    engine: Engine = None
    battery: Battery = None
    
    def __init__(self, engine: Engine, battery: Battery):
        if engine is None:
            raise TypeError("engine must not be None!")
        
        if battery is None:
            raise TypeError("battery must not be None!")
        
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        battery_service = self.battery.needs_service()
        engine_service = self.engine.needs_service()
        return battery_service or engine_service
