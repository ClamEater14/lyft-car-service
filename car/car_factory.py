from typing import List
from datetime import datetime

from car.car import Car
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
	def __init__(self) -> None:
		return
	
	def create_calliope(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wornness: List[float]) -> Car:
		e: CapuletEngine = CapuletEngine(last_service_mileage, current_mileage)
		b: SpindlerBattery = SpindlerBattery(last_service_date, current_date)
		t: CarriganTires = CarriganTires(wornness)
		return Car(e, b, t)
		
	def create_glissade(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wornness: List[float]) -> Car:
		e: WilloughbyEngine = WilloughbyEngine(last_service_mileage, current_mileage)
		b: SpindlerBattery = SpindlerBattery(last_service_date, current_date)
		t: OctoprimeTires = OctoprimeTires(wornness)
		return Car(e, b, t)
	
	def create_palindrome(self, current_date: datetime, last_service_date: datetime, warning_light_on: bool, wornness: List[float]) -> Car:
		e: SternmanEngine = SternmanEngine(warning_light_on)
		b: SpindlerBattery = SpindlerBattery(last_service_date, current_date)
		t: CarriganTires = CarriganTires(wornness)
		return Car(e, b, t)
	
	def create_roschach(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wornness: List[float]) -> Car:
		e: WilloughbyEngine = WilloughbyEngine(last_service_mileage, current_mileage)
		b: NubbinBattery = NubbinBattery(last_service_date, current_date)
		t: OctoprimeTires = OctoprimeTires(wornness)
		return Car(e, b, t)
	
	def create_thovex(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wornness: List[float]) -> Car:
		e: CapuletEngine = CapuletEngine(last_service_mileage, current_mileage)
		b: NubbinBattery = NubbinBattery(last_service_date, current_date)
		t: CarriganTires = CarriganTires(wornness)
		return Car(e, b, t)