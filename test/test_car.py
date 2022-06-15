import unittest
from datetime import datetime

from attr import Factory

from car.car_factory import CarFactory

class TestCalliope(unittest.TestCase):
    factory: CarFactory
    
    def setUp(self):
        super().setUp()
        self.factory = CarFactory()
    
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 1
        last_service_mileage = 0
        wornness = [0.1, 0.5, 1, 0.7]

        car = self.factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 1
        last_service_mileage = 0
        wornness = [0.5, 0.8, 0.7, 0.4]

        car = self.factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    factory: CarFactory
    
    def setUp(self):
        super().setUp()
        self.factory = CarFactory()
        
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wornness = [1, 0.8, 0.9, 0.7]

        car = self.factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wornness = [0.5, 1, 0.4, 0.6]

        car = self.factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    factory: CarFactory
    
    def setUp(self):
        super().setUp()
        self.factory = CarFactory()
    
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = False
        wornness = [0, 0, 0, 0]

        car = self.factory.create_palindrome(today, last_service_date, warning_light_is_on, wornness)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        wornness = [0, 0, 0, 0]

        car = self.factory.create_palindrome(today, last_service_date, warning_light_is_on, wornness)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        wornness = [0, 0, 0, 0]

        car = self.factory.create_palindrome(today, last_service_date, warning_light_is_on, wornness)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wornness = [0, 0, 0, 0]

        car = self.factory.create_palindrome(today, last_service_date, warning_light_is_on, wornness)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wornness = [0.1, 0.5, 1, 0.7]

        car = self.factory.create_palindrome(today, last_service_date, warning_light_is_on, wornness)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wornness = [0.5, 0.8, 0.7, 0.4]

        car = self.factory.create_palindrome(today, last_service_date, warning_light_is_on, wornness)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    factory: CarFactory
    
    def setUp(self):
        super().setUp()
        self.factory = CarFactory()
    
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_roschach(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_roschach(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_roschach(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_roschach(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wornness = [1, 0.8, 0.9, 0.7]

        car = self.factory.create_roschach(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wornness = [0.5, 1, 0.4, 0.6]

        car = self.factory.create_roschach(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())
    


class TestThovex(unittest.TestCase):
    factory: CarFactory
    
    def setUp(self):
        super().setUp()
        self.factory = CarFactory()
    
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wornness = [0, 0, 0, 0]

        car = self.factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 1
        last_service_mileage = 0
        wornness = [0.1, 0.5, 1, 0.7]

        car = self.factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 1
        last_service_mileage = 0
        wornness = [0.5, 0.8, 0.7, 0.4]

        car = self.factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wornness)
        self.assertFalse(car.needs_service())



if __name__ == '__main__':
    unittest.main()
