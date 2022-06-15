from tires.tires import Tires


class CarriganTires(Tires):
	def needs_service(self) -> bool:
		for _, w in enumerate(self.wornness):
			if w >= 0.9:
				return True
		
		return False