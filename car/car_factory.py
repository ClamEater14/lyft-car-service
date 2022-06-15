from datetime import datetime

from car.car import Car
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine


class CarFactory:
	def __init__(self) -> None:
		return
	
	def create_calliope(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
		e: CapuletEngine = CapuletEngine(last_service_mileage, current_mileage)
		b: SpindlerBattery = SpindlerBattery(last_service_date, current_date)
		return Car(e, b)
		
	def create_glissade(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
		e: WilloughbyEngine = WilloughbyEngine(last_service_mileage, current_mileage)
		b: SpindlerBattery = SpindlerBattery(last_service_date, current_date)
		return Car(e, b)
	
	def create_palindrome(self, current_date: datetime, last_service_date: datetime, warning_light_on: bool) -> Car:
		e: SternmanEngine = SternmanEngine(warning_light_on)
		b: SpindlerBattery = SpindlerBattery(last_service_date, current_date)
		return Car(e, b)
	
	def create_roschach(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
		e: WilloughbyEngine = WilloughbyEngine(last_service_mileage, current_mileage)
		b: NubbinBattery = NubbinBattery(last_service_date, current_date)
		return Car(e, b)
	
	def create_thovex(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
		e: CapuletEngine = CapuletEngine(last_service_mileage, current_mileage)
		b: NubbinBattery = NubbinBattery(last_service_date, current_date)
		return Car(e, b)