from datetime import datetime
from battery.battery import Battery
from dateutil.relativedelta import relativedelta

class NubbinBattery(Battery):
	last_service_date: datetime
	current_date: datetime
	
	def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
		super().__init__()
		self.last_service_date = last_service_date
		self.current_date = current_date
	
	def needs_service(self) -> bool:
		service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
		return service_threshold_date < self.current_date