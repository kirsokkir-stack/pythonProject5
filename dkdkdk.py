class Vehicle:
    speed = 60
    _vin = ""
    def __init__(self, speed_from_user, vin_from_user):
        self._vin = vin_from_user
        self._speed = speed_from_user
    def show_speed(self):
        print(f"Speed of vehicle: {self._speed}")
    def show_vin(self):
        print(f'Vin of vehicle: {self._vin[0:3]}')
    def get_vin(self):
        return f'Vin of vehicle: {self._vin[0:3]}'
class Bus(Vehicle):
    def __init__(self, speed_from_user, vin_from_user, decks_number_from_user):
        super().__init__(speed_from_user, vin_from_user)
        self._decks_number = decks_number_from_user
    def print_info(self):
        print(f'Speed: {self._speed}, Dekcs: {self._decks_number}, Vin: {self.get_vin()}')

bus = Bus(100, 'Dubciuse8723', 2)
bus.print_info()