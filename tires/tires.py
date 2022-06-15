from abc import ABC, abstractmethod
from typing import List


class Tires(ABC):
	wornness: List[float]
	
	def __init__(self, wornness: List[float]) -> None:
		super().__init__()
		self.wornness = wornness
		
	
	@abstractmethod
	def needs_service(self) -> bool:
		pass